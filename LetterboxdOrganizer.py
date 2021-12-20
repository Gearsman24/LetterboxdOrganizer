# Python Modules
from Download import download
from ZipExtract import zip_extract
from Organize import organize

# Import Internal Libraries
import os
import shutil
from urllib.parse import urlparse
from getpass import getpass

if __name__ == "__main__":
    # Constants
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(BASE_DIR, "data")
    LISTS_DIR = os.path.join(DATA_DIR, "lists")
    FOLDER_DIR = os.path.join(BASE_DIR, "folders")

    # Create Empty Data Directory
    print("Creating Empty Data Directory...", end=" ")
    os.makedirs(DATA_DIR)
    print("DONE")

    # Create Empty Folder Directory
    print("Creating Empty Folder Directory...", end=" ")
    if os.path.exists(FOLDER_DIR):
        shutil.rmtree(FOLDER_DIR)
    os.makedirs(FOLDER_DIR)
    print("DONE\n")

    while(True):
        # Get Username and Password
        username = getpass("Input your Letterboxd username\n")
        password = getpass("Input your Letterboxd password\n")

        # Download Stats Zip File
        print("\nDownloading Data...")
        dl_pass = download(username, password)
        if(not dl_pass):
            print("\ninvalid Username or Password\n")
            continue
        break
    print("Downloading Data... DONE")

    # Extract Lists from Zip File into Data Folder
    print("Extracting Data from Zip...", end=" ")
    zip_pass = zip_extract(username)
    print("DONE")

    # Organize Data into Folders
    print("Organizing Data...", end= " ")
    organize(LISTS_DIR, FOLDER_DIR)
    print("DONE\n")
    print("Your Letterboxd Lists Are Organized!")

    # Remove Storage of Data
    shutil.rmtree(DATA_DIR)