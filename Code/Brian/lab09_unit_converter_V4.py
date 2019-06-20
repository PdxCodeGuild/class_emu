# lab09_unit_converter_V4.py
import string
distance = float(input("Let's do some distance conversion!  What is the distance in numbers? (Example: 100): ")) # prompt user to input distance and store in variable distance as a float
convert_from_units = input("What unit will you be convering from? Type feet('ft'), miles('mi'), meters('m'), kilometers('km'), inches('in') or yards('yd') ").lower() # prompt user to input units and store in variable convert_from_units and .lower to convert input to lowercase
convert_to_units = input("What units would you like to convert to? Type feet('ft'), miles('mi'), meters('m'), kilometers('km'), inches('in') or yards('yd') ").lower() # prompt user to input units and store in variable convert_to_units and .lower to convert input to lowercase
ft_to_meters = 0.3048
mi_to_meters = 1609.34
m_to_meters = 1
km_to_meters = 1000
yd_to_meters = 0.9144
in_to_meters = 0.0254

if convert_from_units == 'ft' or convert_from_units == 'feet': # accounts for the user typing either
    meters_from_other = distance * ft_to_meters # converts user_input's number and unit choice to meters
elif convert_from_units == 'mi' or convert_from_units == 'miles':
    meters_from_other = distance * mi_to_meters
elif convert_from_units == 'm' or convert_from_units == 'meters':
    meters_from_other = distance * m_to_meters
elif convert_from_units == 'km' or convert_from_units == 'kilometers':
    meters_from_other = distance * km_to_meters
elif convert_from_units == 'in' or convert_from_units == 'inches':
    meters_from_other = distance * in_to_meters
elif convert_from_units == 'yd' or convert_from_units == 'yards':
    meters_from_other = distance * yd_to_meters

if convert_to_units == 'ft' or convert_to_units == 'feet':
    meters_to_other = meters_from_other / ft_to_meters # converts from meters to user_input's unit choice
elif convert_to_units == 'mi' or convert_to_units == 'miles':
    meters_to_other = meters_from_other / mi_to_meters
elif convert_to_units == 'm' or convert_to_units == 'meters':
    meters_to_other = meters_from_other / m_to_meters
elif convert_to_units == 'km' or convert_to_units == 'kilometers':
    meters_to_other = meters_from_other / km_to_meters
elif convert_to_units == 'in' or convert_to_units == 'inches':
    meters_to_other = meters_from_other / in_to_meters
elif convert_to_units == 'yd' or convert_to_units == 'yards':
    meters_to_other = meters_from_other / yd_to_meters
print(f"Your distance of {distance} converted from {convert_from_units} into {convert_to_units} is: {meters_to_other}") # f string to calculate the value and let the user know