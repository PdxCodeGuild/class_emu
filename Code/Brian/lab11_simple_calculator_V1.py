# lab11_simple_calculator_V1.py
'''
Lab 11: Simple Calculator

** Version 1 **

Let's write a simple REPL (read evaluate print loop) calculator that can handle addition, subtraction, multiplication, and division. Ask the user for an operator and each operand. Don't forget that input returns a string, which you can convert to a float using float(user_input) where user_input is the string you got from input. Below is some sample input/output.

> What is the operation you'd like to perform? +
> What is the first number? 5
> What is the second number? 12
> 5 + 12 = 17
'''
print("Let's solve a math problem! ") # prints a statement

user_operator = input("What is the operation you would like to perform? type: +, -, / or * ") # prompts user for input
user_number1 = float(input("What is the first number? ")) # prompts user for input and converts it to a float
user_number2 = float(input("What is the second number? ")) # prompts user for input and converts it to a float
if user_operator in '+-*/': # if statement checks if user_operator is in this string
    if user_operator == '+': # if the above if statement is true, checks to see if the user operator is a +
        print("The result is: " +str(user_number1 + user_number2)) # if the above statement is true, prints the result
    elif user_operator == '-': # if the above if statement is false, checks to see if the user operator is a -
        print("The result is: " +str(user_number1 - user_number2)) # if the above statement is true, prints the result
    elif user_operator == '*': # if the above if statements are false, checks to see if the user operator is a *
        print("The result is: " +str(user_number1 * user_number2)) # if the above statement is true, prints the result
    elif user_operator == '/': # if the above if statements are false, checks to see if the user operator is a /
        print("The result is: " +str(user_number1 / user_number2)) # if the above statement is true, prints the result
else:  # if the above statements are all false, runs the below code
    print("Sorry that is not a valid operation, please type: + OR - OR / OR * ") # if the else statement is true, prints the message.
