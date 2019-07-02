# filename: lab03_v2_grading.py
'''
Lab 3: Grading

Let's convert a number grade to a letter grade, using if and elif statements and comparisons.

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
    numeric_grade = input("Enter a number between 0 and 100: ")
    if numeric_grade.isdigit(): # validate input: if input is < 0 or > 100, print error message & let user try again
        numeric_grade = int(numeric_grade)  # convert input to integer
        if 0 <= numeric_grade <= 100:       # check that input is between 0 and 100
            # convert the number grade to a letter grade, then print the result: letter grade
            plus_minus = '' # base value for string
            if numeric_grade % 10 >= 7:         # use modulus % to get the ones-digit
                plus_minus = '+'                # set plus_minus equal to plus (+)
            elif numeric_grade % 10 <= 2:       # use modulus % to get the ones-digit
                plus_minus = '-'                # set plus_minus equal to minus (-)
            if 90 <= numeric_grade <= 100:      # if numeric_grade is in the range, print the letter grade
                    print(f"You entered {numeric_grade}. That's an A{plus_minus}. Great job!")
            elif 80 <= numeric_grade <= 90:
                    print(f"You entered {numeric_grade}. That's a B{plus_minus}. Good job!")
            elif 70 <= numeric_grade <= 80:
                    print(f"You entered {numeric_grade}. That's a C{plus_minus}. Not bad!")
            elif 60 <= numeric_grade <= 70:
                    print(f"You entered {numeric_grade}. That's a D{plus_minus}. Umm, did you study?!")
            else:                               # if numeric_grade is <= 59
                print(f"You entered {numeric_grade}. That's an F. D'oh!")
            break
    print(f"You entered {numeric_grade}. That's not a number between 0 and 100. ")
