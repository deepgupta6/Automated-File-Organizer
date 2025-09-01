# Automated File Organizer

A **Python-based automation tool** that organizes files into structured folders for easy management. It features a **configurable category system**, **GUI**, **scheduler**, **logging**, **undo**, and **report generation**.

---

## Features

- Automatically sorts files into folders like **Images, Documents, Videos, Music, Archives**, etc.
- **Configurable categories** via `categories.json` for custom file types.
- **Multi-level organization**: category → year → month.
- Handles **file name conflicts** automatically.
- **GUI interface** with drag & drop support using **Tkinter**.
- **Scheduler integration**: schedule organization every hour/day (via `schedule` library or system cron/Task Scheduler).
- **Logging** and **report generation**: CSV/HTML summaries of organized files.
- **Undo feature** to restore files to original locations.
- Optional **email notifications** for daily summaries.

---

## Tools & Technologies

**Python, os, shutil, pathlib, argparse, Tkinter, PyInstaller, schedule/cron, logging**

---

## Folder Structure

