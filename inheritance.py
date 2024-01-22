#inheritance

class Mammals:
    def walk(self):
        print("walk")

#cats and dog class are inheriting the mammals class
class Dog(Mammals):
    def bark(self):
        print("Dog bark's")

class Cat(Mammals):
    def annoying(self):
        print("Cat's are annonying")

dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.walk()
cat1.annoying()