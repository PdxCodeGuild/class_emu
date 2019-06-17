# filename: lab03_v1_grading.py
'''
Lab 3: Grading
Let's convert a number grade to a letter grade, using if and elif statements and comparisons.

Instructions:
Have the user enter a number representing the grade (0-100)
Convert the number grade to a letter grade

Numeric Ranges:
90-100: A
80-89: B
70-79: C
60-69: D
0-59: F
'''

# check if number is between 0 and 100
while True:
    # get user input (0 - 100)
    numeric_grade = input("Enter a number between 0 and 100: ")
    if numeric_grade.isdigit():
        numeric_grade = int(numeric_grade)
        # check that input is between 0 and 100
        if 0 <= numeric_grade <= 100:
        # convert the number grade to a letter grade
        # then, print the result: letter grade
            if 90 <= numeric_grade <= 100:
                print(f"You entered {numeric_grade}. That's an A. Great job!")
            elif 80 <= numeric_grade <= 90:
                print(f"You entered {numeric_grade}. That's a B. Good job!")
            elif 70 <= numeric_grade <= 80:
                print(f"You entered {numeric_grade}. That's a C. Not bad!")
            elif 60 <= numeric_grade <= 70:
                print(f"You entered {numeric_grade}. That's a D. Umm, did you study?!")
            else:
                print(f"You entered {numeric_grade}. That's an F. D'oh!")
            break
    # if input is < 0 or > 100, print error message and let' user try again
    print(f"You entered {numeric_grade}. That's not a number between 0 and 100. ")
