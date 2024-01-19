#exrcise in a list

#Write a program to remove the duplicates in a list

numbers = [12,14,15,17,22,12,15,17]

unique = []

for i in numbers:
    if i not in unique:
        unique.append(i)

print(unique)