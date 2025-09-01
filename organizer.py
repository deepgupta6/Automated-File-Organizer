import os
import shutil
from pathlib import Path
import argparse
import logging

# Setup logging
logging.basicConfig(
    filename="file_organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"]
}

def organize_folder(folder_path: Path):
    if not folder_path.exists():
        print("❌ Folder does not exist.")
        return

    for file in folder_path.iterdir():
        if file.is_file():
            moved = False
            for category, extensions in FILE_TYPES.items():
                if file.suffix.lower() in extensions:
                    category_folder = folder_path / category
                    category_folder.mkdir(exist_ok=True)
                    shutil.move(str(file), str(category_folder / file.name))
                    logging.info(f"Moved {file.name} to {category}/")
                    moved = True
                    break

            if not moved:
                other_folder = folder_path / "Others"
                other_folder.mkdir(exist_ok=True)
                shutil.move(str(file), str(other_folder / file.name))
                logging.info(f"Moved {file.name} to Others/")

    print("✅ Files organized successfully!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automated File Organizer")
    parser.add_argument("path", type=str, help="Path of folder to organize")
    args = parser.parse_args()
    organize_folder(Path(args.path))
