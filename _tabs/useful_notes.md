---
# the default layout is 'page'
icon: fas fa-sticky-note
title: RBK Useful Notes
order: 5.1
---

## WSL Installation on Windows

### Prerequisites
- Command Prompt or PowerShell (run as Administrator)

### Installation Steps

```bash
# Install WSL with a specific distribution
wsl --install -d [Distribution Name]
# Example: wsl --install -d Ubuntu-LTS-2.44

# Check installed distributions and versions
wsl.exe -l -v

# Check WSL status
wsl.exe --status

# Check Linux release information
lsb_release -r
```

---

## Jekyll Setup

### Ubuntu Installation
For detailed instructions, refer to the official documentation:
[Jekyll Installation Guide for Ubuntu](https://jekyllrb.com/docs/installation/ubuntu/)

---

## Personal Resources

### Webpages
- **Portfolio**: [https://bharthu58.github.io/](https://bharthu58.github.io/)

### GitHub Profile
- **GitHub**: [https://github.com/bharthu58](https://github.com/bharthu58)

---

## Python Environment Setup

### Creating and Activating Virtual Environment

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies from requirements file
python3 -m pip install -r requirement.txt
```

**Note**: The `requirement.txt` file contains all project dependencies.

---

## Node.js and npm Overview

### What is npm?

npm (node.js package manager) is the package manager for JavaScript and the world's largest software registry, allowing developers to discover and assemble reusable code packages.

### What is Node.js?

**Definition**: Node.js executes JavaScript code outside of a browser.

#### Traditional JavaScript
- JavaScript is primarily used for **client-side scripting**
- Scripts are embedded in HTML and executed by the browser's JavaScript engine
- Complex computations can slow down client devices (computers, smartphones, etc.)

#### Node.js Advantage
Node.js enables developers to:
- Execute JavaScript on a **server** instead of the client
- Run scripts server-side to generate dynamic web content
- Create command-line tools and server-side applications
- Offload computational load from client devices to servers

### npm as a Package Manager

npm solves a key problem: **code reuse**. Instead of rewriting code, developers can download and use packages written by others.

#### Example: Express Framework
A popular npm package, `express` is a lightweight web framework that enables:
- Simple web routing
- Handling different URLs to serve different webpages
- Managing multiple routes from a single server

This approach makes development faster and more efficient.

---

## Gemini Integration into VS Code

### Available Extensions

- **Gemini CLI Companion**: CLI integration of Gemini Agent into VS Code (similar to Claude Code)
- **Gemini Code Assist**: Chat integration of Gemini into VS Code
- **Google Cloud Console(RBK)**: [https://console.cloud.google.com/welcome/new?project=project-2ed1d764-9372-47f7-a24](https://console.cloud.google.com/welcome/new?project=project-2ed1d764-9372-47f7-a24)

