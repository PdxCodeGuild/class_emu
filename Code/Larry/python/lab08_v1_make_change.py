# filename: lab08_v1_make_change.py
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
'''

# Have the user enter the total number in pennies, e.g. for $1.36 = 136.
user_pennies = int(input("Enter a dollar amount (in pennies): "))

# Calculate the number of quarters, dimes, nickles, and pennies from user input
quarters = user_pennies // 25
pennies = user_pennies % 25
dimes = pennies // 10
pennies = pennies % 10
nickels = pennies // 5
pennies = pennies % 5

# Print the result
print(f"That breaks down to {quarters} quarters, {dimes} dimes, {nickels} nickels, and {pennies} pennies")
