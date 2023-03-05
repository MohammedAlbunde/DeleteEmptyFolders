#files and folders
import os
import shutil

def delete_files_and_folders(root_path):
    for foldername, subfolders, filenames in os.walk(root_path, topdown=False):
        # Check if the folder is empty, or contains "Terminated" or "Error" in its name
        if (not any([subfolders, filenames])) or ("Terminated" in foldername) or ("Error" in foldername):
            # Delete the folder and its contents
            shutil.rmtree(foldername)
            print(f"Deleted folder: {foldername}")
        
        # Check if the file contains "Terminated" or "Error" in its name
        for filename in filenames:
            if ("Terminated" in filename) or ("Error" in filename):
                # Delete the file
                os.remove(os.path.join(foldername, filename))
                print(f"Deleted file: {os.path.join(foldername, filename)}")

# Ask the user for the path to search for files and folders
root_path = input("Enter the path to search: ")

# Call the function to delete files and folders
delete_files_and_folders(root_path)

