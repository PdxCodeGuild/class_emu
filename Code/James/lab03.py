# lab03.py

# ask the user for their grade
user_grade = input("What grade did you get?: ")
# turns the user grade into a digit
user_grade = int(user_grade)

# looks to see if the user grade is between the numbers given. If it is, it prints the letter score

# if user_grade > 90:
# if 90 < user_grade < 100:

if user_grade in range(90,101):
    print("You got an A")
if user_grade in range(80,90):
    print("You got a B")
if user_grade in range(70,80):
    print("You got a C")
if user_grade in range(60,70):
    print("You got a D")
if user_grade in range(0,60):
    print("You got an F")
