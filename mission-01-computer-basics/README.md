# Mission 1 — Know your computer

## 1. Task / objective
The objective of Mission 1 is to examine foundational computer architecture concepts, specifically the Input-Processing-Output-Storage (IPOS) model, distinguish between system, application, and utility software alongside physical hardware components, and identify embedded computer systems operating in daily life outside standard personal computing devices.

---

## 2. Work completed
- Analyzed and traced a concrete daily computing activity (typing, reviewing, and saving a code report) across each stage of the IPOS cycle, identifying the physical components responsible.
- Classified hardware components and software utilities into distinct functional categories (Operating System, Application Software, and Utility Software).
- Identified and analyzed three ubiquitous embedded/specialized computing systems (Automated Teller Machine, Smart City Traffic Controller, and Metro Automatic Fare Collection Gate).
- Documented findings in structured tables adhering to all assignment requirements.

---

## 3. Commands / tools used
- Text Editor / Markdown formatting tools for structured documentation.
- Terminal observation tools (`system_profiler` and OS info utilities) to cross-reference system specifications and hardware device buses.

---

## 4. My understanding

### Task 1.1 — Trace one activity using IPOS
**Chosen Activity:** Writing, editing, and saving a Python script (`analysis.py`) inside an integrated development environment.

| Stage | What happens in your example? | Possible hardware / component |
| :--- | :--- | :--- |
| **Input** | Keystrokes representing characters and keyboard shortcuts (`Cmd+S`) are detected by the keyboard controller and sent as hardware interrupts to the OS. | Mechanical/membrane keyboard, trackpad/mouse |
| **Processing** | The CPU fetches keyboard interrupt signals, processes character encodings in cache and RAM, coordinates syntax highlighting, and executes the file save routine. | Multi-core Central Processing Unit (CPU) and System RAM |
| **Output** | The display controller renders the updated code buffer and file status indicators onto the screen pixels at high refresh rates. | Liquid Retina Display / external monitor and GPU |
| **Storage** | The file buffer residing in volatile RAM is serialized into byte streams and written persistently onto non-volatile flash memory cells. | Solid State Drive (NVMe SSD storage controller) |

#### Narrative Explanation of Flow
1. **From Input to Processing:** When a key is struck, electrical contact triggers a scan code. The keyboard microcontroller sends this signal across the USB or SPI bus to the CPU. The operating system kernel receives the interrupt request (IRQ), maps the keycode to a Unicode character, and pushes it into the active editor application's buffer held in RAM.
2. **From Processing to Output:** The editor updates its internal text tree. The CPU and GPU compute font rasterization and send display framebuffers to the display controller, rendering visible letters on screen almost instantaneously.
3. **From Processing to Storage:** When the save command (`Cmd+S`) is executed, the editor issues a system call (`write`) to the file system. The operating system kernel schedules disk I/O, writing the data blocks to the NVMe SSD controller, making the code persistent even if the power is cut.

---

### Task 1.2 — Identify hardware and software
The table below details physical hardware devices and representative software categories used during software development:

| Item / software name | Hardware or software? | Software type (if applicable) | Purpose |
| :--- | :--- | :--- | :--- |
| **NVMe Solid State Drive (SSD)** | Hardware | *Not applicable* | Provides high-speed non-volatile secondary storage for the operating system, applications, and user repositories. |
| **Random Access Memory (RAM)** | Hardware | *Not applicable* | High-speed volatile primary memory holding active instructions and working data needed immediately by the CPU. |
| **Apple M-Series CPU Cores** | Hardware | *Not applicable* | Executes machine code instructions, performs arithmetic and logic operations, and controls data transfers. |
| **Retina Built-in Display** | Hardware | *Not applicable* | Primary visual output device presenting graphical and text interfaces to the user. |
| **macOS (Darwin Kernel)** | Software | Operating System | Manages hardware abstractions, CPU process scheduling, virtual memory, device drivers, and security isolation. |
| **Visual Studio Code** | Software | Application Software | Extensible code editor providing text manipulation, syntax parsing, and workspace navigation for developers. |
| **Terminal (zsh shell)** | Software | Application / System Shell | Command-line interpreter allowing users to interact directly with the operating system kernel via text commands. |
| **Time Machine / Disk Utility** | Software | Utility Software | System maintenance tools for managing disk partitions, repairing file system tables, and creating automated snapshots. |

---

### Task 1.3 — Computer systems around you
Everyday computing systems embedded in dedicated physical infrastructure:

| System | Main purpose | One input | One output |
| :--- | :--- | :--- | :--- |
| **Automated Teller Machine (ATM)** | Dispenses authenticated bank funds and provides account transaction balances securely. | EMV chip card reader and numeric PIN keypad. | Physical cash dispensing shutter mechanism and thermal receipt printer. |
| **Smart Adaptive Traffic Light** | Regulates vehicle flow and pedestrian crossing dynamically to prevent traffic gridlock. | In-road inductive electromagnetic loop sensors and roadside pedestrian push-buttons. | High-intensity LED signal lamps (Green / Yellow / Red) and pedestrian crossing countdown displays. |
| **Metro Automatic Fare Collection (AFC) Gate** | Validates passenger travel transit cards and controls physical platform gate turnstiles. | RFID / NFC contactless smart card scanner. | Pneumatic/motorized turnstile barrier release and acoustic confirmation beeper. |

---

## 5. Difficulties faced
- Distinguishing clearly between system software (operating systems) and utility software (maintenance tools like disk checkers or compression utilities) since utility software often ships bundled with modern operating systems.
- Mapping intangible software commands (like clicking save) to the exact hardware transitions between volatile RAM and solid-state flash blocks.

## 6. How I resolved them
- Reviewed the functional definitions of OS (core supervisor managing hardware resources) versus utilities (specialized tasks that analyze, configure, optimize, or maintain a computer).
- Traced the low-level operating system I/O stack: User Space Application -> System Call Interface (`sys_write`) -> Virtual File System (VFS) -> Block Device Driver -> NVMe Hardware Controller -> Flash Memory NAND cells.

---

## 7. Evidence / files
- [README.md](file:///Users/kakul/Desktop/digital-detective-8017/mission-01-computer-basics/README.md)
- Root index linkage: [Root README.md](file:///Users/kakul/Desktop/digital-detective-8017/README.md)

---

## 8. Commit details
- **Commit message:** `Complete computer basics and IPOS mission`
- **Target branch:** `main`
- **Remote status:** Pushed and verified on GitHub
