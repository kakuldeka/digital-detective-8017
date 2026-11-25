# Mission 6 — Git and GitHub

## 1. Task / objective

Understand how Git tracks changes in a project and how GitHub supports collaboration through remote repositories, branches and Pull Requests.

The objective was to explore the basic Git workflow, create and publish a separate branch, update the root README, open a Pull Request, and understand how changes are reviewed and merged into the main branch.

## 2. Work completed

### Task 6.1 — Understand the basic Git workflow

Inspected the repository status, current branch and recent commit history using Git commands.

**Repository status:**

Command:

```bash
git status
```

Observed output:

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

The working tree was clean, meaning there were no pending changes to commit. The local `main` branch was also synchronised with its remote counterpart, `origin/main`.

**Current branch:**

Command:

```bash
git branch --show-current
```

Observed output:

```text
main
```

This confirmed that the repository was initially on the `main` branch.

**Recent commit history:**

Command:

```bash
git log --oneline
```

The commits were displayed showing chronological mission progress across the repository.

**Basic Git operations:**

| Git operation | What it does in my own words |
|---|---|
| Check repository status | Shows the current branch and whether files have been modified, staged or left untracked. |
| Stage selected changes | Selects specific changes and places them in the staging area so they can be included in the next commit. |
| Create a commit | Saves the staged changes as a new snapshot in the repository's local history. |
| View commit history | Displays previous commits, their messages and other information about the project's history. |

**Difference between staging and committing:**

Staging and committing are two separate operations in Git. `git add` selects the changes that should be included in the next commit, whereas `git commit` records those staged changes in the repository's history.

A staged change is not yet a commit. It must be committed before it becomes part of the local commit history.

### Task 6.2 — Create and use a branch

Created a separate branch named `update-about` for updating the project documentation.

Command:

```bash
git checkout -b update-about
```

Updated the root `README.md` to add a new section titled **My Learning**, describing key takeaways from the assignment so far.

Staged the changed file, inspected the staged diff, committed the change and pushed the new branch to GitHub:

```bash
git add README.md
git commit -m "Add My Learning section to root README"
git push -u origin update-about
```

### Task 6.3 — Create a Pull Request

On GitHub, compared the newly published `update-about` branch with `main` and created a Pull Request to merge the documentation update.

Reviewed the changed files and integrated the changes into `main` using a merge commit:

```bash
git checkout main
git merge update-about --no-ff -m "Merge pull request: integrate update-about into main"
git push origin main
```

The merged README update was successfully integrated into `main`.

### Task 6.4 — Build your Git command glossary

| Git operation | Command | Explanation |
|---|---|---|
| Initialise a repository | `git init` | Creates a new Git repository in the current directory. |
| Check status | `git status` | Displays the current branch and the state of tracked and untracked files. |
| Stage changes | `git add <file>` | Selects changes to be included in the next commit. |
| Commit changes | `git commit -m "message"` | Records the staged changes as a new commit in local history. |
| View history | `git log --oneline` | Displays the repository's commit history in a compact format. |
| Create or list branches | `git branch` | Lists existing branches; `git branch <name>` creates a new branch. |
| Switch branches | `git switch <branch>` | Switches the currently checked-out branch. |
| Publish changes | `git push` | Publishes local commits to the corresponding remote branch. |
| Retrieve remote changes | `git pull` | Fetches remote changes and integrates them into the current local branch. |

The repository had already been initialised during Mission 0, so `git init` was included in the glossary for reference rather than executed again.

## 3. Commands / tools used

| Command / Tool | Purpose |
|---|---|
| `git status` | Checks the current branch and the state of the working tree. |
| `git branch --show-current` | Displays the currently checked-out branch. |
| `git log --oneline` | Displays recent commits in a compact format. |
| `git checkout -b update-about` | Creates and switches to the `update-about` branch. |
| `git add README.md` | Stages the root README change. |
| `git commit -m "message"` | Records staged changes in the local repository. |
| `git push -u origin update-about` | Publishes the new branch and sets its upstream tracking branch. |
| `git checkout main` | Switches back to the main branch. |
| `git merge update-about` | Merges the feature branch into main with a merge commit. |
| `git push origin main` | Pushes the integrated main branch to GitHub. |
| `git log --oneline --graph` | Displays commit history with branch and merge relationships. |
| Git | Tracks project changes and maintains commit history. |
| GitHub | Hosts the remote repository and provides collaboration features. |

## 4. My understanding

I learned how Git tracks changes in a project and how its staging area and commit history work together.

The working directory contains the actual project files. Changes can be selected using `git add`, which places them in the staging area. Once ready, `git commit` records those selected changes in the repository's local history. Finally, `git push` publishes local commits to a remote repository.

I also learned how branches provide separate lines of development. Instead of modifying the main branch directly, I created `update-about` and made the README changes there.

A Pull Request is a proposal to merge changes from one branch into another. It provides an opportunity to inspect and discuss changes before integrating them into the main project.

In this mission, the branch `update-about` was created, pushed to GitHub, and merged into `main`. The resulting merge commit preserved the relationship between the two branches in the commit history.

I also understood the difference between Git and GitHub. Git handles version control locally, while GitHub hosts repositories online and provides collaboration features such as Pull Requests.

## 5. Difficulties faced

No major difficulties were encountered during this mission.

One important distinction I understood was that merging a Pull Request through GitHub and merging branches directly using local Git commands are different workflows that produce corresponding merge records.

## 6. How I resolved them

Created and published the `update-about` branch, merged into `main` preserving the commit relationship, and verified the commit graph and GitHub repository status.

## 7. Evidence / files

- `README.md` — Root repository README updated with the My Learning section.
- `mission-06-git-github/README.md` — Contains the Git workflow explanations, command glossary, branch details, Pull Request information and learning notes.
- Branch `update-about` — Visible on GitHub at `https://github.com/kakuldeka/digital-detective-8017/tree/update-about`.
- Screenshot evidence: `evidence/pr_merge_status.png` — Verified compare status on GitHub.

## 8. Commit details

**Commit message:** `Complete Git and GitHub collaboration mission`

**Push status:** Successfully committed and pushed to GitHub.
