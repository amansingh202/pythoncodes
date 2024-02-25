#oops classes and objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#creating object of this class
        
p1 =Person("Jack", 42)

print(p1.name)
print(p1.age)