# filename: lab08_v3_make_change.py
'''
Lab 8: Make Change
Let's convert a dollar amount into a number of coins.
The input will be the total amount,
the output will be the number of quarters, dimes, nickles, and pennies.

Version 1
Have the user enter the total number in pennies, e.g. for $1.36, the user will enter 136.

Version 2
Have the user enter a dollar amount (1.36), convert this to the total in pennies, and proceed as before.
Do this with float() and round().

Version 3 (optional)
Instead of hard-coding the coins, store them in a list. This way you can make custom coins.

coins = [
    ('quarter', 50),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]
'''
# Not sure how to access items from list example above, therefore using a dictionary instead
coins = {'quarter': 25, 'dime': 10, 'nickel': 5, 'penny': 1}
# Have the user enter the total number in dollars & cents, e.g. 1.36.
dollars = input("Enter a dollar amount (e.g. 1.36): ")
# convert dollars & cents to pennies
pennies = round(float(dollars) * 100)
# print(user_pennies) #debug

# Calculate the number of quarters, dimes, nickles, and pennies from user input
quarters = pennies // coins["quarter"]
pennies = pennies % coins["quarter"]
dimes = pennies // coins["dime"]
pennies = pennies % coins["dime"]
nickels = pennies // coins["nickel"]
pennies = pennies % coins["nickel"]

# Print the result
print(f"That breaks down to {quarters} quarters, {dimes} dimes, {nickels} nickels, and {pennies} pennies")
