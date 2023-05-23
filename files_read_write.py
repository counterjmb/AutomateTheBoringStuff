import os, shelve
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

textfile = open('test.txt')
print(textfile.read())
textfile.close()
#each line as a string textfile.readlines()

#open file for writeing
# w - write mode will overwrite contents
# a - append mode will add to the end of the file
# if file doesn't exist it will be created
writefile = open('test.txt', 'a')
writefile.write('\nAdded to file')
#will return how many bytes adds - you can ignore
writefile.close()


# for large text opbjects, use the shelve module. 
# it's like a dictionary for saved files
shelveFile = shelve.open('myShelve')
shelveFile.close()