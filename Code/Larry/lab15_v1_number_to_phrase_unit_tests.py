# filename: lab15_v1_number_to_phrase_unit_tests.py
'''
Lab 15: Number to Phrase - UNIT TESTS

Convert a given number into its english representation.
For example: 67 becomes 'sixty-seven'.
Handle numbers from 0-99.

Hint: you can use modulus to extract the ones and tens digit.
| x = 67
| tens_digit = x//10
| ones_digit = x%10

Hint 2: use the digit as an index for a list of strings.
'''

def run_tests(user_number):

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
    tens_digit = user_number // 10
    ones_digit = user_number % 10

    # Return the numeric phrase equivalent
    if 0 <= user_number <= 9: # use ones_list
        return ones_list[ones_digit] # add +1 to intentionally break the unit test
    elif 10 <= user_number <= 19: # use teens_dict
        return teens_dict[user_number]
    elif 20 <= user_number <= 99: # use tens_dict & ones_list
        return f"{tens_dict[tens_digit*10]} {ones_list[ones_digit]}"

# try a bunch of numbers as input
if run_tests(3) == "three":
    print("3: Pass")
else:
    print(f"3: Fail. Expected Result: 'three' ==> Actual result: '{run_tests(3)}'")

if run_tests(15) == "fifteen":
    print("15: Pass")
else:
    print(f"15: Fail. Expected Result: 'fifteen' ==> Actual result: '{run_tests(15)}'")

if run_tests(21) == "twenty one":
    print("21: Pass")
else:
    print(f"21: Fail. Expected Result: 'twenty one' ==> Actual result: '{run_tests(21)}'")

if run_tests(99) == "ninety nine":
    print("99: Pass")
else:
    print(f"99: Fail. Expected Result: 'ninety nine' ==> Actual result: '{run_tests(99)}'")

if run_tests(101) == None:
    print("101: Pass")
else:
    print(f"101: Fail. Expected Result: 'None' ==> Actual result: '{run_tests(101)}'")
