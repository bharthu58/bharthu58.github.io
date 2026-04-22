---
layout: page
title: "DevOps — Tool Version Management (mise)"
domain: "DevOps"
---

## What is mise?

`mise` (formerly asdf-plugin-manager) is a fast, cross-platform tool version manager. It replaces asdf, nvm, rbenv, pyenv, and similar per-language version managers with a single unified tool. Configure tools per-project via `mise.toml`.

---

## Core Commands

| Command | Description |
|---|---|
| `mise use <tool>@<version>` | **Most used.** Installs tool and adds to local `mise.toml` (e.g. `mise use node@20`) |
| `mise use -g <tool>@<version>` | Installs tool globally (`~/.config/mise/config.toml`) |
| `mise install [tool@version]` | Installs tools defined in `mise.toml` or a specific version |
| `mise ls` | Lists all currently installed/active tools |
| `mise ls-remote <tool>` | Lists available versions of a tool |
| `mise exec <tool>@ver -- <cmd>` | Runs command using specific tool version without modifying config |
| `mise run <task>` | Runs a defined task from `mise.toml` |
| `mise outdated` | Checks for newer versions of installed tools |
| `mise link <path>` | Symlinks a tool installed elsewhere into mise |
| `mise --version` | Checks installed version of mise |

---

## Common Options

| Flag | Meaning |
|---|---|
| `-f`, `--force` | Force reinstall |
| `-y`, `--yes` | Answer yes to all prompts |
| `-p`, `--path` | Specify a config file path |

---

## Key Concepts

- **`mise.toml`** — per-project config file; checked into the repo; defines which tool versions are active in this directory
- **`~/.config/mise/config.toml`** — global config; applies everywhere unless overridden by a local `mise.toml`
- **Activation** — mise hooks into your shell to auto-switch tool versions when you `cd` into a project
- **Tasks** — mise supports task runners (`mise run <task>`) as a lightweight alternative to Makefiles

---

## Common Workflow

```bash
# Initial project setup
mise use node@20          # installs node@20 and writes to mise.toml
mise use python@3.12      # adds python to the same project config
git add mise.toml         # commit the config so team members get same versions

# Team member onboarding
mise install              # reads mise.toml and installs all declared tools

# Check what's installed
mise ls

# Update a tool
mise use node@22          # updates mise.toml to node@22
```

---

## See Also

- [Python — Package Management (uv and pipx)](/wiki/python-package-management-uv-and-pipx/) — Python-specific package and environment management (mise handles the Python version; uv/pipx handle packages)
- [DevOps — GitHub vs GitLab](/wiki/devops-github-vs-gitlab/) — repository and CI/CD tooling

