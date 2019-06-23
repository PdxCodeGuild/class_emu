# Lab_03_Grading_V1.py
'''
Lab 3: Grading

** Version 1 **

Let's convert a number grade to a letter grade, using if and elif statements and comparisons.

Concepts Covered
input, print
type conversion (str to int)
comparisons (< <= > >=)
if, elif, else
Instructions
Have the user enter a number representing the grade (0-100)
Convert the number grade to a letter grade
Numeric Ranges
90-100: A
80-89: B
70-79: C
60-69: D
0-59: F
'''
import random # imports random for use to randomize things
user_grade = input("What was your score on the test?: ") # asks user to enter test score, is string
user_grade = int(user_grade) # converts string to interger
if user_grade >= 90 and user_grade <= 100: # if statement checks to see if the interger is between 90 and 100
    print("You got an A, Good Job!") # if the user enters between 90 and 100, prints this text.
elif user_grade >= 80:
    print("You got B, Good Job!")
elif user_grade >= 70:
    print("You got C, Room for improvement")
elif user_grade >= 60:
    print("You got D, This is not good")
elif user_grade >= 0:
    print("You got an F, See the teacher after class")
user_curious = input("Do you want to see how you did compared to your rival?: ").lower()
if user_curious == 'yes': # checks to see if the user said yes.  (.lower() converts the user input to lowercase)
    print(f"Your rival scored a {random.randint(0,100)}") # random.randit(0,100) randomly enters a interger between 0 and 100.
if user_curious == 'no':
    print("Not competitive eh?  No worries, have a great day!")
