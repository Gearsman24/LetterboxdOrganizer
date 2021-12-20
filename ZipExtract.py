# Internal Libraries for Zip Extract
import os
from datetime import datetime
from zipfile import ZipFile
from pathlib import Path

def zip_extract(username):
    # Determine Directory of ZipFile
    downloads_path = (Path.home() / "Downloads")
    time = datetime.utcnow()
    hour = str(time.hour) if time.hour > 9 else "0" + str(time.hour)
    minute = str(time.minute) if time.minute > 9 else "0" + str(time.minute)
    day = str(time.day) if time.day > 9 else "0" + str(time.day)
    month = str(time.month) if time.month > 9 else "0" + str(time.month)
    zip_path = downloads_path / ("letterboxd-" + username + "-" + str(time.year) + "-" + month + "-" + day + "-" + hour + "-" + minute + "-utc.zip")

    # Extract Letterboxd csv Lists into Data Folder
    try:
        with ZipFile(zip_path, 'r') as zipObj:
            for file_name in zipObj.namelist():
                if 'lists/' in file_name and 'deleted' not in file_name:
                    zipObj.extract(file_name, 'data')
        
        os.remove(zip_path)
        return True
    except:
        os.remove(zip_path)
        return False