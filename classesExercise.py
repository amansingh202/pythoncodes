#exercise is Person, class: person, name attribute and talk method

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        return f"{self.name} is talking"

person1 = Person("Aman")

print(person1.name)
print(person1.talk())

