# lab15_number_to_phrase_V4.py

'''
** Version 4 (optional) **

Convert a time given in hours and minutes to a phrase.

'''
# NOTE: Utilizing code from last lab - up_to_tens
zero_to_nine = ('Zero One Two Three Four Five Six Seven Eight Nine').split() # defines variable as string and .split splits the string into a list Note: Defaults to split at white'space'
ten_to_nineteen = ('Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen').split()
tens = ('Nonesy Nonesy Twenty Thirty Fourty Fifty Sixty Seventy Eighty Ninety').split()

while True: # creates a while loop for user input to ensure the correct input is given NOTE: for 3 separate inputs here and below
    user_input_hour = int(input("Enter the first part of the time in hours 1 to 12: "))
    if user_input_hour > 12 or user_input_hour < 1:
        print("Sorry, that number is not valid, please enter a number between 1 and 12. ")
    else:
        break
while True:
    user_input_minutes = int(input("Now enter the second part of the time in minutes 0 to 59: "))
    if user_input_minutes > 59 or user_input_minutes < 0:
        print("Sorry, that number is not valid, please enter a number between 0 and 59. ")
    else:
        break
while True:
    user_input_am_or_pm = input("Is that time 'AM' or 'PM'? ").upper()
    if user_input_am_or_pm == 'PM' or user_input_am_or_pm == 'AM':
        break
    else:
        print("Sorry, that is not valid, please enter either 'AM' or 'PM'. ")

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

if user_input_hour < 100: # if True, code below runs
    print(up_to_tens(user_input_hour) + ' ' + up_to_tens(user_input_minutes) + ' ' + user_input_am_or_pm) # if above is true, calls function to process user inputs for hr and min and prints it with am or pm at the end
