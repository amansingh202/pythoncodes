#files and directories in python
from pathlib import Path

#absolute path ex: c:\Program files\Microsoft
#relative path 

path = Path("emails")

print(path.exists()) #to check whether a path named emails exits or not

#to create a new directory

#print(path.mkdir())

#the above line of code will create a new directory called emails

path2 = Path("Airline")

#print(path2.mkdir()) #this will create directory callied Airline

#to remove a directory
#print(path2.rmdir())
#this will remove the airline directory


#to check for all the files and directories in a given path
path3 = Path()
for file in path3.glob('*.py'):  #* means everything
    print(file)

