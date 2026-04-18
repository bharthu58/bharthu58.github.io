---
layout: page
title: "Linux — Commands Reference"
---

## Most Used Linux Commands (ByteByteGo)

---

### File Viewing
| Command | Description |
|---|---|
| `cat file` | Print file contents |
| `less file` | Scroll through file |
| `head -n 10 file` | Show first lines |
| `tail -n 10 file` | Show last lines |
| `echo "text"` | Print text |
| `nano file` | Simple terminal editor |
| `vim file` | Advanced text editor |

### Text Processing
| Command | Description |
|---|---|
| `grep "pat" file` | Search text patterns |
| `grep -R "pat" path` | Recursive search |
| `awk 'print $1' file` | Extract columns/fields |
| `sort file` | Sort text lines |
| `diff file1 file2` | Compare text files |

### File Management
| Command | Description |
|---|---|
| `ls` | List directory contents |
| `pwd` | Print current directory |
| `cd` | Change directory |
| `touch file` | Create empty file |
| `mkdir dir` | Create directory |
| `rmdir dir` | Remove empty directory |
| `cp src dest` | Copy files/directories |
| `mv src dest` | Move/rename files |
| `rm` | Remove files/directories |
| `ln -s target link` | Create symbolic link |
| `clear` | Clear terminal screen |

### Permissions
| Command | Description |
|---|---|
| `chmod 755 file` | Change file permissions |
| `chown user:group file` | Change ownership |

### User Management
| Command | Description |
|---|---|
| `whoami` | Show current user |
| `sudo cmd` | Run as root |
| `su - user` | Switch user account |
| `passwd` | Change user password |
| `useradd user` | Create user account |
| `adduser user` | Guided user creation |
| `exit` | Exit shell/session |

### Networking
| Command | Description |
|---|---|
| `ssh user@host` | Remote secure login |
| `scp file user@host:path` | Secure file copy |
| `curl URL` | Fetch headers quickly |
| `wget URL` | Download from web |
| `ping host` | Test reachability |
| `traceroute host` | Trace route hops |
| `ip a` | Show IP addresses |
| `ss -tulpn` | List listening ports |
| `netstat -tulpn` | Network ports (legacy) |
| `ifconfig` | Interface info (legacy) |
| `ufw status/allow 22` | Simple firewall rules |
| `iptables -L` | List firewall rules |

### Disk & System Info
| Command | Description |
|---|---|
| `df -h` | Disk space usage |
| `du -sh dir` | Directory size summary |
| `free -h` | Memory usage summary |
| `uname -a` | Kernel/system details |
| `cal` | Show calendar |
| `neofetch` | System info summary |

### Process Management
| Command | Description |
|---|---|
| `ps aux` | List running processes |
| `top` | Live process view |
| `htop` | Better live process view |
| `kill PID` | Terminate by PID |
| `pkill name` | Kill by process name |

### System Control
| Command | Description |
|---|---|
| `systemctl status/start/stop etc` | Manage system services |
| `reboot` | Restart system |
| `shutdown -h now` | Power off now |

### Archiving
| Command | Description |
|---|---|
| `tar -czf a.tgz dir/` | Create/extract archives |
| `zip -r a.zip dir/` | Create zip archive |
| `unzip a.zip` | Extract zip archive |

### Package Management
| Distro | Command |
|---|---|
| Debian/Ubuntu | `apt` |
| Fedora/RHEL | `dnf` |
| Legacy RHEL | `yum` |
| SUSE | `zypper` |
| Universal app packages | `snap` |

### Help & Reference
| Command | Description |
|---|---|
| `man cmd` | Open manual page |
| `whatis cmd` | One-line description |
| `which cmd` | Show command path |
| `whereis cmd` | Find binary/source |
| `history` | Show command history |

---

## See Also

- [Linux — WSL2 Obsidian Vault Access](/wiki/linux-wsl2-obsidian-vault-access/) — accessing Linux (WSL2) filesystems from Windows

