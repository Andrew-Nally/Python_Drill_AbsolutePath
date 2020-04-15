import os
import time

#List all files in directory
File_Dir = os.getcwd()
for entry in os.listdir(File_Dir):
    abPath = os.path.join(File_Dir, entry)
    file_created = os.path.getmtime(abPath)
    file_time = time.ctime(file_created)
    if abPath.endswith(".txt"):
        print(abPath, file_time)
