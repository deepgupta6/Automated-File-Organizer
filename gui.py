import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

from organizer import organize_folder  # import function from Step 1

def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        organize_folder(Path(folder))
        messagebox.showinfo("Success", "Files organized successfully!")

root = tk.Tk()
root.title("Automated File Organizer")

label = tk.Label(root, text="Select a folder to organize:")
label.pack(pady=10)

btn = tk.Button(root, text="Browse", command=browse_folder)
btn.pack(pady=5)

root.mainloop()
