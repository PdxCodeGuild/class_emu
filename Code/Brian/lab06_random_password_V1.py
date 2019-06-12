# lab06_random_password_V1.py
import random #imports the random module to be used in random number and word generation
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&()*+,-./:;<=>?@[]^_`{|}~' #string of all characters for use in the password
while True: #needed to add a while loop per lab instructions
    length = 8 #established the length of password I wanted
    if length > 7 and length < 9: #determines a truth to the 8 characters I desired
        break #breaks out of the loop
length = int(length) #converts length to an interger
password = '' #empty string to define password and to fill it up with random characters
for chars in range(length): #sets up the range for random generation below
    password += random.choice(characters) #adds the random charachters to 8 by incrementing + 1
print('Here you go!  Please copy and use the password below. ') #prints the message
print(password) #prints the random characters to complete the password
