import os

print(help(os))

path = os.getcwd()
fName = os.__getitem__
file_list = os.listdir(path)
fPath = '‪C:\\Users\\Andre\\Desktop\\Python_Drills\\'
abPath = os.path.join(fPath,fName)
for fName in file_list:
    print(abPath)







    
