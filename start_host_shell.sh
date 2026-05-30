#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."
python3 host_ui.py
