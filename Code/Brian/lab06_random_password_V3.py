# lab06_random_password_V3.py
'''
** Version 3 (optional) **

Ask the user for how many lowercase letters, uppercase letters, numbers, and special characters they'd like in their password.
Generate a password accordingly.
'''
import random #imports the random module to be used in random number and word generation
print("Let's create a secure password using each type of character! ")
lower_characters = 'abcdefghijklmnopqrstuvwxyz' #string of all lowercase characters for use in the password
upper_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #string of all uppercase characters for use in the password
numbers_characters = '0123456789' #string of all number characters for use in the password
special_characters = '!"#$%&()*+,-./:;<=>?@[]^_`{|}~' #string of all special characters for use in the password
length_lower = input('How many lowercase characters do you want in your password? ') #asks user for input
length_upper = input('How many uppercase characters do you want in your password? ') #asks user for input
length_numbers = input('How many numbers do you want in your password? ') #asks user for input
length_special = input('How many special characters do you want in your password? ') #asks user for input
length_lower = int(length_lower) #converts to an interger
length_upper = int(length_upper) #converts to an interger
length_numbers = int(length_numbers) #converts to an interger
length_special = int(length_special) #converts to an interger
password = '' #empty string to define password and to fill it up with random characters
for chars in range(length_lower): #sets up the range for random generation below
    password += random.choice(lower_characters) #adds the random characters to user input by incrementing + 1
for chars in range(length_upper): #sets up the range for random generation below
    password += random.choice(upper_characters) #adds the random characters to user input by incrementing + 1
for chars in range(length_numbers): #sets up the range for random generation below
    password += random.choice(numbers_characters) #adds the random characters to user input by incrementing + 1
for chars in range(length_special): #sets up the range for random generation below
    password += random.choice(special_characters) #adds the random characters to user input by incrementing + 1
print('Here you go!  Please copy and use the password below. ') #prints the message
print(password) #prints the random characters to complete the password
