# filename: lab11_v1_simple_calculator.py
'''
Lab 11: Simple Calculator

Let's write a simple REPL (read evaluate print loop) calculator that can handle
addition, subtraction, multiplication, and division.

Ask the user for an operator and each operand. Don't forget that input returns a string,
which you can convert to a float using float(user_input) where user_input is the string you got from input.
'''

# Import operator function (to convert string to operator)
import operator

# User input: Ask for an operator and an operand (int, float)
# Then, convert first_number and second_number input (string) to a float, in case user enters a decimal
user_operator = input("What is the operation you'd like to perform? (+)(-)(*)(/): ")
first_number = float(input("What is the first number? "))
second_number = float(input("What is the second number? "))

# check if the float ends in a .0 - round it off
# Source: https://stackoverflow.com/questions/16995249/how-to-see-if-a-number-ends-in-0
if int(first_number) == first_number and isinstance(first_number, float) == True:
    first_number = round(first_number)
if int(second_number) == second_number and isinstance(second_number, float) == True:
    second_number = round(second_number)

# Calculations
if user_operator == "+":
    # result = first_number + second_number # operator hard-coded
    result = operator.add(first_number,second_number) # 'add' operator called from operator()
elif user_operator == "-":
    # result = first_number - second_number # operator hard-coded
    result = operator.sub(first_number,second_number) # 'sub' operator called from operator()
elif user_operator == "*":
    # result = first_number * second_number # operator hard-coded
    result = operator.mul(first_number,second_number) # 'mul' operator called from operator()
else:
    # result = first_number / second_number # operator hard-coded
    result = operator.truediv(first_number,second_number) # 'truediv' operator called from operator()

# Check if the float ends with in (x.0, x.00, etc). if True, round it off
if int(result) == result and isinstance(result, float) == True:
    result = round(result)

# Print the result
print(f"Result: {first_number} {user_operator} {second_number} = {result}")
