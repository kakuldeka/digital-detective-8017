# Mission 0 — Create your GitHub workspace

## 1. Task / objective

Create a correctly named GitHub repository and prepare an organised folder structure for all the missions in the Digital Detective assignment.

The objective was to set up a local development workspace, verify the required tools, and publish the project as a public GitHub repository.

**Repository name:** `digital-detective-8017`

## 2. Work completed

- Created the local project directory named `digital-detective-8017`.
- Created the required folder structure for all nine missions (Mission 0–8).
- Created a separate `README.md` inside every mission directory.
- Created the root `README.md` to introduce the project and provide a mission index.
- Created the `evidence/` directory for storing screenshots and supporting outputs.
- Created the initial `number_converter.py` file inside `mission-05-numbers-data/`.
- Verified the availability of Python 3 and Git.
- Initialised the local Git repository with `main` as its initial branch.
- Configured the Git author profile for the assignment.
- Connected the local repository to GitHub and published the setup commit.

## 3. Commands / tools used

| Command / Tool | Purpose |
|---|---|
| `python3 --version` | Checked the installed Python version (3.14.7). |
| `git --version` | Checked the installed Git version (2.54.0, Apple Git-157). |
| `git config --global init.defaultBranch main` | Configured `main` as the default initial branch. |
| `git init -b main` | Initialised the local Git repository on branch `main`. |
| `git remote add origin https://github.com/kakuldeka/digital-detective-8017.git` | Linked local repository to the public GitHub remote repository. |
| `git status` | Checked the repository state and identified untracked files. |
| `mkdir -p` | Created mission directories and evidence folder. |

## 4. My understanding

A Git repository is a project directory whose changes are tracked using Git. It contains the project's files along with the `.git` directory, which stores the repository's history and other version-control information.

GitHub provides online hosting for Git repositories, allowing projects to be published, accessed and collaborated on.

The assignment is organised into separate mission directories to keep related tasks, documentation and evidence together. This makes the repository easier to navigate and maintain.

## 5. Difficulties faced

- Initially, running Git inside subfolders detected the parent home directory repository before an independent local `.git` repository was established.
- Ensuring `main` was the initial branch and properly tracking the remote origin on GitHub.

## 6. How I resolved them

- Initialised a dedicated local repository directly inside `digital-detective-8017` using `git init -b main`.
- Configured the remote origin to `https://github.com/kakuldeka/digital-detective-8017.git` and verified with `git remote -v`.

## 7. Evidence / files

The repository contains the following structure:

```text
digital-detective-8017/
├── .gitignore
├── evidence/
│   ├── .gitkeep
│   └── pr_merge_status.png
├── mission-00-setup/
│   └── README.md
├── mission-01-computer-basics/
│   └── README.md
├── mission-02-terminal/
│   ├── practice-2-1/
│   │   ├── renamed-copy.txt
│   │   └── sample.txt
│   ├── terminal-practice/
│   │   ├── notes-backup.txt
│   │   └── notes.txt
│   └── README.md
├── mission-03-operating-system/
│   └── README.md
├── mission-04-programs/
│   ├── hello.py
│   └── README.md
├── mission-05-numbers-data/
│   ├── number_converter.py
│   └── README.md
├── mission-06-git-github/
│   └── README.md
├── mission-07-networking/
│   └── README.md
├── mission-08-final-report/
│   └── README.md
└── README.md
```

**Tools verified:**

- Python 3.14.7
- Git 2.54.0 (Apple Git-157)

## 8. Commit details

**Commit message:** "Set up Digital Detective mission structure".

**GitHub push status:** Successfully committed and pushed to GitHub.
