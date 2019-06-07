# lab06.py

# pulls information from a sys folder
import random
# pulls information from a sys folder
import string
# pattern_list is a user-created label/variable accessing string.ascii_letters
pattern_list = string.ascii_letters
# length is a user-created label.  "input" asks the user something, and will print to the screen
length = input("How long do you want your password to be? ")
# "int" turns whats in parenthesis(the number given by the user which is a string) into a number
length = int(length)
# "" creates an empty string to be filled
password = ""
#assigns a random choice from the pattern list to the number chosen
for num in range(length):
    password += random.choice(pattern_list)

print(password)
