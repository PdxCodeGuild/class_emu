# addition_tester.py


#imports "random" module to be used here
import random
#assigns "var1" to a random choice between 0 and 5"
num1 = random.randint(0, 5)
#assigns "var2" to a random choice between 0 and 5"
num2 = random.randint(0, 5)
#An f string has code in it and also prints to screen.
#this one adds num1 and num2 in a sentence
print(f"what is {num1} + {num2}?")


#While loop. If all statements are true, it will end
while True:
#assigns "user_answer to whatever the user inputs"
    user_answer = input("what is your answer?: ")
#turns user input into a whole number
    user_answer = int(user_answer)
#compares the user_answer to num1 + num2
    if user_answer == num1 + num2:
#shows the user if its correct
        print("Correct!")
#ends the program
        break
##else keeps the loop going
    else:

        print("Incorrect!")
