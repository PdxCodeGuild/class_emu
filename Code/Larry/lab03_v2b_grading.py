# filename: lab03_v2b_grading.py
'''
Instructions:
Have the user enter a number representing the grade (0-100)
Convert the number grade to a letter grade
Numeric Ranges:
A+ 97–100
A	93–96
A−	90–92
B+	87–89
B	83–86
B−	80–82
C+	77–79
C	73–76
C-	70–72
D+	67–69
D	63–66
D-	60–62
F	0–59
Version 2
Find the specific letter grade (A+, B-, etc).
You can check for more specific ranges using if statements, or use modulus % to get the ones-digit to
set another string to '+', '-', or ' '.
Then you can concatenate that string with your grade string.
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
            # use modulus % to get the ones-digit
            plus_minus = ''
            if numeric_grade % 10 >= 7:
                plus_minus = '+' # set plus_minus equal to plus (+)
            elif numeric_grade % 10 <= 2:
                plus_minus = '-' # set plus_minus equal to minus (-)
            if 90 <= numeric_grade <= 100: #the upper bound is +1 (101 vs 100) since it's not included
                    print(f"You entered {numeric_grade}. That's an A{plus_minus}. Great job!")
            elif numeric_grade in range(80,90): #the upper bound is +1 (90 vs 89) since it's not included
                    print(f"You entered {numeric_grade}. That's a B{plus_minus}. Good job!")
            elif numeric_grade in range(70,80): #the upper bound is +1 (80 vs 79) since it's not included
                    print(f"You entered {numeric_grade}. That's a C{plus_minus}. Not bad!")
            elif numeric_grade in range(60,70): #the upper bound is +1 (70 vs 69) since it's not included
                    print(f"You entered {numeric_grade}. That's a D{plus_minus}. Umm, did you study?!")
            else:
                print(f"You entered {numeric_grade}. That's an F. D'oh!")
            break
    # if input is < 0 or > 100, print error message and let' user try again
    print(f"You entered {numeric_grade}. That's not a number between 0 and 100. ")
