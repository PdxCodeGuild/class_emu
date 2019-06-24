# lab11_simple_calculator_V2.py
'''
** Version 2 **

Allow the user to keep performing operations until they say 'done'. Use while True and break. Below is some sample input/output.

> what is the operation you'd like to perform? +
> what is the first number? 5
> what is the second number? 12
> 5 + 12 = 17
> what is the operation you'd like to perform? done
> goodbye!
'''

print("Let's solve a math problem! ") # prints a statement
while True: # a while loop to run while the condition is true or until a break or program interrup or crash
    user_operator = input("What is the operation you would like to perform? type: +, -, / or * OR hit 'done' to finish:  ") # prompts user for input
    if user_operator.lower() == 'done': # converts user_input into lowercase and checks to see if user_input is "done"
        break # if the above is true, breaks out of the loop/program
    elif user_operator in '+-*/': #if the above statement is false, checks to see if user_operator is in this string
        user_number1 = float(input("What is the first number? ")) # prompts user for input and converts it to a float
        user_number2 = float(input("What is the second number? ")) # prompts user for input and converts it to a float
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
