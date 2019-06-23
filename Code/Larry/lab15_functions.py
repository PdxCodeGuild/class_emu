# filename: lab15_functions.py
'''
This file contains three functions: get_integer(), try_again(), and run_tests().
    • get_integer() is for getting and validating the user input (integer).
    • try_again() is for prompting the user to continue or exit the program.
    • run_tests() is for the units tests embedded in the bottom of the lab 15 solutions.
'''

'''
###################
### GET INTEGER ###
###################

This function takes two parameters: user input prompt text (string) and upper_range_limit (integer),
and returns a integer between 0 and the upper_range_limit.
e.g.
prompt_text = "Enter a number between 0 - 99 to convert: "
'''

def get_integer(prompt_text, upper_range_limit):
    error_msg = f"That's not a number between 0 - {upper_range_limit}. Try again."
    while True:
        try:
            num = int(input(prompt_text))
            if num < 0 or num > upper_range_limit:
                print(error_msg)
            else:
                return num
        except ValueError:
            print(error_msg)

'''
#################
### TRY AGAIN ###
#################

This function takes one parameter: user input prompt text (string),
and returns True if the user types "no".
e.g.
prompt_text = "Do you want to try again? (yes)(no): "
'''
def try_again(prompt_text):
    if input(prompt_text).lower() == "no":
        return True

'''
#################
### RUN TESTS ###
#################

This function takes two parameters: user input (list of tuples) and function_name,
submits each integer to the function-name under-test, then
returns the result of comparison: actual output vs. expected output.

e.g.
input_output = [(integer, cardinal number)] or [(integer, Roman numeral)]
[(7, "seven"), (17, "seventeen"), (77, "seventy seven")]            # lab 15, v1
[(107, "one hundred seven"), (777, "seven hundred seventy seven")]  # lab 15, v2
[(7, "VII"), (17, "XVII"), (77, "LXXVII"), (777, "DCCLXXVII")]      # lab 15, v3

If any tests fail, a descriptive message is returned and printed.
Otherwise, "All tests passed." is returned and printed.
'''

def run_tests(input_output, function_name):
    failed_test_count = 0
    failed_test_msg = ''
    for i in range(len(input_output)):
        function_output = function_name(input_output[i][0])
        expected_output = input_output[i][1]
        if function_output != expected_output:
            failed_test_count += 1
            failed_test_msg += f"\n{input_output[i][0]}: Fail.\nExpected Result: {expected_output} ==> Actual result: {function_output}\n"
    if failed_test_count != 0:
            return failed_test_msg
    if failed_test_count == 0:
            return "All tests passed."
