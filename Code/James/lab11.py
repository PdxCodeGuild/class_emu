# lab11.py


while True:

    user_operator = input("Enter operation to perform or choose 'done'. ").lower()
    if user_operator == "done":
        break
    user_operand1 = int(input("What is the first number? "))
    user_operand2 = int(input("What is the second number? "))
    operators = ("+", "-", "*", "/", "done")


    if user_operator == "+":
        print(f"Answer: {user_operand1 + user_operand2}")

    elif user_operator == "-":
        print(f"Answer: {user_operand1 - user_operand2}")

    elif user_operator == "*":
        print(f"Answer: {user_operand1 * user_operand2}")

    elif user_operator == "/":
        print(f"Answer: {user_operand1 / user_operand2}")



    #else:
        #print("Sorry.  That's not a valid input.")










#user_operand1 = float(user_operand1)
#user_operand2 = float(user_operand2)

#print(user_operand1 + user_operand2)


#v2
#user_operator = input("What is the operation youd like to perform? ")
#user_operand1 = int(input("What is the first number? "))
#user_operand2 = int(input("What is the second number? "))
#operators = ("+", "-", "*", "/")

#if user_operator == "+":
#    print(f"Answer: {user_operand1 + user_operand2}")

#if user_operator == "-":
#    print(f"Answer: {user_operand1 - user_operand2}")

#if user_operator == "*":
#    print(f"Answer: {user_operand1 * user_operand2}")

#if user_operator == "/":
#    print(f"Answer: {user_operand1 / user_operand2}")
