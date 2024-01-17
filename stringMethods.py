#string methods

course = 'Python For The Beginners'
print(len(course)) #length of the string

#upper and lower case methods
print(course.upper())
print(course)
print(course.lower())
print(course)

#finding a character
print(course.find('o')) #this method is case sensitive
print(course.find('The'))

#replace
print(course.replace('Beginners', "Intermediate"))

print("Python" in course) #true
print("python" in course) #false 