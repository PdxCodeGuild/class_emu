# addition_tester.py
import random
num1 = random.randint(0, 5)
num2 = random.randint(0, 5)
print(f"what is {num1} + {num2}?")
while True:
    user_answer = input("what is your answer?: ")
    user_answer = int(user_answer)
    if user_answer == num1 + num2:
        print("Correct!")
        break
    else:
        print("Incorrect!")
