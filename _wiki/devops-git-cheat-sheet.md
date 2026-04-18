---
layout: page
title: "DevOps — Git Cheat Sheet"
---

## Setup

```bash
git config --global user.name "[firstname lastname]"   # identity for commit history
git config --global user.email "[valid-email]"
git config --global color.ui auto                      # coloured output
git config --global core.excludesfile [file]           # system-wide .gitignore
```

## Init & Clone

```bash
git init              # initialise existing directory as a git repo
git clone [url]       # clone a remote repository locally
```

## Stage & Snapshot

```bash
git status                        # show modified files / staging state
git add [file]                    # stage a file for next commit
git reset [file]                  # unstage a file (keep changes in working dir)
git diff                          # diff of changed but not staged
git diff --staged                 # diff of staged but not yet committed
git commit -m "[message]"         # commit staged content as new snapshot
```

## Branch & Merge

```bash
git branch                        # list branches (* = active)
git branch [branch-name]          # create new branch at current commit
git checkout [branch]             # switch to branch
git merge [branch]                # merge specified branch into current
git log                           # show all commits in current branch history
```

## Inspect & Compare

```bash
git log                           # commit history for active branch
git log branchB..branchA          # commits on A not on B
git log --follow [file]           # commits that changed a file, across renames
git diff branchB...branchA        # diff of what's in A but not in B
git show [SHA]                    # show any git object in human-readable format
```

## Share & Update (Remote)

```bash
git remote add [alias] [url]      # add a remote URL with an alias
git fetch [alias]                 # fetch all branches from remote
git merge [alias]/[branch]        # merge remote branch into current
git push [alias] [branch]         # push local commits to remote branch
git pull                          # fetch + merge from tracking remote
```

## Tracking Path Changes

```bash
git rm [file]                     # delete file and stage the removal
git mv [existing] [new-path]      # move/rename file and stage the change
git log --stat -M                 # show commits with path moves indicated
```

## Rewrite History

```bash
git rebase [branch]               # apply current branch commits ahead of specified branch
git reset --hard [commit]         # clear staging area, rewrite working tree from commit
```

## Temporary Commits (Stash)

```bash
git stash                         # save modified and staged changes temporarily
git stash list                    # list stash stack
git stash pop                     # apply top stash and remove from stack
git stash drop                    # discard top stash without applying
```

## Ignoring Patterns

```bash
# .gitignore — place in repo root
logs/
*.notes
pattern*/
```

---

## See Also

- [DevOps — GitHub vs GitLab](/wiki/devops-github-vs-gitlab/) — choosing between GitHub and GitLab platforms
- [DevOps — Tool Version Management (mise)](/wiki/devops-tool-version-management-mise/) — managing tool versions in projects

