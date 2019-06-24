total_amount = float(input("How much money am I converting?"))
total_amount *= 100
total_amount = int(total_amount)
number_of_quarters = total_amount // 25
total_amount -= number_of_quarters *25
number_of_dimes = total_amount // 10
total_amount -= number_of_dimes *10
number_of_nickles = total_amount // 5
total_amount -= number_of_nickles * 5
number_of_pennies = total_amount
total_amount -= number_of_pennies * 1
print(f"Number of Quarters: {number_of_quarters}\nNumber of Dimes: {number_of_dimes}\nNumber of Nickles: {number_of_nickles}\nNumber of Pennies: {number_of_pennies}")