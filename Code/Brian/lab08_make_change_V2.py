# lab08_make_change_V2.py
'''
** Version 2 **

Have the user enter a dollar amount (1.36), convert this to the total in pennies.
'''
unconverted_dollars = input('Please enter how much money you have.  Example: $4.67: ') #asks user for input
unconverted_dollars = int(float(unconverted_dollars.strip('$'))*100) #converts to interger and float, strips away the $ and multiplies by 100 to convert to pennies
print(unconverted_dollars//25, "quarters") #prints the users input floor divided by 25 for quarters
unconverted_dollars = unconverted_dollars % 25 #modulous by 25 and returns the remainder
print(unconverted_dollars//10, "dimes") #prints the users input floor divided by 10 for dimes
unconverted_dollars = unconverted_dollars % 10 #modulous by 10 and returns the remainder
print(unconverted_dollars//5, "nickels") #prints the users input floor divided by 5 for nickels
unconverted_dollars = unconverted_dollars % 5 #modulous by 5 and returns the remainder
print(unconverted_dollars//1, "pennies") #prints the users input floor divided by 1 for pennies
