#keywords arguments in python

#position of arguments matters in python 

#to get rid of this condition we use keyword arguments

def greet_user(firstName, lastName):
    print(f"Welcome {firstName} {lastName}")
    print("welcome aboard")

print("start")

#keyword arguments, it make the code quite clear
#positional arguments comes before keyword arguments
greet_user("Aman",lastName = "Singh")
greet_user(lastName = "Singh", firstName = "Ashok")

print("Stop")