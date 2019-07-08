# filename: lab23_v2_contact_list.py
"""
Lab 23: Contact List

Goal: Build a program to manage a list of contacts, using a CSV "comma-separated values" file.

Version 1: Open the CSV, convert the lines of text into a list of dictionaries, one dictionary for each user.
Version 2: Implement a CRUD REPL
"""

# Use Python open the CSV
with open('./lab23_data.csv', 'r') as file:
    lines = file.read().split('\n')
    lines.pop(-1)

# Convert the lines of text into a list of dictionaries, one dictionary for each user
# (The text in the header represents the keys, the text in the other lines represent the values)
contacts = []
header = lines[0].split(',')
for i in range(1, len(lines)): # down the rows(matt)
    contact = lines[i].split(',')
    contact_dict = {}
    for j in range(len(header)): # across the columns(matt)
        contact_dict[header[j]] = contact[j]
    contacts.append(contact_dict)

# Once you've processed the file, these are the results (raw list of tuples)
'''
    contacts => [
    {'name': 'joe',  'age': '34', 'email': 'joe@gmail.com',  'favorite color': 'blue'},
    {'name': 'jane', 'age': '43', 'email': 'jane@gmail.com', 'favorite color': 'green'},
    {'name': 'jill', 'age': '65', 'email': 'jill@gmail.com', 'favorite color': 'orange'}
    ]
'''

### Create a record ###
# Ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
def create_user():
    name = input("Enter your name: ").lower()
    age = input("Enter your age: ").lower()
    email = input("Enter your email address: ").lower()
    favorite_color = input("What is your favorite color: ").lower()
    contacts.append({'name': name, 'age': age, 'email': email, 'favorite color': favorite_color})

### Retrieve a record ###
# Ask the user for the contact's name, find the user with the given name, and display their information
def get_user(name):
    for i in range(len(contacts)):
        if contacts[i]['name'] == name:
            user_record = contacts[i]
            return user_record

def is_user_valid(prompt_text):
    while True:
        name_lookup = input(prompt_text).lower()
        if get_user(name_lookup) == None:
            print("That user doesn't exist.")
            continue
        return get_user(name_lookup)

def lookup_user():
    prompt_text = "Enter the name of the user you want to lookup: "
    return is_user_valid(prompt_text)

### Update a record ###
# Ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
def update_user():
    prompt_text = "Enter the name of the user you want to update: "
    current_user = is_user_valid(prompt_text)

    while True:
        attribute = input("Enter the field you want to update: (age) (email) (favorite color) ").lower()
        choices = ['age', 'email', 'favorite color']
        if attribute not in choices:
            print("That is not one of the choices.")
            continue
        break

    current_value = current_user[attribute]
    new_value = input(f"{current_user['name'].title()}'s {attribute} is currently set to {current_value}.\nEnter the new value: ")
    current_user[attribute] = new_value
    return current_user

### Delete a record ###
# Ask the user for the contact's name, remove the contact with the given name from the contact list.
def delete_user():
    prompt_text = "Enter the name of the user you want to delete: "
    current_user = is_user_valid(prompt_text)

    answer = input(f"Delete User: Are you sure? (yes)(no): ").lower()
    if answer != "yes":
        return "Operation aborted."
    else:
        # row_index = contacts.index(current_user) # Option 1: Get index of dictionary to be deleted
        # del contacts[row_index]                  #           Use 'del list[index]' method
        contacts.remove(current_user)              # Option 2: Use 'list.remove(value)' method
        return "User deleted."

def print_one_contact(user):
    print(f"""
        +------+-----+-------+----------------+
        | name | age | email | favorite color |
        +------+-----+-------+----------------+
        | {user['name']} | {user['age']} | {user['email']} | {user['favorite color']} |
        +------+-----+-------+----------------+
""")

def print_contacts():
    print(f"""
        +------+-----+-------+----------------+
        | name | age | email | favorite color |
        +------+-----+-------+----------------+""")
    for i in range(len(contacts)):
        print(f"""        | {contacts[i]['name']} | {contacts[i]['age']} | {contacts[i]['email']} | {contacts[i]['favorite color']} | """)
    print(f"""        +------+-----+-------+----------------+
""")

##############################################################################
## Where the functions are called
##############################################################################

def main():
    operation = input("Type an operation: (showall)(lookup)(add)(update)(delete): ").lower()
    valid_operations = ['showall', 'lookup', 'add', 'update', 'delete']
    while True:
        if operation not in valid_operations:
            print("That is not one of the choices.")
            continue
        break
    if operation == "showall":
        print_contacts()
    elif operation == "lookup":
        print_one_contact(lookup_user())
    elif operation == "add":
        create_user()
        print_contacts()                        # prints new contact list in an ascii table
    elif operation == "update":
        print_one_contact(update_user())
    elif operation == "delete":
        delete_status = delete_user()
        print(f"{delete_status}")               # prints "Operation aborted." or deletes user
        if delete_status == "User deleted.":
            print_contacts()                    # prints full contact list in an ascii table

if __name__ == "__main__":
    main()
