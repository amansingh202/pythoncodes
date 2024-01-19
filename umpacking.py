#unpacking in tuples


coordinates = (2,5,8,12)
'''
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
'''



#by using un packing we can write a far less code

x, y, z ,p = coordinates
print(x)
print(y)
print(z)
print(x*y*z)


#can be used in lists too