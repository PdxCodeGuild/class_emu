list_of_numbers = []
user_input = ''
user_input = user_input.lower()

while user_input != "done":
    user_input = input("Enter a number (or 'done'): ")
    list_of_numbers.append(user_input)
print(list_of_numbers)