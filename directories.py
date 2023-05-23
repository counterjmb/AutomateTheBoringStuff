import os

#goes through each folder
location = os.getcwd()
print('Location: ' + str(location))
for foldername, subfolders, filenames in os.walk(location):
    print('Folder: ' + foldername)
    print('Subfolders: ' + str(subfolders))
    print('Files: ' + str(filenames))