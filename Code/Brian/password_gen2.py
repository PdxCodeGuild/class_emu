# password_gen2.py
import random
import string
print("Let's create a secure password! ")
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&()*+,-./:;<=>?@[]^_`{|}~'
while True:
    length = input('How many characters do you want in your password? ')
    if length.isdigit() and int(length) < 8 or int(length) > 16:
        print('Sorry, the password must be between 8 and 16 characters, please try again: ')
    if length.isdigit() and int(length) > 7 and int(length) < 17:
        break
length = int(length)
password = ''
for c in range(length):
    password += random.choice(characters)
print('Here you go!  Please copy and use the password below. ')
print(password)
