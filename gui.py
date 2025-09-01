import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pathlib import Path
from organizer import organize_folder  # import your existing organizer function
import threading

# Function to browse folder
def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_path.set(folder)
        status_label.config(text=f"Selected: {folder}", fg="green")

# Function to run organizer in a thread (so UI doesn't freeze)
def start_organizing():
    folder = folder_path.get()
    if not folder:
        messagebox.showwarning("Warning", "Please select a folder first!")
        return

    # Disable buttons during processing
    browse_btn.config(state="disabled")
    organize_btn.config(state="disabled")
    status_label.config(text="Organizing files...", fg="blue")
    progress_bar.start()

    def task():
        try:
            organize_folder(Path(folder))
            status_label.config(text="Files organized successfully!", fg="green")
            messagebox.showinfo("Success", "Files organized successfully!")
        except Exception as e:
            status_label.config(text=f"Error: {str(e)}", fg="red")
            messagebox.showerror("Error", str(e))
        finally:
            progress_bar.stop()
            browse_btn.config(state="normal")
            organize_btn.config(state="normal")

    threading.Thread(target=task).start()

# Main window
root = tk.Tk()
root.title("📂 Automated File Organizer")
root.geometry("500x300")
root.resizable(False, False)
root.configure(bg="#f0f4f7")

# Folder path variable
folder_path = tk.StringVar()

# Title label
title_label = tk.Label(root, text="Automated File Organizer", font=("Helvetica", 18, "bold"), bg="#f0f4f7", fg="#333")
title_label.pack(pady=15)

# Folder selection frame
frame = tk.Frame(root, bg="#f0f4f7")
frame.pack(pady=10)

folder_entry = tk.Entry(frame, textvariable=folder_path, width=40, font=("Helvetica", 12))
folder_entry.pack(side=tk.LEFT, padx=5)

browse_btn = tk.Button(frame, text="Browse", command=browse_folder, bg="#4CAF50", fg="white", font=("Helvetica", 11), relief="flat", width=10)
browse_btn.pack(side=tk.LEFT, padx=5)

# Organize button
organize_btn = tk.Button(root, text="Organize Files", command=start_organizing, bg="#2196F3", fg="white", font=("Helvetica", 13, "bold"), relief="flat", width=20)
organize_btn.pack(pady=20)

# Progress bar
progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="indeterminate")
progress_bar.pack(pady=10)

# Status label
status_label = tk.Label(root, text="Select a folder to start.", font=("Helvetica", 11), bg="#f0f4f7", fg="#555")
status_label.pack(pady=5)

# Run the app
root.mainloop()
