---
layout: page
title: "Python — Package Management (uv and pipx)"
domain: "Python"
---

## Overview

Two complementary tools for Python package management:
- **`uv`** — fast, all-in-one project manager, virtual environment manager, and pip replacement (Rust-based)
- **`pipx`** — installs CLI tools in isolated environments; the standard for global Python CLI tools

They overlap in the "install CLI tool globally" use case — `uv tool install` vs `pipx install`. `uv` is the modern default; `pipx` is still widely used.

---

## uv — The All-in-One Python Tool

`uv` is a Rust-based drop-in replacement for `pip`, `pip-tools`, `venv`, and package management — significantly faster than any Python-native tool.

### Project Management (`pyproject.toml`)

| Command | Description |
|---|---|
| `uv init` | Initialise a new Python project |
| `uv add <package>` | Add a dependency to the project |
| `uv remove <package>` | Remove a dependency |
| `uv sync` | Sync the virtual environment with project dependencies |
| `uv run <command>` | Run a script or command in the project's environment |

### Virtual Environments & Python Versions

| Command | Description |
|---|---|
| `uv venv` | Create a new virtual environment (default: `.venv`) |
| `uv python install <version>` | Install a specific Python version (e.g. `3.12`) |
| `uv python list` | List available and installed Python versions |

### Tool Management (pipx alternative)

| Command | Description |
|---|---|
| `uv tool install <tool>` | Install a CLI tool globally in an isolated environment |
| `uv tool upgrade-all` | Upgrade all installed tools |
| `uvx <tool>` | Run a tool on-the-fly without installing it |

### Pip Interface (pip / pip-tools alternative)

| Command | Description |
|---|---|
| `uv pip install <package>` | Install a package into the active environment |
| `uv pip compile reqs.in` | Lock dependencies into a `requirements.txt` |
| `uv pip sync reqs.txt` | Sync environment exactly to a `requirements.txt` |
| `uv pip freeze` | List currently installed packages and versions |

---

## pipx — Global CLI Tool Installer

`pipx` installs Python CLI applications in isolated virtual environments — each tool gets its own environment, preventing dependency conflicts.

### When to Use pipx

Use for global CLI tools you want available system-wide: `black`, `mypy`, `httpie`, `cookiecutter`, etc.
**Do not use** for libraries you import in code or for project-specific dependencies (use `uv` or `pip` for those).

### Installation

```bash
# Debian/Ubuntu Linux
sudo apt install pipx
pipx ensurepath  # add to PATH
# restart terminal

# Windows / other
pip install --user pipx
pipx ensurepath
```

### Common Commands

| Command | Description |
|---|---|
| `pipx install <package>` | Install an application |
| `pipx list` | List installed applications |
| `pipx upgrade <package>` | Upgrade an application |
| `pipx upgrade-all` | Upgrade all applications |
| `pipx uninstall <package>` | Uninstall an application |
| `pipx run <package>` | Run application temporarily (no install) |

---

## Decision Guide

| Scenario | Tool |
|---|---|
| New Python project with dependencies | `uv init` + `uv add` |
| Isolated virtual environment | `uv venv` |
| Install a specific Python version | `uv python install` |
| Install a global CLI tool | `uv tool install` or `pipx install` |
| Run a tool without installing | `uvx <tool>` |
| Lock/sync requirements.txt workflow | `uv pip compile` + `uv pip sync` |
| Replace pip in existing workflow | `uv pip install` |
| Manage the Python version itself | `mise use python@3.12` (see [DevOps — Tool Version Management (mise)](/wiki/devops-tool-version-management-mise/)) |

---

## See Also

- [DevOps — Tool Version Management (mise)](/wiki/devops-tool-version-management-mise/) — manages the Python version; uv/pipx manage packages within that version
- [DevOps — GitHub vs GitLab](/wiki/devops-github-vs-gitlab/) — CI/CD tooling context for Python project deployment

