import random
playing = True
number = str(random.randint(0, 9))

print("Enter a number from 0 to 9")
while playing:
    guess = input("Enter number: ")
    
    if number == guess:
        print("CONGRATS!")
        playing = False
    
    else:
        print("Try again!")