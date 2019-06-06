# filename: unit_converter.py

'''
Lab 9: Unit Converter

This lab will involve writing a program that allows the user to convert a number between units.

Version 1
Ask the user for the number of feet, and print out the equivalent distance in meters

Version 2
Allow the user to also enter the units.
Then depending on the units, convert the distance into meters.
The units we'll allow are feet, miles, meters, and kilometers.

1 ft is 0.3048 m
1 mi is 1609.34 m
1 m is 1 m
1 km is 1000 m
Below is some sample input/output:

> what is the distance? 100
> what are the units? mi
> 100 mi is 160934 m

https://metricunitconversion.globefeed.com/length_conversion_table.asp

Version 3
Add support for yards, and inches.

1 yard is 0.9144 m
1 inch is 0.0254 m

'''

# Ask the user for the number of feet
while True:
    input_distance = input("What is the distance? ")
    if input_distance.isdigit():
        break
    else:
        print("You must enter a number. Try again.")

# Ask the user what kind of unit they want to start with
input_units = input("What are the units (ft, mi, m, km, yd, in)? ")

# Define unit conversion (library) for feet, miles, meters, kilometers
unit_dict = { "ft": 0.3048, "feet": 0.3048,
            "mi": 1609.344, "miles": 1609.344, "mile": 1609.344,
            "m": 1, "meters": 1, "meter": 1,
            "km": 1000, "kilometers": 1000, "kilometer": 1000,
            "yd": 0.9144, "yards": 0.9144, "yard": 0.9144,
            "in": 0.0254, "inches": 0.0254, "inch": 0.0254
            }

# Convert from input(unit) to meters
converted_dist = int(input_distance) * unit_dict[input_units]

# Print out the equivalent distance in meters
print(f"You entered {input_distance} {input_units}. That's {round(converted_dist,4)} meters.")
