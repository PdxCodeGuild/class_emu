# filename: lab15_unit_test.py
'''
This function takes two parameters: input (a number) and expected output
from a list of tuples.
e.g.
[(7, "seven"), (17, "seventeen"), (77, "seventy seven")]            # lab 15, v1
((107, "one hundred seven"), (777, "seven hundred seventy seven")]  # lab 15, v2
[(7, "VII"), (17, "XVII"), (77, "LXXVII"), (777, "DCCLXXVII")]      # lab 15, v3
'''

def run_tests(input_output, lab_name):
    failed_test_count = 0
    for i in range(len(input_output)):
        input = lab_name(input_output[i][0])
        expected_output = input_output[i][1]
        if input != expected_output:
            return f"{input}: Fail. Expected Result: {expected_output} ==> Actual result: {input}"
            failed_test_count += 1
    if failed_test_count == 0:
            return "All tests passed."
