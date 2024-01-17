#type conversion
birthYear = input('Birth Year: ')

print(type(birthYear))
age = 2024 - int(birthYear) #type conversion in here
print(type(age))

print("Age is: ", age)

#convert pounds to kg
weightPound = int(input("Enter your weight in pounds: "))
print(type(weightPound))

weightKg = 0.454 * float(weightPound)

print(type(weightKg))
print("weight in Kg is: ", weightKg)

