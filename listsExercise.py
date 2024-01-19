#Exercise for lists

#Find the largest number in a list

numbers = [23, 45, 63, 61, 99, 2, 101, 26, 55]

max = 0

for i in numbers:
    if (i > max):
        max = i
print(max)