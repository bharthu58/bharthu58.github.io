# From "It Works on My Machine" to "It Works Everywhere": Building the Ultimate Polyglot Bootstrap

We have all been there. You get a new laptop, or you spin up a fresh cloud instance, and the excitement of a clean slate is immediately replaced by the dread of **The Setup**.

You spend four hours installing `nvm`, then `pyenv`, then realizing your system Python conflicts with your project Python. Then you install `zsh`, but your aliases are in `.bashrc`. You try to run a C++ build, but `cmake` is too old.

I decided to solve this problem once and for all. I didn't just want a dotfiles repo; I wanted a **System State Engine**. I wanted a single command that could turn a bare-bones Ubuntu server or a fresh Docker container into a world-class, AI-enhanced, polyglot engineering environment.

Here is the journey of building **rbk-dotfiles**.

---

## The Requirements: High-Performance & Polyglot

I am not just building a web app. My workflow requires a heavy-duty, polyglot stack. A standard "install node and git" script wouldn't cut it. I needed:

1.  **Polyglot Runtimes**: Node.js (LTS), Python 3.12+, Java 21, and CMake 3.28+.
2.  **Modern C++ Toolchain**: Clang, Ninja, Ccache, and GDB.
3.  **AI-Native Workflow**: Gemini and Claude CLIs integrated directly into the shell.
4.  **Container Compatibility**: The script must run on my laptop *and* inside a CI/Docker container without human intervention.
5.  **Verification**: A way to prove the environment is correct programmatically.

## The Stack Selection

To achieve this, I moved away from the old school `apt-get install everything` approach and embraced modern tooling.

### 1. The Runtime Manager: `mise`
I ditched `nvm`, `pyenv`, and `jenv` in favor of **mise**.
Mise (formerly rtx) is written in Rust. It’s blazing fast, manages multiple languages via a single CLI, and handles environment variables better than the competition.

### 2. The Dotfile Manager: `chezmoi`
Symlinking files manually is fragile. **chezmoi** allows me to manage dotfiles as templates. It handles permissions securely and allows me to inject machine-specific configurations dynamically.

### 3. The Shell: Bash + Starship
While Zsh is popular, Bash is universal. I decided to optimize Bash with **Starship**, a cross-shell prompt that gives me git status, package versions, and execution time at a glance.

---

## The Challenge: The "Bootstrap" Paradox

The hardest part of automating a setup is the "chicken and egg" problem. You need tools to install tools.

### Solving the Container vs. Sudo Problem
One of the biggest headaches was making the script work in Docker. Standard Ubuntu containers run as `root` but don't have `sudo` installed. My local machine runs as a user *with* `sudo`.

I wrote a logic block in `bootstrap.sh` to detect the environment and adapt:

```bash
# Container/CI compatibility: Ensure sudo exists or we are root
if ! command -v sudo &> /dev/null; then
  if [ "$(id -u)" -eq 0 ]; then
    echo "⚠️  Running as root without sudo. Installing sudo for compatibility..."
    apt-get update && apt-get install -y sudo
  else
    echo "❌ Error: This script requires 'sudo' or root privileges."
    exit 1
  fi
fi
```

This ensures the script is portable across bare metal and cloud containers.

### The "Shim" Wars: Installing AI CLIs
I wanted the Google Gemini CLI available globally. However, installing global NPM packages via `mise` sometimes results in path issues where the binary isn't immediately visible to the shell.

I had to write a custom detection loop to find where `npm` put the binary and force-link it to `~/.local/bin`:

```bash
# Discover the global npm bin dir for mise's node
BIN_DIR="$(mise exec node@lts -- npm prefix -g 2>/dev/null)/bin"

# Look for variations of the binary name
CANDS=(gemini gemini-cli gemini-chat generative-ai-cli)
for b in "${CANDS[@]}"; do
  if [ -x "$BIN_DIR/$b" ]; then
    ln -sf "$BIN_DIR/$b" "$HOME/.local/bin/gemini"
    break
  fi
done
```

This guarantees that when I type `gemini`, it actually works, regardless of how the upstream package names their binary.

---

## The "Secret Sauce": AI Integration

This isn't just a coding environment; it's a **thinking** environment. I integrated custom AI commands directly into the workflow.

I created a configuration for `gemini` specifically for high-frequency trading architecture design. By placing a TOML file in `~/.gemini/commands/trade-engine.toml`, I can trigger a specific persona:

```toml
name = "trade-engine"
description = "Design and implementation plan for an Always-On AI Hedging Engine."
prompt = '''
You are a Senior Quantitative Systems Architect specializing in Ultra-Low Latency (ULL)...
Technical Stack: C++20/23, Aeron IPC, QuestDB, LibTorch...
'''
```

Now, I simply type `gemini trade-engine` in my terminal, and I have an AI architect context-aware of my specific C++ stack ready to help.

---

## Trust but Verify: The Testing Harness

A bootstrap script is code, and code needs tests. I didn't want to wipe my laptop every time I tweaked a line of code.

I built a **Docker Test Harness** (`test-in-docker.sh`). It mounts the current repository into a fresh `ubuntu:latest` container and runs the bootstrap.

```bash
docker run --rm -it \
  -v "$REPO_ROOT:/root/dotfiles" \
  -w /root/dotfiles \
  -e TEST_MODE=true \
  ubuntu:latest \
  bash -c "bash bootstrap.sh && bash verify-bs.sh"
```

But I went a step further. I wrote a **Verification Script** (`verify-bs.sh`). It’s essentially a unit test suite for my operating system. It checks:
1.  Are `node`, `python`, `java`, `cmake` accessible?
2.  Is the C++ toolchain (`clang`, `ninja`) healthy?
3.  Did `chezmoi` apply the config files?
4.  Is `starship` hooked into `.bashrc`?

If `verify-bs.sh` exits with code 0, I know the environment is perfect.

---

## The Result

The final result is a repository that I can clone on any machine, run `./bootstrap.sh`, and within minutes, have a production-ready environment.

*   **No more version conflicts.**
*   **No more missing paths.**
*   **No more "it works on my machine."**

It installs everything from `neovim` and `tmux` to `clang-tidy` and `gemini-cli`. It configures my shell with safety aliases (like `rm -I`) and modern tools (`ripgrep` instead of `grep`).

If you are tired of manual setups, I highly recommend adopting a "Bootstrap + Verify" pattern. It turns your development environment into immutable infrastructure.

**Check out the project structure:**
*   `bootstrap.sh`: The engine.
*   `verify-bs.sh`: The quality assurance.
*   `test-in-docker.sh`: The lab.
*   `.tool-versions`: The source of truth for languages.

Happy Coding! 🚀
