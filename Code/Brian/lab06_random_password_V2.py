# lab06_random_password_V2.py
import random #imports the random module to be used in random number and word generation
print("Let's create a secure password! ")
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&()*+,-./:;<=>?@[]^_`{|}~' #string of all characters for use in the password
while True: #adding while loop for use to determine # of characters and limit them between 8 and 16 characters
    length = input('How many characters do you want in your password? ') #asks user for input
    if length.isdigit() and int(length) < 8 or int(length) > 16: #checks if the users input is a digit and if that digit is outside 8 and 16 characters
        print('Sorry, the password must be between 8 and 16 characters, please try again: ') #if not 8 - 16, prints this message
    elif length.isdigit() and int(length) > 7 and int(length) < 17: #checks if the users input is a digit and if that digit is between 8 and 16 characters
        break
length = int(length) #converts length to an interger
password = '' #empty string to define password and to fill it up with random characters
for chars in range(length): #sets up the range for random generation below
    password += random.choice(characters) #adds the random charachters to 8 by incrementing + 1
print('Here you go!  Please copy and use the password below. ') #prints the message
print(password) #prints the random characters to complete the password
