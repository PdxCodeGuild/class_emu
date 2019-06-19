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
        if ones_digit == 0:
            return f"{tens_dict[tens_digit*10]}"
        else:
            return f"{tens_dict[tens_digit*10]} {ones_list[ones_digit]}"

# try a bunch of numbers as input

input_output = [
    (-1, None),
    (0, "zero"),
    (3, "three"),
    (9, "nine"),
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
    (101, None)
]

failed_test_count = 0
for i in range(len(input_output)):
    if run_tests(input_output[i][0]) != input_output[i][1]:
        print(f"{input_output[i][0]}: Fail. Expected Result: {input_output[i][1]} ==> Actual result: {run_tests(input_output[i][0])}")
        failed_test_count += 1
if failed_test_count == 0:
        print("All tests passed.")
