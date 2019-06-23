# lab09_unit_converter_V3.py
'''
** Version 3 **

Add support for yards, and inches.

1 yard is 0.9144 m
1 inch is 0.0254 m
'''
import string
distance = float(input("What is the distance?: ")) # prompt user to input distance and store in variable distance
units = input("Is that distance in feet('ft'), miles('mi'), meters('m'), kilometers('km'), inches('in') or yards('yd')? ").lower() # prompt user to input units and store in variable units
ft_to_meters = 0.3048
mi_to_meters = 1609.34
m_to_meters = 1
km_to_meters = 1000
in_to_meters = 0.9144
yd_to_meters = 0.0254
if units == 'ft' or 'feet':
    print("Your distance in metres is: " + str(distance * ft_to_meters) + " metres") # display distance in metres
elif units == 'mi' or 'miles':
    print("Your distance in metres is: " + str(distance * mi_to_meters) + " metres") # display distance in metres
elif units == 'm' or 'meters':
    print("Your distance in metres is: " + str(distance * m_to_meters) + " metres") # display distance in metres
elif units == 'km' or 'kilometers':
    print("Your distance in metres is: " + str(distance * km_to_meters) + " metres") # display distance in metres
elif units == 'in' or 'inches':
    print("Your distance in metres is: " + str(distance * in_to_meters) + " metres") # display distance in metres
elif units == 'yd' or 'yards':
    print("Your distance in metres is: " + str(distance * yd_to_meters) + " metres") # display distance in metres
