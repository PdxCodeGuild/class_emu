# filename: lab_functions.py
'''
This file contains two Run Tests functions: run_tests_1() & run_tests_2().
    • run_tests_1() is for the Anagram, Blackjack Advice, & Credit Card Validation units tests.
    • run_tests_2() is for the Palindrome units.
    • TODO: add the input section(s) from the labs, if time allows.
'''

'''
#######################################
### RUN TESTS - One-parameter input ###
#######################################

This function takes two parameters, user input & expected output (list of tuples) and function_name,
submits each test_input(string, strings, or tuple) to the function-name under-test, then
returns the result of comparison: actual output (Boolean or string) vs. expected output (Boolean or string).

e.g. Anagram (lab 17)
# input_output = [(string, expected_output] # 1-parameter input
# (1, 'racecar', True),    # base case (no capital letters, spaces, or non-ascii letters)
# (2, 'Race car', True),   # capital letters are converted to lowercase
# (3, 'racecar!', True),   # non-ascii letters are ignored
# (4, 'racecar', False)]   # the second 'a' and 'o' are transposed

e.g. Blackjack Advice (lab 19)
# input_output => [(test number, [list of poker cards], expected result string)] # 1-parameter input
### v1 - Ace is always worth 1 ###
# (1, ['A', '8', '2'], '11 Hit'),            # Hit
# (2, ['K', '3', '5'], '18 Stay'),           # Stay
# (3, ['J', 'Q', 'A'], '21 Blackjack!'),     # Blackjack!
# (4, ['9', '7', '6'], '22 Already busted!') # Already busted!

### v2 - Ace can be worth 1 or 11 ###
# (1, ['2', '4', '8'], '14 Hit'),            # Hit
# (2, ['A', 'A', 'A'], '13 Hit'),            # Hit, three As (11+1+1) - lines 40-44
# (3, ['A', 'A', '4'], '16 Hit'),            # Hit, two As (11+1) - lines 35-39
# (4, ['K', '3', '5'], '18 Stay'),           # Stay
# (5, ['J', 'Q', 'A'], '21 Blackjack!'),     # Blackjack!, one A (1) - lines 30-34
# (6, ['A', '8', '2'], '21 Blackjack!'),     # Blackjack!, one A (11) - lines 30-34
# (7, ['9', '7', '6'], '22 Already busted!') # Already busted!

e.g. Credit Card Valdation
# input_output => [(test number, [list of credit card numbers], expected result string)] # 1-parameter input
# (1, "5392799316110230", True),  # MasterCard
# (2, "4971023049709545", True)   # Visa

If any tests fail, a descriptive message is returned and printed.
Otherwise, "All tests passed." is returned and printed.
'''

def run_tests_1(input_output, function_name):
    failed_test_count = 0
    failed_test_msg = ''
    for i in range(len(input_output)):
        test_number = input_output[i][0]
        test_input = input_output[i][1]
        function_output = function_name(test_input)
        expected_output = input_output[i][2]
        if function_output != expected_output:
            failed_test_count += 1
            failed_test_msg += f"\nTest #{test_number} - Failed\nInput: {test_input}\n==> Expected Result: {expected_output}\n==>   Actual result: {function_output}\n"
    if failed_test_count != 0:
            return failed_test_msg
    if failed_test_count == 0:
            return "All tests passed."

'''
#######################################
### RUN TESTS - Two-parameter input ###
#######################################

This function takes two parameters, user input & expected output (list of tuples) and function_name,
submits first_string and second_string to the function-name under-test, then
returns the result of comparison: actual output vs. expected output.

e.g. Palindrome (lab 17)
# input_output = [(test_number, first string, second string, expected_output)] # 2-parameter input
# (1, 'nude dragons', 'soundgarden', True),         # input includes spaces
# (2, 'Brag', 'Grab!', True),                       # input includes capital letters and punctuation
# (3, 'The Morse Code', 'Here comes dots', False),  # length mismatch
# (4, 'Angel', 'Gleam', False)]                     # letters don't match

If any tests fail, a descriptive message is returned and printed.
Otherwise, "All tests passed." is returned and printed.
'''

def run_tests_2(input_output, function_name):
    failed_test_count = 0
    failed_test_msg = ''
    for i in range(len(input_output)):
        test_number = input_output[i][0]
        first_string = input_output[i][1]
        second_string = input_output[i][2]
        function_output = function_name(first_string, second_string)
        expected_output = input_output[i][3]
        if function_output != expected_output:
            failed_test_count += 1
            failed_test_msg += f"\nTest #{test_number} - Failed\nInput: {first_string, second_string}\n==> Expected Result: {expected_output}\n==>   Actual result: {function_output}\n"
    if failed_test_count != 0:
        return failed_test_msg
    if failed_test_count == 0:
        return "All tests passed."
