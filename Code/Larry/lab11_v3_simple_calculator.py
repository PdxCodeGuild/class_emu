# filename: lab11_v3_simple_calculator.py
'''
Lab 11: Simple Calculator

Let's write a simple REPL (read evaluate print loop) calculator that can handle addition, subtraction, multiplication,
and division. Ask the user for an operator and each operand. Don't forget that input returns a string,
which you can convert to a float using float(user_input) where user_input is the string you got from input.

Version 3 (optional)
Allow the user to enter a full arithmetic expression and use eval to evaluate it.
'''

while True:
    # User input: Ask for an operator and an operand (int, float)
    user_arith_exp = input("Enter a full arithmetic expression, e.g. 3+4 (x+y)(x-y)(x*y)(x/y): ")

    # Use eval to evaluate it
    result = eval(user_arith_exp)

    # Check if the float ends with in (x.0, x.00, etc). if True, round it off
    if int(result) == result and isinstance(result, float):
        result = round(result)

    # Print the result
    print(f"\nResult: {user_arith_exp} = {result}")

    # Ask if user wants to keep performing operations (and set answer to lowercase)
    play_again = input("\nDo you want to keep performing operations? (yes)(no)(done): ").lower()
    if play_again == "no" or play_again == "done": # if user types "no" or "done"
        print("Goodbye!\n") # print 'Goodbye!'
        break # break out of while loop

# Alternate method for lines 30-32
    # if play_again == "yes": # alternate method to "play again"
    #     continue # if user types "yes", continue, starting at the top of the while loop
    # print("Goodbye!\n") # if user types anything else, print 'Goodbye!'
    # break # then, break out of while loop
