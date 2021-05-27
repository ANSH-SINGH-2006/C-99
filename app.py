import shutil
import os

#take the folder input from the user

path=input("Enter the name of directory to be sorted: ")

#create a list with all the filename present in the directory

list_of_files=os.listdir(path)

#go through each and every file and split the extension

for file in list_of_files:
    name, ext=os.path.splitext(file)
    #storing only the extension types
    ext=ext[1:]

    if ext=='':
        continue

    #we will move the file to the directory if the name ext already exists

    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)
        