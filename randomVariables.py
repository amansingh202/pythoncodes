#Random variables

import random


for i in range(3):
    print(random.randint(10,30))

members = ["Aman", "John", "Mary", "Ali"]

leader = random.choice(members)
print("Leader name is ",leader)