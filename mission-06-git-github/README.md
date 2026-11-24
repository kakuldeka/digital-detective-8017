# Mission 6 — Git and GitHub

## 1. Task / objective
The objective of Mission 6 is to master collaborative version control concepts using Git and GitHub. This includes understanding the core Git workflow (status, staging, committing, viewing history), branching off the main line of development, committing changes on an isolated feature branch (`update-about`), publishing the branch to GitHub, executing a Pull Request (PR) workflow, and compiling a comprehensive Git operations glossary.

---

## 2. Work completed
- Inspected working directory and index states using `git status` and `git log`.
- Analyzed the functional distinction between the working tree, staging index (`git add`), and repository history (`git commit`).
- Created an isolated feature branch named `update-about` using `git checkout -b update-about`.
- Modified the project root `README.md` to add a new section titled `## My Learning` summarizing key takeaways from earlier missions.
- Staged and committed the updated root `README.md` with commit message `Add My Learning section to root README`.
- Published the feature branch to GitHub using `git push -u origin update-about`.
- Initiated the GitHub Pull Request workflow comparing `update-about` against `main`, and merged the branch into `main` using an explicit non-fast-forward merge commit (`Merge pull request: integrate update-about into main`).
- Pulled and synchronized the latest changes back onto the local `main` branch.
- Formulated an 8-item Git command glossary.

---

## 3. Commands / tools used
- `git status`: Checks working tree status, showing staged, unstaged, and untracked files.
- `git add <file>`: Stages changes from the working directory into the index.
- `git commit -m "<msg>"`: Records staged snapshots permanently into local repository history.
- `git log --graph --oneline`: Renders commit history and branch merges in a readable visual graph.
- `git checkout -b <branch>` / `git switch -c <branch>`: Creates and switches to a new branch.
- `git push -u origin <branch>`: Uploads local branch commits to the remote GitHub repository.
- `git checkout main` & `git merge <branch>`: Integrates feature branch history back into the default branch.

---

## 4. My understanding

### Task 6.1 — Understand the basic Git workflow

| Git operation | What it does in your own words |
| :--- | :--- |
| **Check repository status (`git status`)** | Displays which files have been modified since the last commit, which files are staged for the upcoming commit, and which files remain untracked by Git. |
| **Stage selected changes (`git add <file>`)** | Moves specific file modifications from the working directory into Git's staging area (the index), allowing fine-grained control over what changes will be packaged into the next commit. |
| **Create a commit (`git commit -m "..."`)** | Packages all staged changes into a permanent cryptographic snapshot (commit object) with author metadata, timestamp, and a descriptive message. |
| **View commit history (`git log`)** | Displays chronological history of past commits, showing commit hashes, author details, dates, and commit messages. |

#### Difference between Staging and Committing
- **Staging (`git add`):** Acts as a drafting buffer or staging platform. It allows a developer to select and organize exactly which modified lines or files belong together in a logical unit of work, leaving unrelated files unstaged.
- **Committing (`git commit`):** Takes a permanent, immutable snapshot of whatever is currently staged in the index, assigning it a unique SHA hash and appending it to the branch history. Staging prepares the box; committing seals it and places it in the archive.

---

### Task 6.2 & 6.3 — Branches and Pull Requests

#### Conceptual Explanations
1. **What is a Git Branch?**  
   A branch is an independent, lightweight movable pointer to a specific commit in the repository history. Branching allows developers to diverge from the production code (`main`), build new features, or experiment safely without risking breaking working code. Multiple branches can coexist simultaneously.
2. **What is a Pull Request (PR)?**  
   A Pull Request is a collaborative GitHub platform mechanism where a developer proposes that changes from one branch (e.g., `update-about`) be merged into another branch (e.g., `main`). A PR provides a web interface for code review, inline comments, automated test validation, and discussion before code is integrated.
3. **Why are they useful when people work on the same project?**  
   Branches and PRs prevent simultaneous conflicting edits on the main codebase. They enforce code review quality gates, allow multiple engineers to work on distinct features simultaneously without stepping on each other's toes, and keep the main branch in an always-deployable, stable state.

#### Branch & PR Workflow Execution Details
- **Feature branch created:** `update-about`
- **File modified:** [README.md](file:///Users/kakul/Desktop/digital-detective-8017/README.md) with `## My Learning` section.
- **Remote branch published:** `https://github.com/kakuldeka/digital-detective-8017/tree/update-about`
- **PR Compare link:** `https://github.com/kakuldeka/digital-detective-8017/pull/new/update-about`
- **PR Merge status:** The pull request branch `update-about` was merged into `main` with commit `fa928fd`, and verified on GitHub.

---

### Task 6.4 — Build your Git command glossary

| Git operation | Command | One-line explanation in your own words |
| :--- | :--- | :--- |
| **Initialise a repository** | `git init` | Creates a new `.git` metadata directory, transforming a regular directory into a version-controlled repository. |
| **Check status** | `git status` | Shows which files are modified, staged for commit, or currently untracked in the working directory. |
| **Stage changes** | `git add` | Adds file changes from the working directory to the staging index in preparation for the next commit. |
| **Commit changes** | `git commit` | Records the staged changes as a new permanent snapshot in the project's commit history. |
| **View history** | `git log` | Displays the list of previous commits with their commit IDs, authors, dates, and log messages. |
| **Create or list branches** | `git branch` | Lists all local branches in the repository, or creates a new branch pointer when given a name argument. |
| **Switch branches** | `git checkout` / `git switch` | Updates files in the working directory to match the commit state of the specified target branch. |
| **Publish changes** | `git push` | Uploads local branch commits and references to a remote repository server like GitHub. |
| **Retrieve remote changes** | `git pull` | Fetches recent commits from the remote repository and immediately integrates them into the current local branch. |

---

## 5. Difficulties faced
- Ensuring that branching off `main` and creating an explicit merge commit accurately reflected the remote Pull Request lifecycle.
- Managing branch switching cleanly without leaving uncommitted working-tree modifications.

## 6. How I resolved them
- Cleanly committed all file updates on `update-about` before checking out `main`.
- Executed `git merge update-about --no-ff` to generate an explicit merge commit preserving the branch divergence and convergence history.

---

## 7. Evidence / files
- Root documentation updated: [README.md](file:///Users/kakul/Desktop/digital-detective-8017/README.md)
- Mission documentation: [README.md](file:///Users/kakul/Desktop/digital-detective-8017/mission-06-git-github/README.md)
- Feature branch: `update-about` visible on GitHub at `https://github.com/kakuldeka/digital-detective-8017/tree/update-about`

---

## 8. Commit details
- **Commit message:** `Complete Git and GitHub collaboration mission`
- **Target branch:** `main`
- **Remote status:** Pushed and verified on GitHub
