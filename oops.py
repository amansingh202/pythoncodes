#oops classes and objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #__str()__ function for string representation
    def __str__(self):
        return f"{self.name}({self.age})"
    
    #creating user defined functions
    def myfunc(self):
        print(f"Hello, the name and age are {self.name}, {self.age}")

#creating object of this class
        
p1 =Person("Jack", 42)

print(p1.name)
print(p1.age)

#print(type(p1.age))
p1.myfunc()