# filename: lab17_functions.py
'''
This file contains one function: run_tests().
    • run_tests() is for the units tests embedded in the bottom of the lab 15 solutions.
'''

'''
### RUN TESTS ###
This function takes two parameters: user input (list of pokers cards) and expected output
from a list of tuples.
input_output = boolean(result), first string, second string

e.g.
(True, 'nude dragons', 'soundgarden'),          # input includes spaces
(True, 'Brag', 'Grab!'),                        # input includes capital letters and punctuation
(False, 'The Morse Code', 'Here comes dots'),   # length mismatch
(False, 'Angel', 'Gleam'),                      # letters don't match

If any tests fail, a descriptive message is returned and printed.
Otherwise, "All tests passed." is returned and printed.
'''
### RUN TESTS ###
def run_tests(input_output, function_name):
    failed_test_count = 0
    failed_test_msg = ''
    for i in range(len(input_output)):
        function_output = function_name(input_output[i][1], input_output[i][2])
        expected_output = input_output[i][0]
        if function_output != expected_output:
            failed_test_count += 1
            failed_test_msg += f"\nInput: {input_output[i][1], input_output[i][2]}\nFail. Expected Result: {expected_output} ==> Actual result: {function_output}\n"
    if failed_test_count != 0:
        return failed_test_msg
    if failed_test_count == 0:
        return "All tests passed."
