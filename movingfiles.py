import os 
import shutil

source=input("Folder Path: ")

destination=input("Folder Path: ")

source=source+'/'
destination=destination+'/'

list_of_files= os.listdir(source)

for file in list_of_files:
    shutil.move((source+file), destination)
