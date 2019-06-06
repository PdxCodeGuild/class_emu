# filename: addition_tester.py
import random
num1 = random.randint(1, 6)
num2 = random.randint(1, 6)
print(f"What is {num1} + {num2}? ")
while True:
    user_answer = int(input("Type your answer: "))
    if user_answer == num1 + num2:
        print ("Correct")
        break
    else:
        print("Incorrect")

# version 2 WITHOUT 'else' statement
import random
num1 = random.randint(1, 6)
num2 = random.randint(1, 6)
print(f"What is {num1} + {num2}? ")
while True:
    user_answer = int(input("Type your answer: "))
    if user_answer == num1 + num2:
        print ("Correct")
        break
    # else:
    #   print("Incorrect")
    print("Incorrect")
