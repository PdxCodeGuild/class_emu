import random
password_Length = input("How many characters would you like your password to be? \n")
password_Length = int(password_Length)
int_Counter = 0
random_choice = 'abcdefhijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
password = ''
while int_Counter < password_Length:
    password += random.choice(random_choice)
    int_Counter += 1

print(password)