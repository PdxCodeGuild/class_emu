# lab15_number_to_phrase_V1.py
'''
Lab 15: Number to Phrase

** Version 1 **

Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

Hint: you can use modulus to extract the ones and tens digit.

x = 67
tens_digit = x//10
ones_digit = x%10
Hint 2: use the digit as an index for a list of strings.

'''
zero_to_nine = ('Zero One Two Three Four Five Six Seven Eight Nine').split() # defines variable as string and .split splits the string into a list Note: Defaults to split at white'space'
ten_to_nineteen = ('Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen').split()
tens = ('Nonesy Nonsey Twenty Thirty Fourty Fifty Sixty Seventy Eighty Ninety').split()
user_input = int(input('What number would you like to convert to its english representation? '))

def nums_0_to_9(num): # defines function for 0 to 9
    if user_input < 10 and user_input >= 0: # if this is true, code will run
        return zero_to_nine[user_input] # returns the index number based in user input

def nums_10_to_19(num):
    if user_input >= 10:
        return ten_to_nineteen[user_input - 10] # -10 allows it to start at index 0

def tens_nums(num):
    if user_input >= 20:
        tens_number = user_input // 10 # floor division breaks the number down to tens
        ones_number = user_input % 10 # modulus gives the remainder to be processed by ones
        if ones_number == 0: # if true, below code runs
            return tens[tens_number] # returns tens number even
        else: # if above if statement is false, code below runs
            return tens[tens_number] + '-' + zero_to_nine[ones_number] # takes into account the tens number, add - and then accounts for ones number

if user_input < 0 or user_input > 99: # if true, code below runs
    print("That number is invalid.  Please enter a number between: 0 and 99. ") # if above true, prints statement
elif user_input < 10:
    print(nums_0_to_9(user_input)) # prints user_input based on the parameters of the defined function and applies it
elif user_input >= 10 and user_input <=19:
    print(nums_10_to_19(user_input))
elif user_input >= 20:
    print(tens_nums(user_input))
