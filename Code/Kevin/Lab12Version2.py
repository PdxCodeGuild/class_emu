tryCounter = 1
import random
xNumber = random.randint(1,10)
print(xNumber)

while True:
    guessNumber = int(input(f"Guess a number between 1 and 10. \n"))
    if xNumber == guessNumber:
        print(f"You guessed correctly! The correct number is: {xNumber}! It took you {tryCounter} tries.")
        break
    else:
        print(f"Sorry, that number is incorrect! Please try again. \n")
        tryCounter +=1
    # guessNumber = int(input(f"Guess a number between 1 and 10. \n"))
    # if xNumber == guessNumber:
    #     print(f"You guessed correctly! The correct number is: {xNumber}! It took you {tryCounter} tries")
    #     break
