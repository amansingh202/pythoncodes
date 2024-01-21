#constructors in python

#constructor is a function that gets called at the time of creating an object

class Point:

    #constructor for this class
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move point")

    def draw(self):
        print("draw")

#object of this class

point1 = Point(10,20)
point1.x = 12
print(point1.x)