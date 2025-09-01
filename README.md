# 🤖 Automated File Organizer

A powerful and intuitive Python tool to automatically organize your messy folders into a clean, structured directory hierarchy. Say goodbye to cluttered `Downloads` folders forever!

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.8+-green.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen.svg)

Tired of manually sorting files? This tool watches over your specified folders (like `Downloads`) and intelligently moves files into categorized subfolders based on their type, creation date, and your custom rules.

![GUI Demo](examples/gui_demo.gif)

---

## 📋 Table of Contents

- [✨ Key Features](#-key-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [📂 Project Structure](#-project-structure)
- [🚀 Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [💡 How to Use](#-how-to-use)
  - [1. Command-Line Interface (CLI)](#1-command-line-interface-cli)
  - [2. Graphical User Interface (GUI)](#2-graphical-user-interface-gui)
  - [3. Automated Scheduling](#3-automated-scheduling)
- [🔧 Configuration](#-configuration)
- [📦 Building an Executable](#-building-an-executable)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## ✨ Key Features

-   🧠 **Smart Categorization**: Automatically sorts files into predefined categories like **Images, Documents, Videos, Music, and Archives**.
-   🎨 **Intuitive GUI**: A simple **drag-and-drop** graphical interface built with Tkinter for ease of use.
-   🔧 **Fully Configurable**: Easily define your own categories and file extensions by editing a simple `categories.json` file.
-   🗂️ **Structured Organization**: Organizes files into a `Category/Year/Month` structure for effortless browsing.
-   ⚠️ **Conflict Resolution**: Intelligently handles file name collisions by automatically renaming new files (e.g., `report.pdf` becomes `report (1).pdf`).
-   📅 **Powerful Scheduler**: Set it and forget it! Run the organizer automatically on an hourly or daily basis.
-   ↩️ **Undo Functionality**: Made a mistake? The tool logs every move, allowing you to easily revert the last organization task.
-   📊 **Reporting & Logging**: Generates detailed **CSV/HTML reports** summarizing all file operations and maintains a comprehensive log file.
-   ⚙️ **Flexible CLI**: A robust command-line interface with options for **dry runs**, custom paths, reporting, and log levels.
-   📧 **Email Notifications**: (Optional) Receive daily summary reports directly in your inbox.

---

## 🛠️ Tech Stack

-   **Core Language**: Python 3
-   **Core Libraries**: `os`, `shutil`, `pathlib`, `logging`
-   **CLI**: `argparse`
-   **GUI**: `Tkinter`
-   **Scheduling**: `schedule` (or system `cron`/`Task Scheduler`)
-   **Distribution**: `PyInstaller`

---

## 📂 Project Structure

Automated-File-Organizer/
  │
  ├── organizer.py        # Core CLI logic for file organization
  ├── gui.py              # Tkinter-based GUI application
  ├── scheduler.py        # Script for running organization on a schedule
  │
  ├── categories.json     # User-configurable file type definitions
  ├── history.json        # Stores file move history for the undo feature
  ├── requirements.txt    # Python package dependencies
  ├── README.md           # You are here!
  │
  ├── file_organizer.log  # Auto-generated log file
  ├── reports/            # Directory for generated CSV/HTML summary reports
  ├── dist/               # Default output directory for PyInstaller executables
  └── examples/           # Contains screenshots or demo GIFs

---

## 🚀 Getting Started

### Prerequisites

-   Python 3.8 or newer
-   `pip` (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/Automated-File-Organizer.git](https://github.com/yourusername/Automated-File-Organizer.git)
    cd Automated-File-Organizer
    ```

2.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **(Optional) Customize your categories:**
    Before running, you can open `categories.json` and add or modify file extensions to suit your needs.

---

## 💡 How to Use

You can run the tool in three different ways:

### 1. Command-Line Interface (CLI)

The CLI is perfect for scripting and automation. The primary command organizes files in a specified directory.

**Basic Usage:**
```bash
python organizer.py --path "C:/Users/YourName/Downloads"