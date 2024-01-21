#classes in python, 
#point class will have methods like move, dran, get, distance methods on points

class Point: #always capitalize the first word in class
    def move(self):
        print("move")

    def draw(self):
        print("draw")

#objects of point class

#first object        
point1 = Point()
point1.draw()

#second object
point2 = Point()
point2.x = 20 #herex is the attribute of the point class, which can be defined anywhere in the program
print(point2.x)
