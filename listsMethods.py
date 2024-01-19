#methods in lists

numbers =[4,7,12,43,78,61,12]

numbers.append(101)

print(numbers)

#insert at a particular position

numbers.insert(2,3)
print(numbers)

#remove a particular number
numbers.remove(78)
print(numbers)

#pop a number from the end 

numbers.pop()
print(numbers)
'''
#delete all numbers
numbers.clear()
print(numbers)
'''

print(numbers.index(3))

print(43 in numbers) #to check whether a number exists or  not

#count the number of times an element appears in the list
print("number of 12's in the list is: ", numbers.count(12))

#sorting a list with the built in method 

numbers.sort()
print(numbers)

#reverse a list
numbers.reverse()
print("reverse of the list is: ", numbers)

#copying a list
numbers2 = numbers.copy()
print("copied list is: ", numbers2)