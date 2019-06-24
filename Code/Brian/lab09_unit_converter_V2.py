# lab09_unit_converter_V2.py
'''
** Version 2 **

Allow the user to also enter the units. Then depending on the units, convert the distance into meters.
The units we'll allow are feet, miles, meters, and kilometers.

1 ft is 0.3048 m
1 mi is 1609.34 m
1 m is 1 m
1 km is 1000 m
Below is some sample input/output:

> what is the distance? 100
> what are the units? mi
> 100 mi is 160934 m
'''
distance = float(input("What is the distance?: ")) # prompt user to input distance and store in variable distance
units = input("Is that distance in feet('ft'), miles('mi'), meters('m') or kilometers('km')? ").lower() # prompt user to input units and store in variable units
ft_to_meters = 0.3048
mi_to_meters = 1609.34
m_to_meters = 1
km_to_meters = 1000
if units == 'ft' or 'feet':
    print("Your distance in metres is: " + str(distance * ft_to_meters) + " metres") # display distance in metres
elif units == 'mi' or 'miles':
    print("Your distance in metres is: " + str(distance * mi_to_meters) + " metres") # display distance in metres
elif units == 'm' or 'meters':
    print("Your distance in metres is: " + str(distance * m_to_meters) + " metres") # display distance in metres
elif units == 'km' or 'kilometers':
    print("Your distance in metres is: " + str(distance * km_to_meters) + " metres") # display distance in metres
