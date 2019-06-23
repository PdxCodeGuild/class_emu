# lab08_make_change_V1.py
'''
Lab 8: Make Change
Let's convert a dollar amount into a number of coins. The input will be the total amount, the output will be the number of quarters, dimes, nickles, and pennies. Always break the total into the highest coin value first, resulting in the fewest amount of coins. For this, you'll have to use floor division //, which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.

Concepts Covered
conditionals, comparisons
arithmetic

** Version 1 **

Have the user enter the total number in pennies, e.g. for $1.36, the user will enter 136.
'''
unconverted_pennies = int(input('Please enter how many pennies you have: ')) #asks user for input
print(unconverted_pennies//25, "quarters") #prints the users input floor divided by 25 for quarters
unconverted_pennies = unconverted_pennies % 25 #modulous by 25 and returns the remainder
print(unconverted_pennies//10, "dimes")  #prints the users input floor divided by 10 for dimes, dicards remainder.
unconverted_pennies = unconverted_pennies % 10 #modulous by 10 and returns the remainder
print(unconverted_pennies//5, "nickels") #prints the users input floor divided by 5 for nickels, dicards remainder.
unconverted_pennies = unconverted_pennies % 5 #modulous by 5 and returns the remainder
print(unconverted_pennies//1, "pennies") #prints the users input floor divided by 1 for pennies
