#If else statements

is_hot = False
is_cold = True
 
if is_hot:
    print("It's a hot day")
    print('Drink plenty of water')
elif is_cold:
    print("It's a cold day")
    print("wear warm clothes")
else:
    print("It's a lovely day")
print("Have a good day")

#Exercise, price of house = $1 million, good credit -> 8% deposit, otherwise -> 20% deposit

price = 1000000

hasGoodCredit = bool(input("Enter True or False only: "))

if hasGoodCredit:
    deposit = 0.08 * price
else: 
    deposit = 0.2*price

print("Amount is: ", deposit)

