number_one = 0
number_two = 0
while True:
    operand = input("What is the operand we're working with? You can enter '+', '-', '/', '*' :\n")
    if operand == "+":
        number_one = int(input("Enter the first number to add: \n"))
        number_two = int(input("Second number: \n"))
        print(f"Answer: {number_one + number_two}")
        break
    elif operand == "-":
        number_one = int(input("Enter the first number to subtract: \n"))
        number_two = int(input("Second number: \n"))
        print(f"Answer: {number_one - number_two}")
        break
    elif operand == "*":
        number_one = int(input("Enter the first number to multiply: \n"))
        number_two = int(input("Second number: \n"))
        print(f"Answer: {number_one * number_two}")
        break
    elif operand == "/":
        number_one = int(input("Enter the first number to divide: \n"))
        number_two = int(input("Second number (Remember not to divide by a zero!): \n"))
        print(f"Answer: {number_one / number_two}")
        if number_two == 0:
            print("Please enter a different value than 0. Don't want the Earth the explode!")
            # number_two = int(input("Second number (Remember not to divide by a zero!): \n"))
        else:
            print(f"Answer: {number_one / number_two}")
            break
    else: 
        print("Please enter a valid op")