# lab15_number_to_phrase_V2.py
'''
** Version 2 **

Handle numbers from 100-999.

'''
zero_to_nine = ('Zero One Two Three Four Five Six Seven Eight Nine').split() # defines variable as string and .split splits the string into a list Note: Defaults to split at white'space'
ten_to_nineteen = ('Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen').split()
tens = ('Nonesy Nonesy Twenty Thirty Fourty Fifty Sixty Seventy Eighty Ninety').split()

while True:
    user_input = int(input('What number would you like to convert to its english representation? ')) # prompts user for input and converts it to integer
    if user_input < 0 or user_input > 999: # if/or statment to determine if the number is valid
        print("That number is invalid.  Please enter a number between: 0 and 999. ") # if the above is True, prints statement.
    else:
        break
def up_to_tens(num): # defines function for 0 to 99
    if num < 10: # if number is less than 10, below code runs
        return zero_to_nine[num] # if the above is True, returns value
    elif num < 20: # if number is less than 20 but greater than 9, code below runs
        return ten_to_nineteen[num - 10] # if the above is True, returns value Note: -10 allows value to start at index [0]
    elif num < 100: # if number is less than 100 and greater than 19, code below runs
        tens_number = num // 10 # floor division breaks the number down to tens
        ones_number = num % 10 # modulus gives the remainder to be processed by ones
        if ones_number == 0: # if True, code below runs
            return tens[tens_number] # if the above is True, returns value
        else: # if the above is False, below code runs
            return tens[tens_number] + '-' + zero_to_nine[ones_number] # if the above is True, returns values concatenated w/hyphen in the middle

def hundreds_nums(num): # defines function for 100's with remainder to be processed by up_to_tens function
        tens_number = num % 100 # modulus gives the remainder to be processed by up_to_tens later
        hundreds_number = num // 100 # floor division breaks the number down to hundreds
        hundreds_statement = zero_to_nine[hundreds_number] + '-Hundred' # creates the hundreds statement from zero_to_nine plus hyphen and word Hundred
        return hundreds_statement + ' ' + up_to_tens(tens_number) # returns the Hundreds statment and up_to_tens nunmber with a space in between

if user_input < 100: # if True, code below runs
    print(up_to_tens(user_input)) # if above is true, calls function to process user_input and prints it
else: # if the above if statement is False, code below runs
    print(hundreds_nums(user_input)) # if above is true, calls function to process user_input and prints it
