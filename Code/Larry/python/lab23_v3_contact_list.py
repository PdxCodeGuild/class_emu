# filename: lab23_v3_contact_list.py
"""
Lab 23: Contact List

Goal: Build a program to manage a list of contacts, using a CSV "comma-separated values" file.

Version 1: Open the CSV, convert the lines of text into a list of dictionaries, one dictionary for each user.
Version 2: Implement a CRUD REPL
Version 3: When REPL loop finishes, write the updated contact info to the CSV file to be saved.
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
# Note: This code does not prevent blank input.
def create_user():
    name = input("Enter your name: ").lower()
    age = input("Enter your age: ").lower()
    email = input("Enter your email address: ").lower()
    favorite_color = input("What is your favorite color: ").lower()
    contacts.append({'name': name, 'age': age, 'email': email, 'favorite color': favorite_color})

### Retrieve a record ###
# Ask the user for the contact's name, find the user with the given name, and display their information
def get_user(name):
    for i in range(len(contacts)):                   # loop through each contact record
        if contacts[i]['name'] == name:              # if name matches a record with the name
            full_record = contacts[i]                # grab the whole contact (dictionary)
            return full_record                       # return the full record

def is_user_valid(prompt_text):
    while True:                                      # start infinite loop
        name_lookup = input(prompt_text).lower()     # prompt user for input
        if get_user(name_lookup) == None:            # if get_user doesn't find any matches
            print("That user doesn't exist.")        # print error msg
            continue                                 # loop back to top
        return get_user(name_lookup)                 # otherwise, return the full record

def lookup_user():
    prompt_text = "Enter the name of the user you want to lookup: "
    return is_user_valid(prompt_text)                # submit prompt_text to is_user_valid, return the result

### Update a record ###
# Ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
def update_user():
    prompt_text = "Enter the name of the user you want to update: "
    current_user = is_user_valid(prompt_text)        # fetch and return valid user's full record

    while True:
        attribute = input("Enter the field you want to update: (age) (email) (favorite color): ").lower()
        choices = ['age', 'email', 'favorite color']
        if attribute not in choices:                 # ensure only valid attributes are entered
            print("That is not one of the choices.") #
            continue                                 #
        break

    current_value = current_user[attribute]
    print(f"{current_user['name'].title()}'s {attribute} is currently set to {current_value}.")
    while True:
        new_value = input("Enter the new value: ")   # ensure something is entered
        stripped_new_value = new_value.strip()       # (string whitespace)
        if len(stripped_new_value) == 0:             #
            print("New value cannot be blank.")      #
            continue                                 #
        break                                        #
    current_user[attribute] = new_value              # then, update attribute for current_user
    return current_user                              # return current_user's full record

### Delete a record ###
# Ask the user for the contact's name, remove the contact with the given name from the contact list.
def delete_user():
    prompt_text = "Enter the name of the user you want to delete: "
    current_user = is_user_valid(prompt_text)        # fetch and return valid user's full record

    answer = input(f"Delete User: Are you sure? (yes)(no): ").lower()
    if answer != "yes":                              # give user a chance to abort
        return "Operation aborted."                  # print a abort succeeded msg
    else:
        # row_index = contacts.index(current_user)   # Option 1: Get index of dictionary to be deleted
        # del contacts[row_index]                    #           Use 'del list[index]' method
        contacts.remove(current_user)                # Option 2: Use 'list.remove(value)' method
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
    if len(contacts) == 0:
        print("\nThere are no records show.\n")
    else:
        print(f"""
        +------+-----+-------+----------------+
        | name | age | email | favorite color |
        +------+-----+-------+----------------+""")
        for i in range(len(contacts)):
            print(f"""        | {contacts[i]['name']} | {contacts[i]['age']} | {contacts[i]['email']} | {contacts[i]['favorite color']} | """)
        print(f"""        +------+-----+-------+----------------+
        """)

def write_changes():
    f = open('./lab23_data.csv', 'w')               # open the .csv file for writing (w)
    csv_header = ','.join(header)                   # convert header (list) to comma-separated string
    f.write(f"{csv_header}\r\n")                    # write the header row
    for i in range(len(contacts)):                  # loop through the elements in contacts list
        t_contact = list(contacts[i].values())      # convert dictionary to list and set temporary variable (t_contact)
        t_csv_row = ','.join(t_contact)             # convert contact (list) to comma-separated string
        f.write(f"{t_csv_row}\r\n")                 # write the contact row
    f.close()                                       # close the .csv file from writing

def try_again(prompt_text):
    return input(prompt_text).lower() == "no"       # if user types 'no', returns True

##############################################################################
## Where the functions are called
##############################################################################

def main():
    while True:
        operation = input("Type an operation: (showall)(lookup)(add)(update)(delete), (done): ").lower()
        valid_operations = ['showall', 'lookup', 'add', 'update', 'delete', 'done']
        if operation not in valid_operations:       # ensure only valid operations are entered
            print("That is not one of the choices.")#
            continue                                #
        if operation == "showall":
            print_contacts()                        # prints all contacts
        elif operation == "lookup":
            print_one_contact(lookup_user())        # prints selected contact
        elif operation == "add":
            create_user()                           # create a new contact
            print_contacts()                        # prints new contact list in an ascii table
            write_changes()                         # commits the changes to the .csv file
        elif operation == "update":
            print_one_contact(update_user())        # prints updated contact in an ascii table
            write_changes()                         # commits the changes to the .csv file
        elif operation == "delete":
            delete_status = delete_user()           # calls delete_user(), which may delete contact, and sets delete_status
            print(f"{delete_status}")               # prints "Operation aborted."
            if delete_status == "User deleted.":
                print_contacts()                    # prints full contact list in an ascii table
            write_changes()                         # commits the changes to the .csv file
        elif operation == "done":
            break                                   # break out of while loop

        if try_again("Do you want to try again? (yes)(no): "):
            break                                   # break if answer was 'no'

if __name__ == "__main__":
    main()
