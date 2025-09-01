import schedule
import time
from pathlib import Path
from organizer import organize_folder

FOLDER_TO_ORGANIZE = Path("C:/Users/Dell/Downloads")

def job():
    print("Running scheduled file organization...")
    organize_folder(FOLDER_TO_ORGANIZE)

# Run every 1 hour
schedule.every(1).hours.do(job)

while True:
    schedule.run_pending()
    time.sleep(60)
