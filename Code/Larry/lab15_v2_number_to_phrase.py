# filename: lab15_v2_number_to_phrase.py
'''
Lab 15: Number to Phrase

Convert a given number into its english representation.
For example: 67 becomes 'sixty-seven'.
Handle numbers from 0-99.

Version 2
Handle numbers from 100-999.
'''

# Get a number to convert via user input
def get_integer(prompt_text):
    error_msg = "That's not a number between 0 - 999. Try again."
    while True:
        try:
            num = int(input(prompt_text))
            if num < 0 or num > 999:
                print(error_msg)
            else:
                return num
        except ValueError:
            print(error_msg)

while True:
    user_number = get_integer("Enter a number between 0 - 999 to convert: ")

    # Define the word equivalent of the numbers
    ones_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'] # 0 - 9
    teens_dict = { # 10 - 19
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen'
    }
    tens_dict = { # 20 - 90
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety'
    }

    # Break the number into tens_digit and ones_digit
    hundreds_digit = user_number // 100
    tens_digit = user_number % 100 // 10
    ones_digit = user_number % 10

    # Print the numeric phrase equivalent
    if 0 <= user_number <= 9: # use ones_list
        print(ones_list[ones_digit])
    elif 10 <= user_number <= 19: # use teens_dict
        print(teens_dict[user_number])
    elif 20 <= user_number <= 99: # use tens_dict & ones_list
        print(f"{tens_dict[tens_digit*10]} {ones_list[ones_digit]}")
    elif 100 <= user_number <= 999: # use tens_dict & ones_list
        if ones_digit == 0 and tens_digit == 0: # if user_number is n00, e.g. 100
            print(f"{ones_list[hundreds_digit]} hundred")
        elif tens_digit == 0 and ones_digit > 0: # if user_number is n0n, e.g. 101
            print(f"{ones_list[hundreds_digit]} hundred {ones_list[ones_digit]}")
        elif tens_digit == 1 and ones_digit == 0: # if user_number is nn0, e.g. 110
            print(f"{ones_list[hundreds_digit]} hundred {teens_dict[tens_digit*10]}")
        elif tens_digit == 1 and ones_digit >= 0: # if user_number is n1n, e.g. 111
            print(f"{ones_list[hundreds_digit]} hundred {teens_dict[tens_digit*10+ones_digit]}")
        elif tens_digit > 1 and ones_digit == 0: # if user_number is nn0, e.g. 120
            print(f"{ones_list[hundreds_digit]} hundred {tens_dict[tens_digit*10]}")
        elif tens_digit == 1 and ones_digit >= 0: # if user_number is n1n, e.g. 121
            print(f"{ones_list[hundreds_digit]} hundred {teens_dict[tens_digit*10+ones_digit]}")
        else:
            print(f"{ones_list[hundreds_digit]} hundred {tens_dict[tens_digit*10]} {ones_list[ones_digit]}")

    try_again = input("Do you want to try again? (yes)(no): ").lower()
    if try_again == "no":
        break
