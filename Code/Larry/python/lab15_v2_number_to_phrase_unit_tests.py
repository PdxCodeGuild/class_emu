# filename: lab15_v2_number_to_phrase_unit_tests.py
'''
Lab 15: Number to Phrase - FUNCTION w/ UNIT TESTS

Convert a given number into its english representation.
For example: 67 becomes 'sixty-seven'.
Handle numbers from 0-99.

Version 2
Handle numbers from 100-999.
'''

def get_word_number2(user_number):

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
        return ones_list[ones_digit]
    elif 10 <= user_number <= 19: # use teens_dict
        return teens_dict[user_number]
    elif 20 <= user_number <= 99: # use tens_dict & ones_list
        if ones_digit == 0:
            return f"{tens_dict[tens_digit*10]}"
        else:
            return f"{tens_dict[tens_digit*10]} {ones_list[ones_digit]}"
    elif 100 <= user_number <= 999: # use tens_dict & ones_list
        if ones_digit == 0 and tens_digit == 0: # if user_number is n00, e.g. 100
            return f"{ones_list[hundreds_digit]} hundred"
        elif tens_digit == 0 and ones_digit > 0: # if user_number is n0n, e.g. 101
            return f"{ones_list[hundreds_digit]} hundred {ones_list[ones_digit]}"
        elif tens_digit == 1 and ones_digit == 0: # if user_number is nn0, e.g. 110
            return f"{ones_list[hundreds_digit]} hundred {teens_dict[tens_digit*10]}"
        elif tens_digit == 1 and ones_digit >= 0: # if user_number is n1n, e.g. 111
            return f"{ones_list[hundreds_digit]} hundred {teens_dict[tens_digit*10+ones_digit]}"
        elif tens_digit > 1 and ones_digit == 0: # if user_number is nn0, e.g. 120
            return f"{ones_list[hundreds_digit]} hundred {tens_dict[tens_digit*10]}"
        elif tens_digit == 1 and ones_digit >= 0: # if user_number is n1n, e.g. 121
            return f"{ones_list[hundreds_digit]} hundred {teens_dict[tens_digit*10+ones_digit]}"
        else:
            return f"{ones_list[hundreds_digit]} hundred {tens_dict[tens_digit*10]} {ones_list[ones_digit]}"



###########################################################
### UNIT TESTS ###
###########################################################

# Check (at least) one number from every if/elif conditional
if __name__ == '__main__':

    test_data = [
        (-1, None),
        (0, "zero"),
        (1, "one"),
        (10, "ten"),
        (15, "fifteen"),
        (19, "nineteen"),
        (20, "twenty"),
        (23, "twenty three"),
        (30, "thirty"),
        (31, "thirty one"),
        (40, "forty"),
        (42, "forty two"),
        (50, "fifty"),
        (53, "fifty three"),
        (60, "sixty"),
        (64, "sixty four"),
        (70, "seventy"),
        (75, "seventy five"),
        (80, "eighty"),
        (86, "eighty six"),
        (90, "ninety"),
        (99, "ninety nine"),
        (100, "one hundred"),
        (101, "one hundred one"),
        (110, "one hundred ten"),
        (111, "one hundred eleven"),
        (120, "one hundred twenty"),
        (121, "one hundred twenty one"),
        (145, "one hundred forty five"),
        (200, "two hundred"),
        (259, "two hundred fifty nine"),
        (301, "three hundred one"),
        (436, "four hundred thirty six"),
        (538, "five hundred thirty eight"),
        (605, "six hundred five"),
        (777, "seven hundred seventy seven"),
        (888, "eight hundred eighty eight"),
        (999, "nine hundred ninety nine"),
        (1000, None)
    ]

    from lab15_functions import run_tests

    print(run_tests(test_data, get_word_number2))
