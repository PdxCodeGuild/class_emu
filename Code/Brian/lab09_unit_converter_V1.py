# lab09_unit_converter_V1.py
'''
Lab 9: Unit Converter
This lab will involve writing a program that allows the user to convert a number between units.

** Version 1 **

Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. Below is some sample input/output.

> what is the distance in feet? 12
> 12 ft is 3.6576 m
'''
feet = float(input("What is the distance in feet?: ")) # prompts user to input distance and stores in variable feet
metres = feet*0.3048 # converts feet to metres
print("Your distance in metres is: " + str(metres) + " metres") # displays distance in metres
