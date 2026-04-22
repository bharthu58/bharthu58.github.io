---
layout: page
title: "Linux — WSL2 Obsidian Vault Access"
domain: "Linux"
---

## Overview

Managing Obsidian vaults stored in the WSL2 filesystem from Windows. For best performance, keep vault files within the WSL filesystem (e.g. `/home/username/vault`) and access via the `\\wsl$\` network path — this avoids file-watching performance issues.

---

## Method 1 — Direct Access via `\\wsl$` (Recommended)

1. Open Obsidian on Windows
2. Click **Open folder as vault**
3. In the file dialog address bar, enter: `\\wsl$`
4. Navigate to your WSL distribution files (e.g. `\\wsl$\Ubuntu\home\youruser\vault`)
5. Select the vault folder

**Why this works:** Windows exposes the WSL2 filesystem via a network-share-like path. Obsidian on Windows can open it directly. File watching works correctly when the vault stays in the WSL filesystem.

---

## Method 2 — Symlinking

1. Create a folder in your Windows filesystem (e.g. `C:\Users\yourname\ObsidianVaults\`)
2. In WSL, create a symbolic link pointing to the Windows-accessible location:
   ```bash
   ln -s /mnt/c/Users/yourname/ObsidianVaults/myvault ~/vault
   ```
   Or in reverse — symlink from Windows into WSL (requires WSL admin).

**Note:** Cross-filesystem symlinks can have performance implications; the `\\wsl$` method is generally preferred.

---

## Performance Notes

- **Keep vault IN WSL filesystem** — do not store the vault in `/mnt/c/...` (the Windows drive mounted in WSL). Cross-filesystem I/O is slow.
- **Open from Windows side via `\\wsl$`** — not from within WSL's file manager
- Obsidian's file watcher performs better when the vault is natively in WSL

---

## This Vault

This Obsidian vault (`rbk-obsidian-vault`) is stored on a Windows-accessible Google Drive path (`/mnt/g/My Drive/...`) and accessed directly — not via WSL filesystem. Claude Code (running in WSL2) accesses it via the `/mnt/g/` mount.

---

## See Also

- [Linux — Commands Reference](/wiki/linux-commands-reference/) — Linux command reference including filesystem navigation
- [Obsidian — Word and Google Docs Integration](/wiki/obsidian-word-and-google-docs-integration/) — other Obsidian tooling

