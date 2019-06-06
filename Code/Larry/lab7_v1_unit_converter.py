# filename: unit_converter.py

'''
Lab 9: Unit Converter

This lab will involve writing a program that allows the user to convert a number between units.

Version 1

Ask the user for the number of feet, and print out the equivalent distance in meters.
Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048.
Below is some sample input/output.

> what is the distance in feet? 12
> 12 ft is 3.6576 m

https://metricunitconversion.globefeed.com/length_conversion_table.asp

Hint:
num_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
first_num = input("What is the first number? ")
second_num = input("What is the second number? ")
print(f"The sum is {num_dict[first_num] + num_dict[second_num]}")

'''

# Ask the user for the number of feet
while True:
    input_in_feet = input("What is the distance in feet? ")
    if input_in_feet.isdigit():
        break
    else:
        print("You must enter a number. Try again.")

# Convert from feet to meters
converted_dist = int(input_in_feet) * 0.3048

# Print out the equivalent distance in meters
print(f"You entered {input_in_feet} feet. That's {round(converted_dist,4)} in meters.")
