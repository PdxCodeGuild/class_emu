# filename: lab17_functions.py
'''
This file contains one function: run_tests().
    • run_tests() is for the units tests embedded in the bottom of the lab 15 solutions.
    • TODO: add the input section from v1 and v1 of the labs, if time allows.
'''

'''
###########################
### RUN TESTS - Anagram ###
###########################

This function takes two parameters, user input & expected output (list of tuples) and function_name,
submits first_string and second_string to the function-name under-test, then
returns the result of comparison: actual output vs. expected output.

e.g.
input_output = [(expected_output(boolean)), first string, second string)]
[(True, 'nude dragons', 'soundgarden'),         # input includes spaces
(True, 'Brag', 'Grab!'),                        # input includes capital letters and punctuation
(False, 'The Morse Code', 'Here comes dots'),   # length mismatch
(False, 'Angel', 'Gleam')]                      # letters don't match

If any tests fail, a descriptive message is returned and printed.
Otherwise, "All tests passed." is returned and printed.
'''

def run_tests(input_output, function_name):
    failed_test_count = 0
    failed_test_msg = ''
    for i in range(len(input_output)):
        first_string = input_output[i][1]
        second_string = input_output[i][2]
        function_output = function_name(first_string, second_string)
        expected_output = input_output[i][0]
        if function_output != expected_output:
            failed_test_count += 1
            failed_test_msg += f"\nInput: {first_string, second_string}\nFail. Expected Result: {expected_output} ==> Actual result: {function_output}\n"
    if failed_test_count != 0:
        return failed_test_msg
    if failed_test_count == 0:
        return "All tests passed."

'''
##############################
### RUN TESTS - Palindrome ###
##############################

This function takes two parameters, user input & expected output (list of tuples) and function_name,
submits each test_input(string) to the function-name under-test, then
returns the result of comparison: actual output vs. expected output.

e.g.
input_output = [(expected_output), test_input(string)]
[(True, 'racecar'),   # base case (no capital letters, spaces, or non-ascii letters)
(True, 'Race car'),   # capital letters are converted to lowercase
(True, 'racecar!'),   # non-ascii letters are ignored
(False, 'racecar')]   # the second 'a' and 'o' are transposed

If any tests fail, a descriptive message is returned and printed.
Otherwise, "All tests passed." is returned and printed.
'''

def run_tests_p(input_output, function_name):
    failed_test_count = 0
    failed_test_msg = ''
    for i in range(len(input_output)):
        test_input = input_output[i][1]
        function_output = function_name(test_input)
        expected_output = input_output[i][0]
        if function_output != expected_output:
            failed_test_count += 1
            failed_test_msg += f"\nInput: {test_input}\nFail. Expected Result: {expected_output} ==> Actual result: {function_output}\n"
    if failed_test_count != 0:
        return failed_test_msg
    if failed_test_count == 0:
        return "All tests passed."
