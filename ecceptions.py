#Exceptions in Python

#how to handle errors



#try except in python, program completes in this way and don't crash
try:
    age = int(input("Age: "))
    income = 25000
    risk = income / age
    print(age)

except ValueError:
    print("Invalid format")

except ZeroDivisionError:
    print("Age can't be zero")