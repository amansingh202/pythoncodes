#car game
print("type help to start the game: ")
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == 'start':
        if started:
            print("Car's already started! ")
        else:
            started = True
            print('car started.... Ready to go!')
    elif command == 'stop':
        if not started:
            print("Car's already Stopped")
        else: 
            started = False
            print("Car's stopped!")
    elif command == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - to quit''')
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand your message")

