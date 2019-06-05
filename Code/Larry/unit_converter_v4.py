# filename: unit_converter_v4.py

'''
Lab 9: Unit Converter

Note:
See unit_converter.py, unit_converter_v2.py, and unit_converter_v3.py for previous objectives.

Version 4
Now we'll ask the user for the distance, the starting units, and the units to convert to.

'''

# Ask the user for the number of feet
while True:
    input_distance = input("What is the distance? ")
    if input_distance.isdigit():
        break
    else:
        print("You must enter a number. Try again.")

# Ask the user what kind of unit they want to start with
input_units = input("What are the input units (ft, mi, m, km, yd, in)? ")

# Ask the user what kind of unit they want to end up with
output_units = input("What are the output units (ft, mi, m, km, yd, in)? ")

# Define unit conversion (library) for feet, miles, meters, kilometers ==> meters
unit_dict_in = { "ft": 0.3048, "feet": 0.3048,
            "mi": 1609.344, "miles": 1609.344, "mile": 1609.344,
            "m": 1, "meters": 1, "meter": 1,
            "km": 1000, "kilometers": 1000, "kilometer": 1000,
            "yd": 0.9144, "yards": 0.9144, "yard": 0.9144,
            "in": 0.0254, "inches": 0.0254, "inch": 0.0254
            }

# Convert from input(unit) to meters
converted_dist_in_m = int(input_distance) * unit_dict_in[input_units]

unit_dict_out = { "ft": 3.2808398950131, "feet": 3.2808398950131,
            "mi": 0.00062137119223733, "miles": 0.00062137119223733, "mile": 0.00062137119223733,
            "m": 1, "meters": 1, "meter": 1,
            "km": 0.001, "kilometers": 0.001, "kilometer": 0.001,
            "yd": 1.0936132983377, "yards": 1.0936132983377, "yard": 1.0936132983377,
            "in": 39.370078740157, "inches": 39.370078740157, "inch": 39.370078740157
            }

# Convert from meters to output(unit)
converted_dist_from_m = converted_dist_in_m  * unit_dict_out[output_units]

# Print out the equivalent distance in meters
print(f"You entered {input_distance} {input_units}. That's {round(converted_dist_from_m,4)} {output_units}.")
