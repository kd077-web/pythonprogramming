#by os module we can create automatically a folder or many file or folders using mkdir .first we have to import os module
import os
#os.mkdir("myapp")
#we can create many more foolders at once line of code as
#import os
#for i in range(0,100):
#    os.rmdir(f"data{i+1}")#for folder inside folder data/data1, for removing dir rmdir
'''
suppose you have created 1500 of folderrs and you want to rename it it willtake long time for renaming the folder if we do manually
so we can rename as 
os.mkdir(source,destination)
'''    
'''
for listing the folders inside directory
folders=os.listdir("dir_name")
'''
#to check in which directory we are
print(os.getcwd())
#to change the current directory 
#os.chdir("\dirname")]
os.chdir("pyhton programming")
