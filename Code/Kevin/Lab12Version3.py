tryCounter = 1
import random
xNumber = random.randint(1,10)
print(xNumber)
#guessNumber = int(input(f"Guess a number between 1 and 10. \n"))

while True:
    guessNumber = int(input(f"Guess a number between 1 and 10. \n"))
    if guessNumber == xNumber:
        print(f"You guessed correctly! The correct number is: {xNumber}! It took you {tryCounter} tries.")
        break
    else:
        if guessNumber > xNumber:
            print(f"Sorry, that number is incorrect and is too high! Please try again. \n")
            tryCounter +=1
        if guessNumber < xNumber:
            print(f"Sorry, that number is incorrect and is too low! Please try again. \n")
            tryCounter +=1
            