import os
import shutil

list_of_files = os.listdir()
folder_path = input("Enter folder path: ")
if os.path.exists('list_of_files'):
    print("The files Exist!")
else:
    print("Error!")

images = 0
documents = 0
videos = 0
others = 0
