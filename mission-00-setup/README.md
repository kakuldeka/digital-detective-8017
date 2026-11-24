# Mission 0 — Create your GitHub workspace

## 1. Task / objective
The objective of Mission 0 is to set up a clean, correctly named GitHub workspace and establish the project directory structure for all nine missions (0 through 8). This includes verifying system tools (Python 3 and Git), structuring folders and documentation according to assignment guidelines, preparing the root README, and linking the local workspace to the public GitHub repository.

## 2. Work completed
- Decided and confirmed repository name: `digital-detective-8017` (matching assignment name + last 4 digits of USN).
- Initialized local repository inside `/Users/kakul/Desktop/digital-detective-8017` on branch `main`.
- Connected the remote GitHub repository at `https://github.com/kakuldeka/digital-detective-8017.git`.
- Checked and verified local installations and versions of Python 3 (`Python 3.14.7`) and Git (`git version 2.54.0`).
- Generated all required mission folders (`mission-00-setup` through `mission-08-final-report`), the `evidence/` directory, and initial file placeholders.
- Drafted the root `README.md` with student metadata, mission navigation links, and project goals.
- Authored this `README.md` following the standardized 8-section reporting structure.

## 3. Commands / tools used
- `python3 --version`: Verified the installed Python runtime version (`Python 3.14.7`).
- `git --version`: Verified the installed Git version (`git version 2.54.0`).
- `git init -b main`: Initialized a clean, local Git repository with `main` as the default branch.
- `git remote add origin https://github.com/kakuldeka/digital-detective-8017.git`: Linked local directory to the remote GitHub repository.
- `mkdir -p`: Created directories for each mission and the evidence folder.
- `touch`: Created placeholder Markdown files and python script files.

## 4. My understanding
- **What is a Git Repository?**  
  A repository (or repo) is a managed digital workspace tracked by Git. It records changes made to files over time, keeping a complete history of snapshots (commits). This allows developers to roll back errors, inspect historical states, and collaborate seamlessly across different machines.
- **Why organize folders by mission?**  
  Structuring the project into dedicated folders (`mission-00-setup`, `mission-01-computer-basics`, etc.) provides separation of concerns. Each topic can be developed, tested, documented, and reviewed in isolation without cluttering the project root or mixing up files. It also maps directly to the assignment's modular evaluation criteria.

## 5. Difficulties faced
- The parent user directory (`/Users/kakul`) had an existing repository initialization, which initially caused Git commands inside subfolders to report parent untracked files instead of an isolated workspace.
- Needed to ensure the local folder `/Users/kakul/Desktop/digital-detective-8017` had its own independent `.git` repository tracking only assignment files.

## 6. How I resolved them
- Explicitly ran `git init -b main` within `/Users/kakul/Desktop/digital-detective-8017` to establish a dedicated Git root boundary for this assignment.
- Verified with `git status` and `git remote -v` that only files inside `digital-detective-8017` are tracked and associated with the `digital-detective-8017` remote.

## 7. Evidence / files
- [README.md](file:///Users/kakul/Desktop/digital-detective-8017/README.md)
- [mission-00-setup/README.md](file:///Users/kakul/Desktop/digital-detective-8017/mission-00-setup/README.md)
- Directory layout:
  - `mission-00-setup/`
  - `mission-01-computer-basics/`
  - `mission-02-terminal/`
  - `mission-03-operating-system/`
  - `mission-04-programs/`
  - `mission-05-numbers-data/`
  - `mission-06-git-github/`
  - `mission-07-networking/`
  - `mission-08-final-report/`
  - `evidence/`

## 8. Commit details
- **Commit message:** `Set up Digital Detective mission structure`
- **Target branch:** `main`
- **Remote status:** Pushed and verified on GitHub at `https://github.com/kakuldeka/digital-detective-8017`
