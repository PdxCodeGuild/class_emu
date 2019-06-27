# lab15_number_to_phrase_V3.py

'''
** Version 3 (optional) **

Convert a number to roman numerals.

'''
num_to_roman_list = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
# defines variable as a list of keys and values


while True: # creates a loop
    user_input = int(input("What number, between 1 and 4999, would you like to convert to roman numerals?: ")) # prompts user for input and converts to integer
    if user_input <= 0 or user_input >= 5000: # if True, the below code runs
        print("Sorry that is not a valid number, please enter a number between 1 and 4999.") # if above is True, prints statement and starts back at top of loop
    else: # if the above is false, code below runs
        break # if number is valid, 1 to 4999, breaks out of the loop

def num_to_roman(num): # defines a function called num_to_roman with parameter num
    roman = '' # defines variable roman as an empty list to be populated
    while num > 0: # creates a while loop as long as the number is greater than 0 and less than 5000 based on above code
        for key, value in num_to_roman_list: # creates for loop with keys and values from above list
            while num >= key: # while loop stating if the num(user_input) is equal or greater than the key, below code runs
                roman += value # if above is true, adds the value of num(user_input) from the associated key to the roman string
                num -= key # and removes the key value from num(user_input)
    return roman # after all iterations of the list, based on num(user_input), returns the roman string

print(num_to_roman(user_input)) # calls the function to process the user_input and prints the result
