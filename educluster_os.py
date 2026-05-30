#!/usr/bin/env python3
"""EduCluster OS all-in-one code file.

Run modes:

    python3 educluster_os.py host
    python3 educluster_os.py core --host 0.0.0.0 --port 5050
    python3 educluster_os.py ai "explain tcp bridge"

This single file contains:

- Node 1 graphical shell
- Node 2 TCP processing server
- Local AI tutor
- Built-in tasks and settings
"""

from __future__ import annotations

import argparse
import html
import json
import math
import os
import platform
import queue
import random
import re
import socket
import subprocess
import sys
import threading
import time
import urllib.parse
import urllib.request
from dataclasses import dataclass
from typing import Any, Callable

import tkinter as tk
from tkinter import scrolledtext


SETTINGS = {
    "node_name": "EduCluster-2X",
    "core_host": "192.168.50.2",
    "core_port": 5050,
    "top_screen": {"x": 0, "y": 0, "width": 480, "height": 320},
    "bottom_screen": {"x": 0, "y": 320, "width": 480, "height": 320},
}

PALETTE = {
    "bg": "#06111f",
    "panel": "#101d32",
    "text": "#e5edf7",
    "muted": "#94a3b8",
    "accent": "#38bdf8",
    "green": "#22c55e",
    "yellow": "#f59e0b",
    "red": "#ef4444",
    "button": "#1e293b",
    "button_active": "#334155",
}

TASKS = [
    {
        "id": "python_print",
        "title": "Python: Print Output",
        "category": "Python",
        "difficulty": "Beginner",
        "prompt": "Write a Python command that prints Hello EduCluster.",
        "hint": "Use print('text').",
        "expected_keywords": ["print", "hello"],
    },
    {
        "id": "linux_pwd",
        "title": "Linux: Current Folder",
        "category": "Linux",
        "difficulty": "Beginner",
        "prompt": "Which command shows the current working directory?",
        "hint": "It is three letters.",
        "expected_keywords": ["pwd"],
    },
    {
        "id": "network_ping",
        "title": "Networking: Ping",
        "category": "Networking",
        "difficulty": "Beginner",
        "prompt": "Which command tests whether another host is reachable?",
        "hint": "It sends ICMP echo requests.",
        "expected_keywords": ["ping"],
    },
    {
        "id": "socket_role",
        "title": "Networking: Client and Server",
        "category": "Networking",
        "difficulty": "Intermediate",
        "prompt": "In a TCP connection, which side waits and listens on a port?",
        "hint": "Node 2 is doing this in the project.",
        "expected_keywords": ["server"],
    },
]

BUILTIN_DOCS = [
    {
        "id": "system.overview",
        "title": "EduCluster overview",
        "text": (
            "EduCluster-2X is a two-node Raspberry Pi learning computer. Node 1 "
            "runs the graphical shell and touch interface. Node 2 runs a headless "
            "sandbox server. The nodes communicate over a short wired Ethernet "
            "bridge using JSON messages."
        ),
    },
    {
        "id": "ui.shell",
        "title": "OS shell interface",
        "text": (
            "The host interface behaves like a lightweight desktop shell. The top "
            "display shows status, logs, bridge responses, and progress. The bottom "
            "display shows the launcher, learning cards, bridge controls, console "
            "notes, and system status."
        ),
    },
    {
        "id": "network.tcp",
        "title": "TCP bridge",
        "text": (
            "TCP provides a reliable ordered byte stream. In EduCluster, Node 1 is "
            "the client and Node 2 is the server. Commands are serialized as JSON, "
            "sent over Ethernet, processed on Node 2, and returned as text."
        ),
    },
    {
        "id": "safety.rules",
        "title": "Safety rules",
        "text": (
            "The school project shell avoids destructive remote commands. Touch "
            "buttons request safe tasks, explanations, summaries, or simulations "
            "instead of executing arbitrary shell strings."
        ),
    },
]

STOP_WORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "how",
    "i", "in", "is", "it", "of", "on", "or", "that", "the", "this", "to",
    "what", "when", "where", "which", "who", "why", "with", "you", "your",
}


@dataclass
class Document:
    id: str
    title: str
    text: str


@dataclass
class Answer:
    mode: str
    text: str
    confidence: float
    sources: list[str]


@dataclass
class SearchResult:
    title: str
    url: str
    snippet: str


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip())


def tokens(text: str) -> list[str]:
    return [
        token
        for token in re.findall(r"[a-zA-Z0-9_]+", text.lower())
        if token not in STOP_WORDS and len(token) > 1
    ]


def sentence_split(text: str) -> list[str]:
    return [part for part in re.split(r"(?<=[.!?])\s+", normalize(text)) if part]


def strip_html(raw: str) -> str:
    raw = re.sub(r"<script.*?</script>", " ", raw, flags=re.I | re.S)
    raw = re.sub(r"<style.*?</style>", " ", raw, flags=re.I | re.S)
    raw = re.sub(r"<[^>]+>", " ", raw)
    return normalize(html.unescape(raw))


def run_text_command(command: list[str], timeout: float = 1.0) -> str:
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=timeout, check=False)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return f"unavailable: {exc}"
    return (result.stdout or result.stderr or "").strip()


class KnowledgeBase:
    def __init__(self) -> None:
        docs = [Document(**item) for item in BUILTIN_DOCS]
        for item in TASKS:
            docs.append(
                Document(
                    id=f"task.{item['id']}",
                    title=item["title"],
                    text=" ".join(str(item[key]) for key in ("category", "difficulty", "prompt", "hint")),
                )
            )
        self.docs = docs
        self.doc_tokens = {doc.id: tokens(doc.title + " " + doc.text) for doc in docs}
        self.df = self._document_frequency()

    def _document_frequency(self) -> dict[str, int]:
        df: dict[str, int] = {}
        for toks in self.doc_tokens.values():
            for token in set(toks):
                df[token] = df.get(token, 0) + 1
        return df

    def search(self, query: str, limit: int = 5) -> list[tuple[float, Document]]:
        query_tokens = tokens(query)
        scored = [(self._score(query_tokens, doc), doc) for doc in self.docs]
        scored = [(score, doc) for score, doc in scored if score > 0]
        scored.sort(key=lambda item: item[0], reverse=True)
        return scored[:limit]

    def _score(self, query_tokens: list[str], doc: Document) -> float:
        toks = self.doc_tokens[doc.id]
        counts: dict[str, int] = {}
        for token in toks:
            counts[token] = counts.get(token, 0) + 1
        total = max(1, len(toks))
        score = 0.0
        n_docs = max(1, len(self.docs))
        for token in query_tokens:
            tf = counts.get(token, 0) / total
            idf = math.log((1 + n_docs) / (1 + self.df.get(token, 0))) + 1
            score += tf * idf
        title_bonus = sum(1 for token in query_tokens if token in tokens(doc.title)) * 0.2
        return score + title_bonus


class LocalTutor:
    def __init__(self, seed: int | None = None) -> None:
        self.kb = KnowledgeBase()
        self.random = random.Random(seed)

    def answer(self, prompt: str) -> Answer:
        prompt = normalize(prompt)
        lowered = prompt.lower()
        if not prompt or lowered in {"help", "commands", "?"}:
            return self.help()
        if lowered.startswith("search "):
            return self.web_search(prompt[7:])
        if lowered.startswith("quiz ") or lowered.startswith("question "):
            return self.quiz(prompt.split(" ", 1)[1])
        if lowered.startswith("plan "):
            return self.plan(prompt.split(" ", 1)[1])
        if lowered.startswith("summarize "):
            return self.summarize(prompt[10:])
        return self.explain(prompt)

    def help(self) -> Answer:
        return Answer(
            "help",
            "Commands: explain <topic>, quiz <topic>, plan <topic>, summarize <text>, search <query>",
            1.0,
            [],
        )

    def explain(self, topic: str) -> Answer:
        matches = self.kb.search(topic, limit=4)
        if not matches:
            return Answer("explain", "I do not know that topic yet. Try Python, Linux, TCP, sockets, or cluster.", 0.2, [])
        lines = [f"Explanation for '{topic}':"]
        for _, doc in matches:
            lines.append(f"- {best_sentence(doc.text, topic)}")
        return Answer("explain", "\n".join(lines), 0.72, [doc.id for _, doc in matches])

    def quiz(self, topic: str) -> Answer:
        matches = self.kb.search(topic, limit=8) or self.kb.search("python socket linux", limit=8)
        _, doc = self.random.choice(matches)
        key_terms = tokens(doc.title + " " + doc.text)[:6]
        term = self.random.choice(key_terms) if key_terms else "system"
        return Answer(
            "quiz",
            f"QUESTION: Explain how '{term}' is used in: {doc.title}.\nHINT: {best_sentence(doc.text, term)}",
            0.8,
            [doc.id],
        )

    def plan(self, topic: str, minutes: int = 25) -> Answer:
        matches = self.kb.search(topic, limit=5) or self.kb.search("cluster python tcp", limit=5)
        chunk = max(5, minutes // max(1, len(matches)))
        lines = [f"Study plan for {topic} ({minutes} minutes):"]
        for index, (_, doc) in enumerate(matches, start=1):
            lines.append(f"{index}. {chunk} min - {doc.title}: {best_sentence(doc.text, topic)}")
        lines.append("Final check: explain the idea without reading notes.")
        return Answer("plan", "\n".join(lines), 0.84, [doc.id for _, doc in matches])

    def summarize(self, text: str) -> Answer:
        sentences = sentence_split(text)
        if len(sentences) <= 3:
            return Answer("summary", normalize(text), 0.7, [])
        ranked = sorted(sentences, key=lambda item: score_overlap(item, "raspberry pi python socket network display learning safe system"), reverse=True)
        return Answer("summary", " ".join(ranked[:4]), 0.75, [])

    def web_search(self, query: str) -> Answer:
        results = simple_web_search(query)
        lines = [f"Web results for: {query}"]
        for index, result in enumerate(results[:5], start=1):
            lines.append(f"{index}. {result.title}")
            if result.url:
                lines.append(f"   {result.url}")
            if result.snippet:
                lines.append(f"   {result.snippet}")
        return Answer("web_search", "\n".join(lines), 0.62, [result.url for result in results if result.url])


def best_sentence(text: str, query: str) -> str:
    sentences = sentence_split(text)
    if not sentences:
        return normalize(text)
    return max(sentences, key=lambda sentence: score_overlap(sentence, query))


def score_overlap(text: str, query: str) -> int:
    q = set(tokens(query))
    return sum(1 for token in tokens(text) if token in q)


def simple_web_search(query: str, limit: int = 5) -> list[SearchResult]:
    encoded = urllib.parse.urlencode({"q": query})
    url = f"https://duckduckgo.com/html/?{encoded}"
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "EduCluster/1.0"})
        with urllib.request.urlopen(request, timeout=8) as response:
            page = response.read(512_000).decode("utf-8", errors="replace")
    except Exception as exc:
        return [SearchResult("Search unavailable", "", str(exc))]
    results: list[SearchResult] = []
    for block in re.split(r"result__body", page)[1 : limit + 1]:
        title_match = re.search(r'class="result__a[^>]*>(.*?)</a>', block, re.S)
        link_match = re.search(r'href="([^"]+)"[^>]*class="result__a', block)
        snippet_match = re.search(r'class="result__snippet[^>]*>(.*?)</', block, re.S)
        if not title_match:
            continue
        results.append(
            SearchResult(
                strip_html(title_match.group(1)),
                html.unescape(link_match.group(1)) if link_match else "",
                strip_html(snippet_match.group(1)) if snippet_match else "",
            )
        )
    return results or [SearchResult("No parsed results", url, "Try a different query.")]


class LearningEngine:
    def __init__(self) -> None:
        self.tasks = TASKS
        self.started_at = time.time()
        self.ai = LocalTutor()

    def handle(self, payload: dict[str, Any]) -> str:
        command = str(payload.get("command", "")).strip().lower()
        args = payload.get("args", {})
        if command == "status":
            return self.status()
        if command == "next_task":
            return self.next_task()
        if command == "packet_stats":
            return self.packet_stats()
        if command == "explain":
            return self.ai.answer("explain " + str(args.get("topic", ""))).text
        if command == "ai":
            return self.ai.answer(str(args.get("prompt", ""))).text
        return f"Unknown safe command: {command}"

    def status(self) -> str:
        return f"CORE STATUS\ntasks_loaded={len(self.tasks)}\nuptime_seconds={int(time.time() - self.started_at)}\nmode=safe_learning_core"

    def next_task(self) -> str:
        task = random.choice(self.tasks)
        return f"TASK: {task['title']}\nCATEGORY: {task['category']}\nDIFFICULTY: {task['difficulty']}\n\n{task['prompt']}\n\nHINT: {task['hint']}"

    def packet_stats(self) -> str:
        return f"PACKET SIMULATION\nrx_packets={random.randint(40, 500)}\nbridge_latency_ms={round(random.uniform(1, 12), 2)}\ndropped_frames={random.randint(0, 3)}"


class SandboxCoreServer:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self.engine = LearningEngine()

    def serve_forever(self) -> None:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server.bind((self.host, self.port))
            server.listen(5)
            print(f"EduCluster core listening on {self.host}:{self.port}")
            while True:
                conn, addr = server.accept()
                threading.Thread(target=self.handle_client, args=(conn, addr), daemon=True).start()

    def handle_client(self, conn: socket.socket, addr: tuple[str, int]) -> None:
        with conn:
            buffer = b""
            while True:
                chunk = conn.recv(4096)
                if not chunk:
                    return
                buffer += chunk
                while b"\n" in buffer:
                    line, buffer = buffer.split(b"\n", 1)
                    if not line.strip():
                        continue
                    try:
                        payload = json.loads(line.decode("utf-8"))
                    except json.JSONDecodeError as exc:
                        response = f"Invalid JSON: {exc}"
                    else:
                        response = self.engine.handle(payload)
                    stamp = time.strftime("%H:%M:%S")
                    conn.sendall(f"[{stamp}] from={addr[0]}\n{response}\n".encode("utf-8"))


class CoreClient:
    def __init__(self, host: str, port: int, on_message: Callable[[str], None]) -> None:
        self.host = host
        self.port = port
        self.on_message = on_message
        self.sock: socket.socket | None = None
        self.connected = False

    def connect(self) -> None:
        if self.sock is not None:
            return
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(4)
        sock.connect((self.host, self.port))
        sock.settimeout(None)
        self.sock = sock
        self.connected = True
        threading.Thread(target=self.reader, daemon=True).start()

    def send(self, command: str, args: dict[str, Any] | None = None) -> None:
        try:
            if self.sock is None:
                self.connect()
            assert self.sock is not None
            self.sock.sendall(json.dumps({"command": command, "args": args or {}}).encode("utf-8") + b"\n")
        except OSError as exc:
            self.on_message(f"CLIENT ERROR: {exc}")
            self.close()

    def reader(self) -> None:
        assert self.sock is not None
        buffer = b""
        while self.sock is not None:
            try:
                chunk = self.sock.recv(4096)
            except OSError:
                self.close()
                return
            if not chunk:
                self.close()
                return
            buffer += chunk
            while b"\n" in buffer:
                line, buffer = buffer.split(b"\n", 1)
                msg = line.decode("utf-8", errors="replace").strip()
                if msg:
                    self.on_message(msg)

    def close(self) -> None:
        if self.sock:
            try:
                self.sock.close()
            except OSError:
                pass
        self.sock = None
        self.connected = False


class EduClusterShell:
    def __init__(self) -> None:
        self.log_queue: queue.Queue[str] = queue.Queue()
        self.client = CoreClient(SETTINGS["core_host"], SETTINGS["core_port"], self.log_queue.put)
        self.top = tk.Tk()
        self.top.title("EduCluster OS")
        g = SETTINGS["top_screen"]
        self.top.geometry(f"{g['width']}x{g['height']}+{g['x']}+{g['y']}")
        self.top.configure(bg=PALETTE["bg"])
        self.bottom = tk.Toplevel(self.top)
        g = SETTINGS["bottom_screen"]
        self.bottom.title("EduCluster Controls")
        self.bottom.geometry(f"{g['width']}x{g['height']}+{g['x']}+{g['y']}")
        self.bottom.configure(bg=PALETTE["bg"])
        self.clock_var = tk.StringVar(value="--:--")
        self.bridge_var = tk.StringVar(value="offline")
        self.build_top()
        self.build_bottom()

    def build_top(self) -> None:
        bar = tk.Frame(self.top, bg=PALETTE["panel"])
        bar.pack(fill=tk.X)
        tk.Label(bar, text=" EduCluster OS", bg=PALETTE["panel"], fg=PALETTE["accent"], font=("DejaVu Sans", 11, "bold")).pack(side=tk.LEFT)
        tk.Label(bar, textvariable=self.bridge_var, bg=PALETTE["panel"], fg=PALETTE["muted"], font=("DejaVu Sans", 9)).pack(side=tk.LEFT, padx=8)
        tk.Label(bar, textvariable=self.clock_var, bg=PALETTE["panel"], fg=PALETTE["text"], font=("DejaVu Sans", 10, "bold")).pack(side=tk.RIGHT, padx=8)
        self.log = scrolledtext.ScrolledText(self.top, bg="#020817", fg="#dbeafe", font=("DejaVu Sans Mono", 9), wrap=tk.WORD)
        self.log.pack(fill=tk.BOTH, expand=True, padx=6, pady=6)
        self.log.configure(state=tk.DISABLED)
        self.append_log("BOOT: shell ready")

    def build_bottom(self) -> None:
        title = tk.Label(self.bottom, text="Learning Console", bg=PALETTE["bg"], fg=PALETTE["text"], font=("DejaVu Sans", 15, "bold"))
        title.pack(fill=tk.X, pady=6)
        grid = tk.Frame(self.bottom, bg=PALETTE["bg"])
        grid.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)
        actions = [
            ("Status", lambda: self.send("status"), PALETTE["green"]),
            ("Task", lambda: self.send("next_task"), PALETTE["accent"]),
            ("Stats", lambda: self.send("packet_stats"), PALETTE["yellow"]),
            ("AI Python", lambda: self.send("ai", {"prompt": "explain python sockets"}), "#2563eb"),
            ("AI Plan", lambda: self.send("ai", {"prompt": "plan networking"}), "#7c3aed"),
            ("Reconnect", self.reconnect, PALETTE["red"]),
        ]
        for index, (label, action, color) in enumerate(actions):
            row, col = divmod(index, 2)
            button = tk.Button(grid, text=label, command=action, bg=color, fg="white", font=("DejaVu Sans", 11, "bold"), relief=tk.FLAT)
            button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
        for row in range(3):
            grid.rowconfigure(row, weight=1)
        for col in range(2):
            grid.columnconfigure(col, weight=1)

    def append_log(self, message: str) -> None:
        self.log.configure(state=tk.NORMAL)
        self.log.insert(tk.END, f"[{time.strftime('%H:%M:%S')}] {message}\n")
        self.log.see(tk.END)
        self.log.configure(state=tk.DISABLED)

    def send(self, command: str, args: dict[str, Any] | None = None) -> None:
        self.log_queue.put(f"UI -> {command}")
        threading.Thread(target=self.client.send, args=(command, args or {}), daemon=True).start()

    def reconnect(self) -> None:
        self.client.close()
        threading.Thread(target=self.try_connect, daemon=True).start()

    def try_connect(self) -> None:
        try:
            self.client.connect()
            self.log_queue.put("Connected to Node 2")
            self.client.send("status")
        except OSError as exc:
            self.log_queue.put(f"Node 2 unavailable: {exc}")

    def tick(self) -> None:
        self.clock_var.set(time.strftime("%H:%M"))
        self.bridge_var.set("online" if self.client.connected else "offline")
        while True:
            try:
                msg = self.log_queue.get_nowait()
            except queue.Empty:
                break
            self.append_log(msg)
        self.top.after(100, self.tick)

    def start(self) -> None:
        threading.Thread(target=self.try_connect, daemon=True).start()
        self.tick()
        self.top.mainloop()


def run_ai(prompt: str) -> None:
    print(LocalTutor().answer(prompt).text)


def main() -> None:
    parser = argparse.ArgumentParser(description="EduCluster OS all-in-one")
    sub = parser.add_subparsers(dest="mode", required=True)
    sub.add_parser("host")
    core = sub.add_parser("core")
    core.add_argument("--host", default="0.0.0.0")
    core.add_argument("--port", type=int, default=5050)
    ai = sub.add_parser("ai")
    ai.add_argument("prompt", nargs="*", default=["help"])
    args = parser.parse_args()
    if args.mode == "host":
        EduClusterShell().start()
    elif args.mode == "core":
        SandboxCoreServer(args.host, args.port).serve_forever()
    elif args.mode == "ai":
        run_ai(" ".join(args.prompt))


if __name__ == "__main__":
    main()
