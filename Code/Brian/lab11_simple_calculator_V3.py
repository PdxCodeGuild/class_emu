# lab11_simple_calculator_V3.py
'''
** Version 3 (optional) **

Allow the user to enter a full arithmetic expression and use eval to evaluate it.
'''
user_input = eval(input("Write a math problem.  Example: '3 * 5' OR '100 + 50' OR '500 / 5':  "))
# the above prompts user for input and uses eval run the string as code
print(user_input) #prints the evaluation from user_input

# ** This seems dangerous.
