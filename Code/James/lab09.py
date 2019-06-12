# lab09.py

#v1


#user_input = input("How many feet? ")
#num_convert = int(user_input) * 0.3048
#print(f" {user_input}ft is {num_convert}m ")


#V2/3


user_input1 = int(input("What is the distance? "))
user_input1 = int(user_input1)
user_input2 = input("What unit? ").lower()

if userinput2 in ["in", "inches"]:
    user input = "in"
    print(user_input1 / 0.0254)

if user_input2 in ["ft", "feet"]:
    user_input2 = "ft"
    print(user_input1 / 3.281)

if user_input2 in ["mi", "miles"]:
    user_input2 = "mi"
    print(user_input1 * 1609.366)

if user_input2 in ["ki", "kilometers"]:
    user_input2 = "ki"
    print(user_input1 * 1000 )

if user_input2 in ["m", "meters"]:
    user_input2 = "m"
    print(user_input1 * 1)

if user_input2 in ["mi", "miles"]:
    user_input2 = "mi"
    print(user_input1 * 1609.366)

if user_input2 in ["ki", "kilometers"]:
    user_input2 = "ki"
    print(user_input1 * 1000)

if user_input2 in ["y", "yards"]:
    user_input2 = "y"
    print(user_input1 * 0.9144)












#int(user_distance) / 3.281
#if user_unit == "mi":
#    int(user_distance) / 1609.344
#    print()
#if user_unit == "m":
#    int(user_distance) * 1
#    print()
#if user_unit == "ki":
#    int(unser_distance) * 1000
#    print()


#print(f" {user_input}ft is {num_convert}m ")
