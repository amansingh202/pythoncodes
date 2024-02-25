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

    def printname(self):
        print(f"{self.name}, {self.age}")

#creating object of this class
        

        
p1 =Person("Jack", 42)

#modifying and deleting object parameters
p1.age = 38

#del p1.age

print(p1.name)
print(p1.age)

#print(type(p1.age))
p1.myfunc()

#creating a child class

# class student is inheriting the class Person
class Student(Person):
    #pass #when we don't want to add anything in the class

    #the init function will overwrite the properties of parent class

    #to keep the inheritance of the parents use Parents init definition

    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.graduationYear = year


x = Student("Mike", 23, 2019)
print(x.graduationYear)
print(x.name + " "+str(x.age))

