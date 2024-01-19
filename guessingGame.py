#guessing game
secretNumber = 9
guessCount = 0
guessLimit = 3
while guessCount < guessLimit:
    guess = int(input('Guess: '))
    guessCount += 1
    if guess == secretNumber:
        print('You won!')
        break
    
else:
    print("You lost!")