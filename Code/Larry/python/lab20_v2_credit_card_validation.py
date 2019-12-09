# filename: lab20_v2_credit_card_validation.py
'''
Lab 20: Credit Card Validation

Let's write a function which returns whether a string containing a credit card number is valid as a boolean.
e.g. credit_card_number = 4556737586899855
+---------------------------------------------------------------------------------------------+
| Steps                                                | Data                                 |
+------------------------------------------------------+--------------------------------------+
| 1. Convert the input string into a list of ints      | 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5      |
| 2. Slice off the last digit. That is the check digit | 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5        |
| 3. Reverse the digits.                               | 5 8 9 9 8 6 8 5 7 3 7 6 5 5 4        |
| 4. Double every other element in the reversed list   | 10 8 18 9 16 6 16 5 14 3 14 6 10 5 8 |
| 5. Subtract nine from numbers over nine              | 1 8 9 9 7 6 7 5 5 3 5 6 1 5 8        |
| 6. Sum all values                                    | 85                                   |
| 7. Take the second digit of that sum                 | 5                                    |
+------------------------------------------------------+--------------------------------------+
| Result: If that matches the check digit, the whole card number is valid.                    |
+---------------------------------------------------------------------------------------------+

V2: Added code to convert strings to int (lines 29-30);
    replaced for loop with list.reverse() (line 32);
    changed [1] to [-1] on line 44
'''

from sys import argv # for using sys.argv e.g. $python filename.py run_tests

def validate_credit_card(cc_number):            #
    numbers = list(cc_number)                   # Convert the input string into a list
    check_digit = numbers.pop()                 # Slice off the last digit, aka. check digit

    for i in range(len(numbers)):               #
        numbers[i] = int(numbers[i])            # Convert list of strings to integers

    numbers.reverse()                           # Reverse the list of numbers

    for i in range(0, len(numbers), 2):         #
        numbers[i] = numbers[i] * 2             # Double every other element in the reversed list

    for i in range(len(numbers)):               #
        if numbers[i] > 9:                      #
            numbers[i] -= 9                     # Subtract 9 from numbers over 9

    total = str(sum(numbers))                   # Add all the numbers and convert to string

    return check_digit == total[-1]            # If ones digit of that sum matches the check digit, returns True

if len(argv) == 1: # only execute these lines 'run_tests' is passed

    # Get user input
    credit_card_number = input("\nEnter a credit card number: ") # Get input, e.g. "4556737586899855"

    # Print the result
    result = validate_credit_card(credit_card_number)
    if result:
        print(f"\n{result}: This is a valid credit card number.\n")
    else:
        print(f"\n{result}: This is not a valid credit card number.\n")

###########################################################
### UNIT TESTS ###
###########################################################

# Check a variety of comparison (with spaces, Capital letters, punctuation)
if len(argv) > 1:
    if argv[1] == 'run_tests':  # argv[1] = first argument after the program name, e.g. py filename.py run_tests

        # source: https://www.getcreditcardnumbers.com/credit-card-generator
        test_data = [
            (1, "4556737586899855", True),   # Lab 20 example
            (2, "4556737586899856", False),  # Lab 20 with check_digit+1
            (3, "378282246310005", True),    # American Express
            (4, "371449635398431", False),   # American Express
            (5, "378734493671000", True),    # American Express Corporate
            (6, "5610591081018250", True),   # Australian BankCard
            (7, "30569309025904", False),    # Diners Club
            (8, "38520000023237", False),    # Diners Club
            (9, "6011111111111117", False),  # Discover
            (10, "6011000990139424", False), # Discover
            (11, "3530111333300000", True),  # JCB
            (12, "3566002020360505", True),  # JCB
            (13, "5555555555554444", False), # MasterCard
            (14, "5105105105105100", True),  # MasterCard
            (15, "5392799316110230", True),  # MasterCard
            (16, "4111111111111111", False), # Visa
            (17, "4012888888881881", False), # Visa
        ]

        from lab_functions import unit_tester_1

        print(unit_tester_1(test_data, validate_credit_card))
