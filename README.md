# The Digital Detective: Explore Your Computer

## Diwali Independent Learning Assignment
**Student Name:** Kakul Deka  
**USN (Last 4 Digits):** 8017  
**GitHub Repository:** [digital-detective-8017](https://github.com/kakuldeka/digital-detective-8017)  
**Repository URL:** https://github.com/kakuldeka/digital-detective-8017  

---

## 🔍 Assignment Overview
**The Digital Detective** is an independent practical computer science assignment designed to explore the inner workings of modern computer systems. Through nine ordered, self-contained missions (Mission 0 through Mission 8), this project investigates:
- How computers capture input, process data, render output, and persist information (the IPOS model).
- Navigating and manipulating the file system using the Command-Line Interface (CLI).
- How the operating system coordinates processes, schedules CPU time, manages memory, and enforces security permissions.
- How programs execute, comparing compiled machine code against interpreted runtime environments.
- Low-level mathematical representations of data in Binary, Decimal, and Hexadecimal, alongside character encoding standards (ASCII vs. UTF-8).
- Modern collaborative version control workflows using Git and GitHub (commits, branches, pull requests, and merges).
- Computer networking architecture, protocol stacks, packet switching, DNS resolution, and the complete web request lifecycle.

> [!NOTE]
> In compliance with assignment rules, all personal and sensitive details (e.g. domestic IP addresses, Wi-Fi network names, hardware serial numbers, and account usernames) have been securely redacted using `[redacted]`.

---

## 📂 Repository Structure & Mission Index

Each mission has been developed, verified, documented in its own dedicated folder, and committed independently:

| Mission | Folder / Link | Focus Area | Status |
| :--- | :--- | :--- | :--- |
| **Mission 0** | [mission-00-setup/](file:///Users/kakul/Desktop/digital-detective-8017/mission-00-setup/README.md) | Repository and workspace setup, folder hierarchy, tool verification | ✅ Completed |
| **Mission 1** | [mission-01-computer-basics/](file:///Users/kakul/Desktop/digital-detective-8017/mission-01-computer-basics/README.md) | Computer fundamentals, IPOS cycle, hardware/software taxonomy | ✅ Completed |
| **Mission 2** | [mission-02-terminal/](file:///Users/kakul/Desktop/digital-detective-8017/mission-02-terminal/README.md) | Command-line operations, safe file modification, flags, pipes, package managers | ✅ Completed |
| **Mission 3** | [mission-03-operating-system/](file:///Users/kakul/Desktop/digital-detective-8017/mission-03-operating-system/README.md) | Operating system roles, running processes (PIDs), storage, paths, permissions | ✅ Completed |
| **Mission 4** | [mission-04-programs/](file:///Users/kakul/Desktop/digital-detective-8017/mission-04-programs/README.md) | How programs run, `hello.py`, compilers vs interpreters | ✅ Completed |
| **Mission 5** | [mission-05-numbers-data/](file:///Users/kakul/Desktop/digital-detective-8017/mission-05-numbers-data/README.md) | Number conversions (Bin/Dec/Hex), `number_converter.py`, text encoding | ✅ Completed |
| **Mission 6** | [mission-06-git-github/](file:///Users/kakul/Desktop/digital-detective-8017/mission-06-git-github/README.md) | Git workflow, feature branch `update-about`, Pull Requests, command glossary | ✅ Completed |
| **Mission 7** | [mission-07-networking/](file:///Users/kakul/Desktop/digital-detective-8017/mission-07-networking/README.md) | Computer networking (LAN/MAN/WAN), DNS, ping, website access sequence | ✅ Completed |
| **Mission 8** | [mission-08-final-report/](file:///Users/kakul/Desktop/digital-detective-8017/mission-08-final-report/README.md) | Final verification, audit checklist, submission documentation | ✅ Completed |

---

## 🛠️ How to Run the Number Converter

The Python Number Converter developed in Mission 5 accepts any positive decimal integer and outputs its binary and hexadecimal equivalents.

### Prerequisites
- Python 3.8 or higher installed (`python3 --version`).

### Instructions
1. Open your terminal and navigate to the Mission 5 folder:
   ```bash
   cd mission-05-numbers-data
   ```
2. Execute the script using Python 3:
   ```bash
   python3 number_converter.py
   ```
3. Enter a positive decimal integer when prompted (for example, `42`, `255`, or `1024`):
   ```
   ====================================
    Digital Detective Number Converter 
   ====================================
   Enter a positive decimal integer: 255

   --- Conversion Results ---
   Decimal Value:     255
   Binary (bin()):    0b11111111 (raw bits: 11111111)
   Hexadecimal (hex): 0xff (uppercase: FF)
   --------------------------
   ```

---

## 💡 Summary of Learning
Throughout this assignment, several foundational computing pillars were explored and practically applied:
1. **Low-Level to High-Level Hardware Abstraction:** Understood how hardware input signals trigger processor interrupts, interact with volatile memory (RAM), and transition to persistent secondary storage (SSD) through the operating system kernel.
2. **Command-Line Interface Fluency:** Learned to interact with the system via terminal commands, utilizing flags to modify command behavior, and using UNIX pipes (`|`) to compose modular commands into streaming workflows.
3. **Systems & Runtime Mechanics:** Contrasted native machine compilation (C/C++, Rust) with bytecode interpretation (Python), observing how the OS schedules processes via unique Process IDs (PIDs) and isolates memory spaces.
4. **Data Representation:** Demystified how arbitrary information—numbers, instructions, and human text—is represented as voltage-based bitstrings, exploring base-2, base-10, base-16 conversions, and UTF-8 encoding standards.
5. **Collaborative Version Control:** Applied professional Git branching workflows, tracking changes across local commits, opening and integrating feature branches via Pull Requests, and synchronizing with remote cloud repositories on GitHub.
6. **Network Protocols & The Web:** Traced how data packets travel across routers using packet switching, how DNS translates human domain names into IP addresses, and how the multi-layer protocol stack (TCP, TLS, HTTPS) delivers web applications.

---

## 📜 Commit & Verification Discipline
In strict adherence to assignment guidelines:
- Every mission was implemented, documented, committed, and pushed separately in exact sequence.
- All mission folders contain a dedicated, uniform 8-section `README.md`.
- No personal identifying information (passwords, tokens, private network IPs) has been published.
