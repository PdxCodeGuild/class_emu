user_Grade = input("Input a grade and I will tell you it's associated letter grade: \n")
user_Grade_num = int(user_Grade)
def is_plus(grade_num):
    if grade_num % 10 > 5:
        letter_grade = '+'
    elif grade_num % 10 == 5:
        letter_grade = ' '
    else:
        letter_grade = '-'   
    return letter_grade             

letter_grade = is_plus(user_Grade_num)
if user_Grade_num >= 90 and user_Grade_num <= 100:
    print(f"{user_Grade} is equal to an A{letter_grade}! Good Job!\n")
elif user_Grade_num >= 80 or user_Grade_num <= 89:
    print(f"{user_Grade} is equal to a B{letter_grade}! Nice Work!\n")
elif user_Grade_num >= 70 or user_Grade_num <= 79:
    print(f"{user_Grade} is equal to a C{letter_grade}! Keep it Up!\n")
elif user_Grade_num >= 60 or user_Grade_num <= 69:
    print(f"{user_Grade} is equal to a D{letter_grade}! Next Time!\n")
