import os
# os module uses system specific (mac / win) sperators to navigate 
print(os.path.join('root','folder','file.png'))

# current working directory
print(os.getcwd())
#os.chdir to change dir
#os.abspath to give absolute path of file
#os.relpath to give relateive path of file
#os.path.exists boolean if file exists 
#os.isdir os.isfile to check file
#os.getsize for byte size
#os.listdir get all files and folders

#reading plain text files