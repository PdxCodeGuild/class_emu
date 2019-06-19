# lab09_unit_converter_V2.py
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
