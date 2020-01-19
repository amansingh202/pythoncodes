#polymorphism and duck typing

class Pycharm:
    def execute(self):
        print("compiling")
        print("debugging")

class Mymethod:
    def method(self):
        print("compiling")
        print("debugging")
        print("spell check")

class Desktop:
    def new_code(self,ide1):
        ide1.method()

class Laptop:
    def code(self,ide):
        ide.execute()

ide=Pycharm()
lap1=Laptop()
lap1.code(ide)

ide1=Mymethod()
des1=Desktop()
des1.new_code(ide1)
