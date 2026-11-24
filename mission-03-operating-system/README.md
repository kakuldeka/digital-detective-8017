# Mission 3 — Understand the operating system

## 1. Task / objective
The objective of Mission 3 is to inspect the host operating system environment, explore active processes and identify Process IDs (PIDs), analyze filesystem storage utilization, understand absolute versus relative paths, dissect UNIX file permission masks, and articulate the six core responsibilities of modern operating systems.

---

## 2. Work completed
- Inspected operating system release, kernel architecture, current user identity, and storage allocation using terminal diagnostic commands.
- Captured and analyzed a snapshot of running background and foreground processes, inspecting the Process Identifier (PID), CPU usage, and memory consumption.
- Compared absolute filesystem paths with relative navigation paths using files in the assignment directory.
- Analyzed the owner, group, and world read/write/execute permission bits of files inside `terminal-practice/`.
- Explained the six primary roles of an operating system (Process, Memory, Device, File Management, User Interface/Shell, Security/Permissions) with concrete examples.

---

## 3. Commands / tools used
- `sw_vers`: Reports macOS product name, version, and build version.
- `uname -srm`: Reports the Darwin operating system kernel name, release version, and machine hardware architecture (`arm64`).
- `whoami`: Displays the currently logged-in user account name (redacted for privacy).
- `df -h /`: Displays disk space statistics for the root filesystem in human-readable gigabytes.
- `ps -eo pid,comm,%cpu,%mem`: Displays a snapshot of active processes, their PIDs, command names, and resource percentages.
- `ls -l <file>`: Displays permissions, link count, owner, and group metadata.

---

## 4. My understanding

### Task 3.1 — Explore your operating system

| Information explored | What it tells you | Your observation (privacy-safe) |
| :--- | :--- | :--- |
| **Operating system / system details** | Identifies the specific OS distribution, kernel release version, and processor architecture. | macOS version 27.2.1, running Darwin kernel version 27.2.0 on 64-bit ARM architecture (`arm64`). |
| **Current account identity** | Confirms the username and session privileges under which commands are executed. | Active local user account: `[redacted]` (standard user privileges, member of `staff` group). |
| **Available and used storage** | Shows total filesystem capacity, consumed disk blocks, and remaining storage on the boot drive. | APFS Boot Volume (`/dev/disk3s1s1`): Total size `926 GiB`, Used `13 GiB`, Available `554 GiB` (free capacity available for applications and data). |
| **System activity snapshot** | Summarizes real-time CPU and memory allocation across active system processes. | PID 1 (`/sbin/launchd`) initializes system daemons; system services such as `logd` consume minimal CPU (<1%) and memory (<0.5%). |

---

### Task 3.2 — Understand processes

#### Conceptual Questions & Answers
1. **What is a process?**  
   A process is an active, executing instance of a computer program. When a program file stored on disk is launched, the operating system loads its instructions and data into RAM, assigns it dedicated virtual address space, sets up execution threads, and allocates system resources (file handles, network sockets).
2. **What does the PID column represent?**  
   **PID** stands for **Process Identifier**. It is a unique, non-negative integer assigned by the operating system kernel to each running process upon creation. The OS kernel uses the PID to track process state, schedule CPU execution slices, manage child-parent process hierarchies, and route signals (such as `SIGTERM` or `SIGKILL`).
3. **Two examples of processes running on this computer:**  
   - `/sbin/launchd` (PID 1): The parent daemon of all processes on macOS; boots user sessions, launches services, and manages system daemons.
   - `/usr/libexec/logd` (PID 533): The Apple Unified Logging daemon responsible for handling diagnostic log messages and telemetry across the OS.

---

### Task 3.3 — Understand paths and permissions

#### Absolute vs. Relative Paths
- **Absolute Path:** Specifies the complete, unambiguous location of a file or directory starting from the root directory (`/`). It is independent of the shell's current working directory.
  - *Example from workspace:* `/Users/[redacted]/Desktop/digital-detective-8017/terminal-practice/practice_note.txt`
- **Relative Path:** Specifies the location of a file or directory relative to the current working directory (`pwd`). It depends directly on where the user is currently situated in the filesystem.
  - *Example from workspace root:* `terminal-practice/practice_note.txt` (or `./terminal-practice/practice_note.txt`).
  - *Example from inside `terminal-practice/`:* `../mission-00-setup/README.md`.

#### File Permissions Analysis
Inspecting `terminal-practice/practice_note.txt` via `ls -l`:
`-rw-r--r--@ 1 [redacted] staff 82 Nov 24 20:16 terminal-practice/practice_note.txt`

- The first character `-` indicates it is a regular file (not a directory `d` or symbolic link `l`).
- **Owner permissions (`rw-`):** Read (`r`) and Write (`w`) are enabled; Execute (`x`) is not enabled. The owner can inspect and edit the file, but cannot run it as a program.
- **Group permissions (`r--`):** Read-only. Members of the `staff` group can read the file.
- **Others permissions (`r--`):** Read-only. Any other user on the system can read the file.

| Permission | Meaning | Example |
| :--- | :--- | :--- |
| **r — Read** | Grants permission to open, view, or read the byte contents of a file; on a directory, permits listing the contents. | Opening a `.txt` file with `cat` or a text editor. |
| **w — Write** | Grants permission to modify, append to, truncate, or overwrite file data; on a directory, permits creating or deleting files within it. | Saving edits to `practice_note.txt`. |
| **x — Execute** | Grants permission to execute a binary program or script; on a directory, permits traversal (`cd`) into that folder. | Running a compiled executable or entering a folder. |

---

### Task 3.4 — Explain operating-system responsibilities

| OS responsibility | Your explanation | Example |
| :--- | :--- | :--- |
| **Process management** | Controls process lifecycle: creation, CPU time-slice scheduling, inter-process communication (IPC), and termination. | Switching execution between an active code editor and a background web browser seamlessly via preemptive multitasking. |
| **Memory management** | Allocates and tracks physical RAM and virtual memory addresses across processes, preventing programs from corrupting each other's memory. | Paging idle background memory pages to swap space on the SSD when physical RAM is under heavy demand. |
| **Device management** | Abstraction of physical peripherals through device drivers, translating generic OS read/write requests into device-specific hardware protocols. | Sending printer commands over USB or Wi-Fi without the word processor needing to know the printer's internal hardware architecture. |
| **File management** | Organizes data blocks on persistent storage into hierarchical files and directories, maintaining indexing tables and access permissions. | The Apple File System (APFS) allocating blocks, managing inode metadata, and reading files from an NVMe SSD. |
| **User interface / shell** | Provides a human-to-computer interface, either graphical (GUI) or text-based (CLI), allowing users to issue instructions to the system. | The macOS graphical Aqua desktop environment and the command-line Z-shell (`zsh`). |
| **Security and permissions** | Enforces access control matrices, authentication, process sandboxing, and resource authorization to safeguard system integrity. | Preventing non-administrator user accounts from overwriting critical kernel binaries located in `/System` or `/sbin`. |

---

## 5. Difficulties faced
- Filtering process listings without exposing private background personal apps or sensitive window titles in terminal evidence.
- Interpreting macOS specific APFS snapshot mount layouts (`/dev/disk3s1s1`) compared to traditional single-partition Linux disk paths.

## 6. How I resolved them
- Used formatted `ps -eo pid,comm,%cpu,%mem` targeting system-level daemons (`launchd`, `logd`) and applied `[redacted]` placeholders for personal username and hostname details.
- Consulted APFS documentation regarding how macOS separates the sealed read-only System volume from the Data volume.

---

## 7. Evidence / files
- [README.md](file:///Users/kakul/Desktop/digital-detective-8017/mission-03-operating-system/README.md)
- Inspected practice file: [terminal-practice/practice_note.txt](file:///Users/kakul/Desktop/digital-detective-8017/terminal-practice/practice_note.txt)

---

## 8. Commit details
- **Commit message:** `Document operating system and file management`
- **Target branch:** `main`
- **Remote status:** Pushed and verified on GitHub
