# filename: lab03_v1_grading.py
'''
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
    # numeric_grade = int(input("Enter a number between 0 and 100: "))
    numeric_grade = input("Enter a number between 0 and 100: ")
    if numeric_grade.isdigit():
        numeric_grade = int(numeric_grade)
        # check that input is between 0 and 100
        if 0 <= numeric_grade <= 100:
        # convert the number grade to a letter grade
        # then, print the result: letter grade
            if numeric_grade in range(90,101): #the upper bound is +1 (101 vs 100) since it's not included
                print(f"You entered {numeric_grade}. That's an A. Great job!")
            elif numeric_grade in range(80,90): #the upper bound is +1 (90 vs 89) since it's not included
                print(f"You entered {numeric_grade}. That's a B. Good job!")
            elif numeric_grade in range(70,80): #the upper bound is +1 (80 vs 79) since it's not included
                print(f"You entered {numeric_grade}. That's a C. Not bad!")
            elif numeric_grade in range(60,70): #the upper bound is +1 (70 vs 69) since it's not included
                print(f"You entered {numeric_grade}. That's a D. Umm, did you study?!")
            else:
                print(f"You entered {numeric_grade}. That's an F. D'oh!")
            break
    # if input is < 0 or > 100, print error message and let' user try again
    print(f"You entered {numeric_grade}. That's not a number between 0 and 100. ")
