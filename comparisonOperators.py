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


