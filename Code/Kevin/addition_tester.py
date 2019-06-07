tryCounter = 1
import random
xNumber = random.randint(1,10)
print(xNumber)
guessNumber = int(input(f"Guess a number between 1 and 10. You have 3 tries to guess the number correctly. \n"))
while tryCounter !=3:
    if xNumber == guessNumber:
        print(f"You guessed correctly! The correct number is: {xNumber}!")
        break
    else:
        print(f"Sorry, that number is incorrect! Please try again. You have {3-tryCounter} more tries to go! \n")
        tryCounter +=1
    guessNumber = int(input(f"Guess a number between 1 and 10. \n"))
    if xNumber == guessNumber:
        print(f"You guessed correctly! The correct number is: {xNumber}!")
        break
