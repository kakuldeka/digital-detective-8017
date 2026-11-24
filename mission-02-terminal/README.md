# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
The objective of Mission 2 is to gain proficiency with the Command-Line Interface (CLI), master essential navigation and file management commands, safely perform file creation, modification, duplication, and renaming, understand command-line flags and UNIX data pipelines, and evaluate package manager tools.

---

## 2. Work completed
- Practiced core directory navigation and inspection commands (`pwd`, `ls`, `ls -l`, `cd`).
- Created a safe, isolated practice sandbox directory (`terminal-practice/`) inside the repository.
- Practiced non-destructive file modification (comparing overwrite `>` with append `>>`).
- Executed file duplication (`cp`) and renaming (`mv`) operations safely inside the sandbox.
- Tested compound flags (`-lah`) and compared output details with basic directory listings.
- Constructed a pipeline using the pipe operator (`|`) to stream `ls -la` into `head -n 5`.
- Verified macOS package manager Homebrew (`Homebrew 7.0.13`) and inspected managed packages safely without altering system configurations.
- Documented all observations, command tables, and conceptual answers.

---

## 3. Commands / tools used
- `pwd`: Prints the current working directory's absolute path.
- `ls`: Lists files and directories in the current folder.
- `ls -l` / `ls -lah`: Lists items in long format showing permissions, ownership, byte size (or human-readable units), timestamps, and hidden entries.
- `cd ..` / `cd <folder>`: Navigates up to the parent directory or down into a subfolder.
- `mkdir terminal-practice`: Creates a designated practice folder.
- `touch <file>` / `echo ... > <file>`: Creates empty files or writes text into files.
- `echo ... >> <file>`: Appends lines of text without erasing preexisting contents.
- `cat <file>`: Displays file contents directly to standard output.
- `cp <source> <dest>`: Duplicates a file while preserving the original.
- `mv <old> <new>`: Renames a file or relocates it to a new path.
- `|` (UNIX pipe): Passes stdout from the left command into stdin of the right command.
- `head -n <k>`: Filters and outputs only the first $k$ lines of incoming text.
- `brew --version` & `brew list`: Queries the Homebrew package manager.

---

## 4. My understanding

### Task 2.1 — Explore basic Terminal operations

| Operation / command name | What it does | What I observed |
| :--- | :--- | :--- |
| **Current-directory display (`pwd`)** | Prints the full absolute path of the directory currently active in the shell. | Output displayed `/Users/[redacted]/Desktop/digital-detective-8017`, confirming exact location in the filesystem tree. |
| **Directory listing (`ls`)** | Lists names of visible files and folders in the current directory. | Displayed mission folders (`mission-00-setup`, `mission-01-computer-basics`, etc.) and `README.md`. |
| **Detailed listing (`ls -l`)** | Displays items in columnar format with permissions, link count, owner, group, file size in bytes, modification date, and filename. | Listed each entry with details like `-rw-r--r--` and owner name, giving full metadata visibility. |
| **Change directory (`cd ..` and `cd -`)** | Moves shell context up to parent folder (`..`) or navigates to specified subfolders. | Prompt and `pwd` updated dynamically; moving to `..` changed working location to the Desktop folder. |
| **Create directory (`mkdir terminal-practice`)** | Creates a new directory at the specified path if it doesn't already exist. | Created folder `terminal-practice/` without error; verified its presence in subsequent `ls`. |
| **Create empty file (`touch practice_note.txt`)** | Creates a 0-byte file or updates timestamps of an existing file. | A file named `practice_note.txt` appeared with size 0 bytes. |
| **Copy file (`cp practice_note.txt backup_note.txt`)** | Duplicates the source file into a new file, leaving the source intact. | Two separate files existed with identical content and independent inodes. |
| **Move / rename file (`mv backup_note.txt archived_note.txt`)** | Renames the file or moves it to a different directory path without duplicating data. | `backup_note.txt` was renamed to `archived_note.txt`; the old name ceased to exist. |
| **Display file contents (`cat practice_note.txt`)** | Reads file sequentially and outputs its entire text contents to the terminal. | Printed the stored text lines directly to the terminal output stream. |

---

### Task 2.2 — Practise file changes safely (terminal-practice)

#### Conceptual Questions & Answers
1. **What is the difference between replacing a file's contents and adding text to the end?**  
   - **Replacing (`>` redirection):** The single greater-than operator truncates (erases) the existing contents of the target file before writing new data. If the file previously contained 100 lines, they are wiped out and replaced solely with the newly provided line.
   - **Adding to the end (`>>` redirection):** The double greater-than operator opens the file in append mode. It leaves all existing lines untouched and writes the new text strictly after the final existing character.
2. **What is the difference between copying a file and moving a file?**  
   - **Copying (`cp`):** Allocates new storage blocks on the disk and creates an entirely separate duplicate file. Changes made to the copy do not affect the original.
   - **Moving (`mv`):** Within the same filesystem, moving simply updates the directory pointer / filename (metadata entry) pointing to the existing disk blocks. The original filename is removed. No new duplicate data is created.
3. **What information does the current-directory display (`pwd`) provide?**  
   - It provides the absolute path starting from the root directory (`/`), indicating the exact contextual hierarchy where any relative file paths will be resolved.
4. **Why is a directory-listing operation useful?**  
   - It confirms file creation, validates exact spelling and file extensions, verifies file permissions and sizes, and prevents accidental overwrites before running destructive operations.

---

### Task 2.3 — Understand flags and pipes

#### Flags Comparison
- **Normal listing (`ls`):** Only prints filenames in horizontal or simple column layout, hiding hidden files (files beginning with `.`) and omitting permissions, owner, and sizes.
- **Detailed + Hidden + Human-readable listing (`ls -lah`):**
  - `-l`: Formats output as a detailed table with file permissions, link counts, owner, group, size, and modification timestamp.
  - `-a`: Displays **all** files, including hidden dotfiles like `.git`, `.DS_Store`, `.`, and `..`.
  - `-h`: Formats file byte sizes into human-readable units (e.g., `82B`, `4.0K`, `12M`) instead of raw byte counts.

#### UNIX Pipes (`|`)
- **Command Tested:** `ls -la | head -n 5`
- **How it works:**
  - The pipe operator (`|`) connects the Standard Output (`stdout`) of the command on its left (`ls -la`) directly to the Standard Input (`stdin`) of the command on its right (`head -n 5`).
  - **Left side (`ls -la`):** Generates a comprehensive multi-line listing of all files and metadata.
  - **Right side (`head -n 5`):** Receives the stream and filters it, outputting only the first 5 lines (the total summary and the first few directory entries) and discarding the rest.
  - This illustrates the core UNIX philosophy: small, modular tools composed together to perform complex filtering.

---

### Task 2.4 — Understand package managers
- **Observed Version:** Homebrew 7.0.13
- **Observed Managed Packages:** Tools such as `ca-certificates`, `coreutils`, `cowsay`, `ffmpeg`, etc.
- **Why Package Managers are Useful:**  
  A package manager automates the discovery, download, compilation, installation, dependency resolution, updating, and uninstallation of software packages from centralized repositories. Instead of manually downloading binary archives, tracking down shared library dependencies, and placing binaries into system `$PATH` directories, developers can install and maintain command-line tools and libraries using a single standardized command (e.g., `brew install`). It ensures consistency, security updates, and clean removals without leaving orphaned files.

---

## 5. Difficulties faced
- Accidentally running `>` instead of `>>` could erase notes during append testing.
- Remembering to stay strictly within the `terminal-practice` sandbox to ensure no root project files or Git metadata were modified.

## 6. How I resolved them
- Carefully verified shell redirection operators prior to execution (`>>` for append, `>` for initial write).
- Executed `pwd` and `ls` within `terminal-practice/` before every file command to guarantee containment.

---

## 7. Evidence / files
- Sandbox folder: [terminal-practice/](file:///Users/kakul/Desktop/digital-detective-8017/terminal-practice/)
- Practice notes: [terminal-practice/practice_note.txt](file:///Users/kakul/Desktop/digital-detective-8017/terminal-practice/practice_note.txt)
- Archived backup: [terminal-practice/archived_note.txt](file:///Users/kakul/Desktop/digital-detective-8017/terminal-practice/archived_note.txt)
- Mission documentation: [README.md](file:///Users/kakul/Desktop/digital-detective-8017/mission-02-terminal/README.md)

---

## 8. Commit details
- **Commit message:** `Complete Terminal and file management mission`
- **Target branch:** `main`
- **Remote status:** Pushed and verified on GitHub
