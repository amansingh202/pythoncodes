#Comparison operators in python

#if temp is > 30 -> hot day
#if temp < 10 cold day
#otherwise neither hot nor cold


temp = float(input("Enter the temperature in degree C: "))

if temp > 30:
    print(f"It's a hot day at {temp} degree C")

elif temp < 10:
    print(f"It's a cold day at {temp} degree C")

else:
    print(f"It's neither hot nor cold day at {temp} degree C")


#Exercise
"""If name is less than 3 characters long -> name must be 3 characters long
otherwise if it's more than 50 characters long -> name can be a maximum of 50 characters
otherwise -> name looks good"""

name = input("Enter the Person's name: ")

if len(name) < 3:
    print(f"name must be atleat 3 characters long")
elif len(name) > 50:
    print("name can be a maximum of 50 characters")
else:
    print("name look's good!")