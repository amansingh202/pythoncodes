#files and directories in python
from pathlib import Path

#absolute path ex: c:\Program files\Microsoft
#relative path 

path = Path("emails")

print(path.exists()) #to check whether a path named emails exits or not

#to create a new directory

print(path.mkdir())

#the above line of code will create a new directory called emails

path2 = Path("Airline")

print(path2.mkdir()) #this will create directory callied Airline

