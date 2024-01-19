#challenge for nested  loops in the format shown below

"""
xxxxx
xx
xxxxx
xx
xx
"""
numbers = [5,2,5,2,2]
for i in numbers:
    output = ''
    for j in range(i):
        output += 'x'
    print(output)