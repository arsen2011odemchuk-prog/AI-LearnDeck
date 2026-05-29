# AI-LearnDeck: The Distributed Classroom Sandbox

AI-LearnDeck is an educational, portable dual-screen hardware laboratory designed to make exploring distributed networking, operating system management, and automated scripting completely engaging and safe for students. 

Instead of forcing students to use slow virtual machines that crash or lag a single main computer, this device physically splits the student-machine interface across two hardware boundaries to ensure a 0% user-interface lag environment during complex computer science lessons.

---

##  The Story & Philosophy: Why I Built This

When learning server administration or network routing, students often face a wall of frustrating textbook theory. Running heavy educational scripts on a single micro-computer quickly bottlenecks the CPU, causing screen freezing and system crashes that disrupt the classroom flow. 

I built the **AI-LearnDeck** to turn distributed computing into a tactile, physical experience. By decoupling the interface from the backend learning environment, a student can visually monitor real-time diagnostic packets on the top monitor while actively writing and interacting with custom coding tools on the lower touch panel. It is a miniature, fully independent data center that fits entirely in a backpack, built to teach how real-world cluster infrastructure handles resource scaling.

---
### 📦 Diagram 1: Solderless Component Stacking Matrix (Component Placement)

This structural block diagram details the physical placement and vertical stacking layers within the monolithic plate frame enclosure. It maps out how the power systems, compute nodes, and display units fit neatly side-by-side to establish a rugged, single-piece tablet with no moving parts. The main layout positions the integrated fast-charge power bank flat inside a central baseline cavity to provide a perfectly balanced, transport-ready counterweight for handheld operation.

The processing hardware is split between distinct left and right compartments. To completely eliminate internal wire stress, the compute nodes are organized in an opposed-rotation layout, positioning their native network ports facing directly toward the center bulkhead on a straight line. The twin touchscreen display faceplates press directly down onto the physical processing headers, drawing their required electrical current natively through the pins to ensure the entire dual-monitor profile remains completely compact and securely anchored without loose interior overlapping.
 
 <img width="560" height="420" alt="image" src="https://github.com/user-attachments/assets/3b4547c8-c247-43e0-8b01-94adaa3320a0" />
---

### 🔌 Diagram 2: Power Rails & Hardware Bridges (Electrical Connections)

This wiring blueprint maps out the complete electrical connections, isolated power allocation paths, and data bridges running inside the hardware chassis. It provides a highly transparent, trace-level overview to verify that the entire system operates as a 100% solderless, plug-and-play constructor platform. The schematic paths track how the dual fast-charge power delivery streams route cleanly through vertical steering elbow adapters underneath the mounting plates, bypassing the sidewalls without any cable kinking.

The data matrix highlights the hardwired, zero-leak network bridge linking the two computing units across the central partition. By locking the network ports on a straight horizontal axis, the flat copper patch cable connects the nodes in a perfectly straight line with a zero bend radius, preventing structural cable fatigue. The external high-gain wireless dongle hooks directly into the master USB slot, extending its antenna array through clean top-rail windows to handle external packet sourcing blocks while leaving the interior entirely free of loose wire clutter.

![image](https://stasis.hackclub-assets.com/images/1780096645205-1t6uqx.png)
---

### 💻 Diagram 3: Distributed Data Bus Topology (Information Flow)

This transaction pipeline diagram tracks the behavioral information flow, packet sequences, and processing distribution paths across the dual-node architecture. It visually demonstrates how physical hardware isolation protects data integrity and guarantees a smooth user experience. The workflow tracks how incoming wireless packets are ingested by the master graphical host node, which handles the core operating system and renders live diagnostic readouts onto the primary touch monitor.

When a user triggers a command on the lower touch panel, the request serializes over a lightweight local network socket across the flat copper data bus line. The secondary display is electronically inverted in the operating system kernel to correct the physical rotation, allowing it to function as a seamless interactive control deck. This data loop ensures that the secondary sandbox processing core compiles all background automation scripts and local databases in complete isolation, maintaining absolute runtime safety and executing automated multi-pass security wipes if network boundaries are compromised.

<img width="472" height="617" alt="image" src="https://github.com/user-attachments/assets/de1c6f59-6739-4238-a998-a39dd05ea37c" />

##  Enclosure Mechanics & Geometric Engineering

The device uses a solid-plate, monolithic tablet chassis with zero moving parts, optimized for FDM 3D printing using SUNLU PLA filament. To resolve layout boundaries, the enclosure footprint has been uniformly scaled by a strict parametric multiplier of **0.1060922** to perfectly match the real-world 85 mm x 56 mm face of standard 3.5-inch touchscreens.

### Internal Space Budgeting (Layer-by-Layer Stacking):
The interior layout organizes all hardware components side-by-side into a dense, modular constructor ecosystem that entirely avoids loose wire clutter:

* **The Central Power Bay:** A custom-dimensioned cavity ($153.3 \text{ mm} \times 71.5 \text{ mm} \times 15.2 \text{ mm}$) captures a 25W QTshine Power Delivery supply lying completely flat against the lower structural deck. A precise rectangular I/O window is cut on the outer long-side wall to provide direct, unhindered charging access from the exterior.
* **The Stacked Computing Wings:** The compute units are organized into independent left and right compartments. By utilizing an **"Opposed-Node Rotation"** layout, Node 2 is rotated 180 degrees relative to Node 1 within the horizontal frame. This positions their native Ethernet (LAN) jacks facing directly toward the center bulkhead on a flat line.
* **The Display Faceplates:** Twin CUQI 3.5-inch touchscreen modules clip flush into the top face cutouts. They seat directly onto the physical 40-pin GPIO arrays of their respective single-board computers, siphoning their necessary 5V power natively through the pins without loose cables.
---

##  Clean Solderless Wiring & Hardware Bridge

The AI-LearnDeck relies on a 100% plug-and-play constructor layout that completely bypasses hand-soldering:

1. **The Data Bridge:** Because the processing nodes are arranged in an opposed-rotation layout, a standard **15 cm kenable Flat CAT6 Ethernet cable** connects their network jacks across the central bulkhead partition.
2. **Power Allocation:** The system utilizes **SELIACR Vertical 90-Degree USB-C steering adapters**. These low-profile elbow interconnects redirect the power bank's built-in Type-C Power Delivery lines straight downwards into a below-deck routing corridor, delivering continuous, stable 5V/5A current beneath the mounting plates without wire stretching or hitting the inner casing walls.
3. **External Wireless Array:** An **xruc 1300Mbps Dual-Antenna WiFi Dongle** plugs directly into a blue USB 3.0 port on Node 1. The high-gain 5dBi external antennas pass cleanly through top-rail structural cutouts to optimize network data throughput.
---

##  System Engineering Math & Energy Metrics

* **Mass Budgeting (Ergonomics):**
  $$\text{2x Raspberry Pi 5 (92g)} + \text{2x 3.5" LCD (100g)} + \text{QTshine Power Bank (280g)} + \text{PLA Filament (200g)} \approx \mathbf{472\text{ grams.}}$$
  *The total weight sits below half a kilogram, making it highly portable for student labs.*

* **Power Draw & Battery Lifecycle:**
  At a peak computation draw of approximately 4.0 Amps per hour with localized scripts running simultaneously, the integrated **10,800mAh (10.8 Ah)** power bank provides an active lifecycle curve:
  $$\text{Runtime (Peak load)} = \frac{10.8\text{ Ah}}{4.0\text{ A}} \approx \mathbf{2.7\text{ Hours}}$$
  $$\text{Runtime (Standard idle)} = \frac{10.8\text{ Ah}}{1.5\text{ A}} \approx \mathbf{7.2\text{ Hours}}$$

* **Software Display Rotation:**
  To correct the inverted image on the secondary display caused by the 180-degree physical hardware rotation, a parametric compensation rule is injected into the Linux boot sequence file (`/boot/firmware/config.txt`):
  ```bash
  display_hdmi_rotate=2
  ```
  This flips the rendering pipeline electronically by 180 degrees, keeping both touch interfaces reading uniformly left-to-right.

---

##  Network Isolation & Secure-Purge Protection System

To teach students the core principles of defensive network topology and military-grade data sterilization, the custom learning architecture implements an automated protective sequence:

* **Phase 1: Instant Hardware Isolation (Cut-Off):** 
  If an anomalous threat signature or unauthorized network packet is flagged by the background monitoring system, Node 1 instantly issues an isolation command:
  ```bash
  sudo ifconfig eth0 down
  ```
  This software command drops the wired kenable CAT6 hardware bridge immediately, completely isolating the computational environment on Node 2 and protecting the lab data from external network vectors.
* **Phase 2: Secure Wipe Multi-Pass Routine (Shred):**
  If the breach parameter persists or mechanical case tampering is detected, Node 2 immediately executes a low-level data purge command across its 128GB high-speed MicroSD storage drive to prevent unauthorized extraction:
  ```bash
  shred -uvz -n 3 /home/pi/ai_core/data_bytes/*
  ```
  This forces the system to overwrite all critical educational database sectors, binary blocks, and custom code modules **3 consecutive times** with randomized bit pattern sets before performing a permanent physical deletion, guaranteeing that the files cannot be recovered by forensic tools.

### Bill of Materials (BOM)




| Component | Qty | Purpose | Price (GBP) | Price (USD) | Sourcing Link |
| :--- | :---: | :--- | :---: | :---: | :--- |
| Raspberry Pi 5 (2GB RAM) | 2 | Node 1 (OS & Dual Interface) and Node 2 (AI Engine) | £124.80 | $167.24 | [The Pi Hut](https://thepihut.com/products/raspberry-pi-5?variant=43878483198147) |
| HDMI Touch Screen Module (3.5") | 2 | Dual display array for text outputs (Includes HDMI bridges) |   £45.14 | $60.50 | [Amazon](https://www.amazon.co.uk/Touchscreen-Raspberry-Pixels-Monitor-Stylus/dp/B0CZ8NYSP1/ref=sr_1_30?crid=KGO2DZECZTUQ&dib=eyJ2IjoiMSJ9.tjZdsaqI8q1We7bicUHUjZM3938ptEHNk8ypmXHCPxPtA4x2pJXmSd40pgG-QzQuYY3HghcpetNPmd7mzrDBfAsxYzXNHcVctQzhk5s08Wgqo_YdkXLXCSQtK8vq68w4ZSTSmWugLIoKZCPhCVYSoRyOvWzG9QblZkXa5YPzpoZbPfGF0O-5hhjZ7hYPFilSWC-AtM7ivD8EwBUZgTHBJEuR7ap0pW4kygWk9pLeG9wJ8TC5wueWItbSzr6_Mk7nZ3dhaiQmdgxHVtAbVlPKJOJfDJARZ5V4iaxKIPkTqh8.QtL18JGEY_85AgCjOhZb2XSveGMfv7GBSbQvdpfkTWk&dib_tag=se&keywords=touchscreen%2Bfor%2Braspberry%2Bpi%2B3%2C5&qid=1779496656&s=computers&sprefix=touchscreen%2Bfor%2Braspberry%2Bpi%2B3%2B5%2Ccomputers%2C129&sr=1-30&th=1) |
| 128GB Memory Card Micro TF/SD Card Fast Read Storage SD Card | 2 | Independent OS boot storage for all 2 nodes | £14.08| $18.87 |[Aliexpress](https://www.aliexpress.com/item/1005012378583621.html?spm=a2g0o.productlist.main.8.b32enaeFnaeFlH&aem_p4p_detail=202605271014452593618502522400000204003&algo_pvid=51379aee-4f75-4047-80f7-dcc4d8aa2b1e&algo_exp_id=51379aee-4f75-4047-80f7-dcc4d8aa2b1e-7&pdp_ext_f=%7B%22order%22%3A%22-1%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21GBP%217.04%217.04%21%21%2162.39%2162.39%21%40211b6c1917799020852587481edc92%2112000058217101698%21sea%21UK%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3A4c75f75d%3Bm03_new_user%3A-29895&curPageLogUid=bJqLouX4ZPLz&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005012378583621%7C_p_origin_prod%3A&search_p4p_id=202605271014452593618502522400000204003_2) |
|  xruc 1300Mbps WiFi Dongle | 1 | Background network access for data gathering |  £7.99 | $10,71| [Amazon](https://www.amazon.co.uk/1300Mbps-Adapter-Antenna-Wireless-Supports-Black/dp/B0G19NF4NC/ref=sr_1_75?crid=N3N5XMTM6YIV&dib=eyJ2IjoiMSJ9.G6TgHvOxTODxzR_uZ4pYTmBPkkDY1YAEy-kt0BzS5UU7wY1DEDIStFmShOp_Hx1o-YGLsjNl_QHA77r3KaHdFrtipJUMuS0FGPF80v1jJdNGZb2vFK9ny6QYNPOaBlmuI0bMelxT7IMKuUbLIDXgD6g7PNM77YCFtIRIxxJDO4-mnTSUa1UljRtLCfIVOX0d.0BxcVZDHVCkN49L7j2d0tymC0nkibgY6CmxRi0Ab3M4&dib_tag=se&keywords=Sxhlseller+4G+LTE+USB+WiFi+Dongle&qid=1779497051&refinements=p_36%3A-1100&rnid=428432031&sprefix=sxhlseller+4g+lte+usb+wifi+dongle%2Caps%2C164&xpid=cSPfqsQPW4y4m) |
| SUNLU PLA Filament 0.5KG (2-Pack) | 1 | Plastic for 3D printing the custom box | £7.99 | $10.71 |[Amazon](https://www.amazon.co.uk/SUNLU-Filament-Dimensional-Accuracy-Compatible/dp/B0FHKPLJ88/ref=asc_df_B0FHKPLJ88?mcid=e71cb2bcdba63ff9ac8c5ea4c02b7311&tag=googshopuk-21&linkCode=df0&hvadid=755033778404&hvpos=&hvnetw=g&hvrand=4001634302348699234&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9236327&hvtargid=pla-2449517605149&hvocijid=4001634302348699234-B0FHKPLJ88-&hvexpln=0&gad_source=1&th=1) |
|QTshine 10800mAh 25W Power Ban | 1 |Integrated 25W fast charge power supply with LCD screen | £19.54| $26.18 | [Amazon](https://www.amazon.co.uk/Portable-10800mAh-Powerbank-Charging-Essential/dp/B0GRG3K6P1/ref=sr_1_1_sspa?crid=3J0NML0J6WXGE&dib=eyJ2IjoiMSJ9.Kc9YZ8Vxn7QghAQ7G4j36tqNhOC7vIpAD9OLMmopmkqkAgEUdlhodt7bTXDJNcE9WCcJ_9c2f17SitBAc5VD-vrV_2ngl3JB3qF7dnx_bNwl6XceNr7cEr3hYFzDN1lCLEAyTIzmS4ZgNyFY6yEWpSF52nZlPjqf41Qaa_3Qz9rqZtKkwKCiCeP5YDQmCgdRGRrDtA1uKVYyb25dt2ib3MRvxu07vS1L0cPyLSr_LTry37exRo23MuZAB8cNiI-5rZCuqa3ykWRqefLP0NSlQLFTegsblveA2VBVLY-O6fg.0lNCgwVM2ZdU-I2jBRXwlySabVIGcwF_1euLvfOLnPM&dib_tag=se&keywords=6%2Bampere%2Bpower%2Bbank&qid=1779922648&s=electronics&sprefix=6%2Bampere%2Bpower%2Bbank%2Celectronics%2C132&sr=1-1-spons&aref=ZAepRSxsqh&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1)
|kenable Flat CAT6 Ethernet Cable 15cm | 1 |Zero-latency copper wired patch lead for isolated inter-node communication  |£2.87 |$3.85 |[Amazon](https://www.amazon.co.uk/kenable-Ethernet-Profile-Gigabit-Network/dp/B0GZ2J6BYR/ref=sr_1_2?crid=3943JX3V5R8L1&dib=eyJ2IjoiMSJ9.C8-uyzTH0SE6fITf9vCZFl2R0l9JPrdCOnGfoXloq4hFHTh0ib-e9NQdSCLZe-eSzPgAAwgzbkdSZ0ZMdgJF01fOaWiCJts37y3EQYSGUeQrsTErNlfyILjhPe0QGWMwpM2HgAgZ2vsLHkQ-2Hm2O5B93I135xDfQF-vGT6euRSE4eE6kj3SXgsbUuPFcU1YhRzYKviDicWKhF8lMfVIS1WuOPaZmlIklTKDnZM4cGBnT3JCTjSfQIulfwKQocykJ7F_19m-v4vT4LVS2uHiu-YcZCEPX5fjh4Ea_d5kJGA.XKe7Hax4_ZRdGS5_yieMc70wNOXkNdQSJJAIVVpBbO0&dib_tag=se&keywords=Ultra-Short%2BFlat%2BEthernet%2BCable%2B(15cm)&qid=1779982122&s=computers&sprefix=ultra-short%2Bflat%2Bethernet%2Bcable%2B15cm%2B%2Ccomputers%2C155&sr=1-2&th=1)
|SELIACR Vertical 90-Degree USB-C Adapter 3-Pack|1|Low-profile 10Gbps steering adapters to redirect internal power cables beneath the board plates without cord bending|£2.54|$3.40|[Amazon](https://www.amazon.co.uk/SELIACR-Vertical-Direction-Adapters-Compatible/dp/B0B53TS7TM/ref=sr_1_20?crid=3AT5G6Z36X91E&dib=eyJ2IjoiMSJ9.XxlnYXh4JWk6jxaAmD6zeshkf-LPIHWiezJKIlP-zz433uHBGA-WFG0ka6TBA-36-Wg9XE8BoYerSWLZuOABaH1k3AjQ5rJGZ5ANn6RomHqZAwJNKLAp21CpwWDD3OLDQMEZBMjiWaKZlBiKUa4-2ZHEdMHRA7FRiKnekvzPCx1Tyf3NaA_uMzGvz35dskc_UV56pRWHWTl0Il8vGt5KftEcHw-kfVL_pkX4-zookVQBoehpDqfainEQ_sfQMsm3e4zs0SQ7gXBjNvFAdtzp81XtBls07xZHEcKlhIL_haM.7jNRVEKHE6e8ELQ6K2WRjt2n0AaR6JbRCChxuHkcBHw&dib_tag=se&keywords=two%2B90%2Bdegrees%2Badapter%2Busb-c%2B--usb-c&qid=1780009938&refinements=p_36%3A-500&rnid=389035011&s=electronics&sprefix=two%2B90%2Bdegrees%2Badapter%2Busb-c%2B--usb-c%2Celectronics%2C154&sr=1-20&th=1)
| **TOTAL** | | |**£224.95** | **$301.43**| |
