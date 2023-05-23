import shutil, os
#copy and renamte a file
#shutil.copy('source.txt', 'destination\rename.txt')
#copy whole folder
#shutil.copytree('source', 'destination')
#move a file
#shutil.move('file', 'destination')
#rename file
#use move to same location just as a new name


#delete a file: 3 ways
os.unlink('bacon.txt')
# has to be empty
os.rmdir('tmp')
#delete all files and folder
shutil.rmtree('tmp')

#send to trash module: needs pip
#send2trash.send2trash('path')
