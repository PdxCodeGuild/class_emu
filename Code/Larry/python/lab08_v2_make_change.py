# filename: lab08_v2_make_change.py
'''
Lab 8: Make Change

Let's convert a dollar amount into a number of coins.
The input will be the total amount,
the output will be the number of quarters, dimes, nickles, and pennies.

Always break the total into the highest coin value first, resulting in the fewest amount of coins.
For this, you'll have to use floor division //, which throws away the remainder.
10/3 is 3.333333, 10//3 is 3.

Version 1
Have the user enter the total number in pennies, e.g. for $1.36, the user will enter 136.

Version 2
Have the user enter a dollar amount (1.36), convert this to the total in pennies, and proceed as before.
Do this with float() and round().
'''

# Have the user enter the total number in dollars & cents, e.g. 1.36.
dollars = input("Enter a dollar amount (e.g. 1.36): ")
# convert dollars & cents to pennies
pennies = round(float(dollars) * 100)

# Calculate the number of quarters, dimes, nickles, and pennies from user input
quarters = pennies // 25
pennies = pennies % 25
dimes = pennies // 10
pennies = pennies % 10
nickels = pennies // 5
pennies = pennies % 5

# Print the result
print(f"That breaks down to {quarters} quarters, {dimes} dimes, {nickels} nickels, and {pennies} pennies")
