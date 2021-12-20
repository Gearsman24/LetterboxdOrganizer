# Python Modules
from Download import download
from ZipExtract import zip_extract

# Import Internal Libraries
import os
import shutil
from urllib.parse import urlparse
from getpass import getpass

if __name__ == "__main__":
    # Constants
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(BASE_DIR, "data")
    # If Data Directory already has values
    if os.path.exists(DATA_DIR):
        shutil.rmtree(DATA_DIR)
    os.makedirs(DATA_DIR)

    while(True):
        # Get Username and Password
        username = getpass("Input your Letterboxd username\n")
        password = getpass("Input your Letterboxd password\n")

        # Download Stats Zip File
        dl_pass = download(username, password)
        if(not dl_pass):
            print("Invalid Username or Password\n")
            continue
        break

    # Extract Lists from Zip File into Data Folder
    zip_pass = zip_extract(username)
    if(not zip_extract):
        print("Error when Zip Extracting!")

    """Continue From Here..."""
    # Organize Data into Folders
    

    # Remove Storage of Data
    shutil.rmtree(DATA_DIR)