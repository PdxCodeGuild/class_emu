# lab03_grading_V2.py
'''
** Version 2 **

Find the specific letter grade (A+, B-, etc).
You can check for more specific ranges using if statements, or use modulus % to get the ones-digit to set another string to '+', '-', or ' '.
Then you can concatenate that string with your grade string.
'''
import random # imports random for use to randomize things
user_grade = input("What was your score on the test?: ") # asks user to enter test score, is string
user_grade = int(user_grade) # converts string to interger
if user_grade >= 97 % 100:
    print("Your grade is: A+")
elif user_grade >= 94 % 100:
    print("Your grade is: A")
elif user_grade >= 90 % 100:
    print("Your grade is: A-")
elif user_grade >= 87 % 100:
    print("Your grade is: B+")
elif user_grade >= 84 % 100:
    print("Your grade is: B")
elif user_grade >= 80 % 100:
    print("Your grade is: B-")
elif user_grade >= 77 % 100:
    print("Your grade is: C+")
elif user_grade >= 74 % 100:
    print("Your grade is: C")
elif user_grade >= 70 % 100:
    print("Your grade is: C-")
elif user_grade >= 67 % 100:
    print("Your grade is: D+")
elif user_grade >= 64 % 100:
    print("Your grade is: D")
elif user_grade >= 60 % 100:
    print("Your grade is: D-")
elif user_grade <= 59 % 100:
    print("Your grade is: F")
