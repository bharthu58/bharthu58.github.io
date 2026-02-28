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
## Node.js Installation
To install Node.js on WSL (Ubuntu), the most flexible and recommended method is

using **Node Version Manager (NVM)**. This allows you to manage multiple versions of Node.js and avoids common permission issues with global packages.

**Method 1: Using NVM (Recommended)**

This is the standard approach for developers because it makes updating and switching versions easy.

1.  **Install cURL:** Ensure you have the tool needed to download the installer.
    
    bash
    
    ```
    sudo apt update && sudo apt install curl -y
    ```
    
    Use code with caution.
    
2.  **Download and Run NVM Installer:** Get the script from the official [nvm-sh GitHub repository](https://github.com/nvm-sh/nvm).
    
    bash
    
    ```
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
    ```
    
    Use code with caution.
    
3.  **Reload Your Shell:** Close and reopen your WSL terminal, or run the following to apply the changes immediately:
    
    bash
    
    ```
    source ~/.bashrc
    ```
    
    Use code with caution.
    
4.  **Install Node.js:**
    *   To install the latest **LTS** (Long-Term Support) version (recommended for most users):
        
        bash
        
        ```
        nvm install --lts
        ```
        
        Use code with caution.
        
    *   To install the absolute latest release:
        
        bash
        
        ```
        nvm install node
        ```
        
        Use code with caution.
        
5.  **Verify Installation:** Check that both Node and npm (Node Package Manager) are active.
    
    bash
    
    ```
    node -v
    npm -v
    ```
* * *

**Method 2: Using Ubuntu Repositories (Quickest)**

If you only need a basic installation and don't care about having the latest version, use the built-in package manager.

1.  **Install Node.js:**
    
    bash
    
    ```
    sudo apt update
    sudo apt install nodejs npm -y
    ```
    
    Use code with caution.
    
2.  **Verify:**
    
    bash
    
    ```
    node -v
    ```
    
    Use code with caution.
    

* * *

**Important Tips for WSL Users**

*   **Avoid Windows-side Node.js:** Do not try to call the Windows version of Node.js from your WSL terminal. It can cause pathing issues and performance slowdowns.
*   **File Performance:** Keep your project files in the **Linux file system** (e.g., `~/projects/`) rather than on the Windows side (`/mnt/c/`) for much faster performance.
*   **VS Code Integration:** If using VS Code, install the [WSL extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl) to run your code directly in the Ubuntu environment.
---

## Gemini Integration into VS Code

### Available Extensions

- **Gemini CLI Companion**: CLI integration of Gemini Agent into VS Code (similar to Claude Code)
- **Gemini Code Assist**: Chat integration of Gemini into VS Code
- **Google Cloud Console(RBK)**: [https://console.cloud.google.com/welcome/new?project=project-2ed1d764-9372-47f7-a24](https://console.cloud.google.com/welcome/new?project=project-2ed1d764-9372-47f7-a24)

