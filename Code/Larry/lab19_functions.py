# filename: lab19_functions.py
'''
This file contains one function: run_tests().
    • run_tests() is for the units tests embedded in the bottom of the lab 15 solutions.
    • TODO: add the input section from v1 and v1 of the labs, if time allows.
'''

'''
#################
### RUN TESTS ###
#################

This function takes two parameters: user input (list of pokers cards) & expected output
from a list of tuples,

input_output => [(test number, [list of poker cards], expected result string)]
e.g.
### v1 - Ace is always worth 1 ###
# (1, ['A', '8', '2'], '11 Hit'),            # 11
# (2, ['K', '3', '5'], '18 Stay'),           # 18
# (3, ['J', 'Q', 'A'], '21 Blackjack!'),     # 21
# (4, ['9', '7', '6'], '22 Already busted!') # 22

### v2 - Ace can be worth 1 or 11 ###
# (1, ['2', '4', '8'], '14 Hit'),            # 14
# (2, ['A', 'A', 'A'], '13 Hit'),            # 13, three As (11+1+1) - lines 40-44
# (3, ['A', 'A', '4'], '16 Hit'),            # 16, two As (11+1) - lines 35-39
# (4, ['K', '3', '5'], '18 Stay'),           # 18
# (5, ['J', 'Q', 'A'], '21 Blackjack!'),     # 21, one A (1) - lines 30-34
# (6, ['A', '8', '2'], '21 Blackjack!'),     # 21, one A (11) - lines 30-34
# (7, ['9', '7', '6'], '22 Already busted!') # 22

and submits each set of 3-cards to the function-under-test,
then returns the result of comparing the actual output & expected output.

If any tests fail, a descriptive message is returned and printed.
Otherwise, "All tests passed." is returned and printed.
'''

def run_tests(input_output, function_name):
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
