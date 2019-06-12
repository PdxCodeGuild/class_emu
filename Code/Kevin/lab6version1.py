import random
password_Length = input("How many characters would you like your password to be? \n")
password_Length = int(password_Length)
int_Counter = 0
char_Choices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
random_choice = 'abcdefhijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
password = ''
while int_Counter < password_Length:
    print(random.choice(random_choice))
    password += random.choice(random_choice)
    int_Counter += 1

