user_Grade = input("Input a grade and I will tell you it's associated letter grade: \n")
user_Grade_num = int(user_Grade)
if user_Grade_num >= 90 and user_Grade_num >= 100:
    print(f"{user_Grade} is equal to an A! Good Job!\n")
elif user_Grade_num >= 80 or user_Grade_num >= 89:
       print(f"{user_Grade} is equal to a B! Nice Work!\n")
elif user_Grade_num >= 70 or user_Grade_num >= 79:
       print(f"{user_Grade} is equal to a C! Keep it Up!\n")
elif user_Grade_num >= 60 or user_Grade_num >= 69:
       print(f"{user_Grade} is equal to a D! Next Time!\n")