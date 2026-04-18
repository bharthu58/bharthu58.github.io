---
layout: page
title: "Obsidian — iPhone Capture Pipeline"
---

# Obsidian — iPhone Capture Pipeline

Quick-capture workflow for ideas on iOS without an Obsidian Sync plan.

---

## Flow

```
iPhone (Obsidian → iCloud vault)
        ↓  iCloud for Windows auto-syncs
iCloudDrive\iCloud~md~obsidian\RBK-IOS-VAULT\
        ↓  sync-icloud-inbox.ps1  (manual or scheduled)
Agent Access/rbk-pkm-wiki/raw/
        ↓  /wiki-ingest
rbk-main-wiki/ wiki pages
```

---

## Components

| Component | Role |
|---|---|
| **Obsidian mobile (free)** | Capture on iPhone; vault stored in iCloud |
| **iCloud for Windows** | Syncs vault to `%USERPROFILE%\iCloudDrive\iCloud~md~obsidian\` |
| **`sync-icloud-inbox.ps1`** | Copies new `.md` files to `raw/`, moves originals to `_synced/` |
| **`/wiki-ingest`** | Synthesises raw notes into wiki pages |

---

## Key Config (sync script)

File: `Agent Access/sync-icloud-inbox.ps1`

```powershell
$InboxVaultName = "RBK-IOS-VAULT"   # must match iCloud vault folder name
$TargetRaw      = "G:\My Drive\...\raw"
$LogFile        = "G:\My Drive\...\sync-icloud-inbox.log"
```

- Processed notes → `_synced/` subfolder (prevents re-sync)
- Files prefixed with `yyyyMMdd-HHmmss_` timestamp on arrival in `raw/`

---

## Setup Checklist

- [ ] Install **Obsidian** on iPhone → create vault → store in **iCloud**
- [ ] Name vault `RBK-IOS-VAULT` (or update `$InboxVaultName` in script)
- [ ] Install **iCloud for Windows** (Microsoft Store) → sign in
- [ ] Verify vault appears at `%USERPROFILE%\iCloudDrive\iCloud~md~obsidian\RBK-IOS-VAULT\`
- [ ] Run script once manually to confirm it works
- [ ] (Optional) Schedule via Task Scheduler — daily at 9am

### Schedule (PowerShell, run as admin)
```powershell
$action  = New-ScheduledTaskAction -Execute "powershell.exe" `
             -Argument '-NonInteractive -File "G:\My Drive\RBK-OBSIDIAN-NOTES\rbk-obsidian-vault\Agent Access\sync-icloud-inbox.ps1"'
$trigger = New-ScheduledTaskTrigger -Daily -At 9am
Register-ScheduledTask -TaskName "ObsidianInboxSync" -Action $action -Trigger $trigger -RunLevel Highest
```

### Check your task:
```powershell
Get-ScheduledTask \-TaskName "ObsidianInboxSync"
```

### Check last run / next run:
```powershell
Get-ScheduledTaskInfo \-TaskName "ObsidianInboxSync"
```
### See full details:
```powershell
Get-ScheduledTask \-TaskName "ObsidianInboxSync" | Format-List \*
```
### 🔍 Verify it actually works (important)
### Manually trigger it:
```powershell
Start-ScheduledTask \-TaskName "ObsidianInboxSync"
```
Then check:
```powershell
Get-ScheduledTaskInfo \-TaskName "ObsidianInboxSync"
```
Look at:
*   `LastRunTime`
   
*   `LastTaskResult`
👉 `0` = success

* * *

---

## Daily Habit

1. Jot note in Obsidian (iPhone) — opens blank note instantly
2. iCloud syncs in background
3. Run script (or let scheduler fire) → notes land in `raw/`
4. Run `/wiki-ingest` → ideas become wiki knowledge

---

## Related

- [PKM — Personal Workflow Reference](/wiki/pkm-personal-workflow-reference/)
- [PKM — Note-Making Philosophy](/wiki/pkm-note-making-philosophy/)
- [Obsidian — Plugin Recommendations](/wiki/obsidian-plugin-recommendations/)

