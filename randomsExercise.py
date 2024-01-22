#Roll a dice and every time a dice is rolled print the value ie.. (1,1), (5,6) etc.

import random

class Dice:

    def roll(self):
        num1 = random.randint(1,6)
        num2 = random.randint(1,6)

        return (num1, num2)
    

dice1 = Dice()
print(dice1.roll())