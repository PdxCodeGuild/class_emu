# lab08_make_change_V1.py
unconverted_pennies = int(input('Please enter how many pennies you have: ')) #asks user for input
print(unconverted_pennies//25, "quarters") #prints the users input floor divided by 25 for quarters
unconverted_pennies = unconverted_pennies % 25 #modulous by 25 and returns the remainder
print(unconverted_pennies//10, "dimes")  #prints the users input floor divided by 10 for dimes, dicards remainder.
unconverted_pennies = unconverted_pennies % 10 #modulous by 10 and returns the remainder
print(unconverted_pennies//5, "nickels") #prints the users input floor divided by 5 for nickels, dicards remainder.
unconverted_pennies = unconverted_pennies % 5 #modulous by 5 and returns the remainder
print(unconverted_pennies//1, "pennies") #prints the users input floor divided by 1 for pennies
