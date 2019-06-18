# lab08_make_change_V3.py
coins = [] #empty list to be populated
unconverted_dollars = input('Please enter how much money you have.  Example: $4.67: ') #asks user for input
unconverted_dollars = int(float(unconverted_dollars.strip('$'))*100) #converts to interger and float, strips away the $ and multiplies by 100 to convert to pennies
quarters = unconverted_dollars//25 #floor divides user converted input by 25 for quarters
coins.append(quarters) #adds to list of [coins]
unconverted_dollars = unconverted_dollars % 25 #modulous by 25 and returns the remainder
dimes = unconverted_dollars//10 #floor divides user converted input by 10 for dimes
coins.append(dimes) #adds to list of [coins]
unconverted_dollars = unconverted_dollars % 10 #modulous by 10 and returns the remainder
nickels = unconverted_dollars//5 #floor divides user converted input by 5 for nickels
coins.append(nickels) #adds to list of [coins]
unconverted_dollars = unconverted_dollars % 5 #modulous by 5 and returns the remainder
pennies = unconverted_dollars//1 #floor divides user converted input by 1 for pennies
coins.append(pennies) #adds to list of [coins]
print("Quarters", coins[0], "Dimes", coins[1], "Nickels", coins[2], "Pennies", coins[3]) #prints all coins
