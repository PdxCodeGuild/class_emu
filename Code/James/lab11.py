# lab11.py

user_operator = input("What is the operation youd like to perform? ")
user_operand1 = int(input("What is the first number? "))
user_operand2 = int(input("What is the second number? "))
operators = ("+", "-", "*", "/")

if user_operator == "+":
    print(f"Answer: {user_operand1 + user_operand2}")

if user_operator == "-":
    print(f"Answer: {user_operand1 - user_operand2}")

if user_operator == "*":
    print(f"Answer: {user_operand1 * user_operand2}")

if user_operator == "/":
    print(f"Answer: {user_operand1 / user_operand2}")


#user_operand1 = float(user_operand1)
#user_operand2 = float(user_operand2)

#print(user_operand1 + user_operand2)
