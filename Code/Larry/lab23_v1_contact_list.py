# filename: lab23_v1_contact_list.py
"""
Lab 23: Contact List

Let's build a program to manage a list of contacts, using a CSV "comma-separated values" file. Create a text file, paste the following content, and save it as "contacts.csv".

name,age,email,favorite color
joe,34,joe@gmail.com,blue
jane,43,jane@gmail.com,green
jill,65,jill@gmail.com,orange

Using Python open the CSV, convert the lines of text into a list of dictionaries, one dictionary for each user. The text in the header represents the keys, the text in the other lines represent the values.

with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    print(lines)

Once you've processed the file, your list of contacts will look something like this...

contacts = [
    {'name':'matthew', 'favorite fruit':'blackberries', 'favorite color':'orange'},
    {'name':'sam', 'favorite fruit':'pineapple' ...}
]
"""
# Use Python open the CSV
with open('./lab23_data.csv', 'r') as file:
    lines = file.read().split('\n')
    lines.pop(-1)

# Convert the lines of text into a list of dictionaries, one dictionary for each user
# (The text in the header represents the keys, the text in the other lines represent the values)
contacts = []
header = lines[0].split(',')
for i in range(1, len(header)):
    contact = lines[i].split(',')
    contact_dict = {}
    for i in range(len(contact)):
        contact_dict[header[i]] = contact[i]
    contacts.append(contact_dict)

# Once you've processed the file, your list of contacts will look something like this...
# contacts = [
#     {'name':'matthew', 'favorite fruit':'blackberries', 'favorite color':'orange'},
#     {'name':'sam', 'favorite fruit':'pineapple' ...}
# ]
print(contacts)
'''
    [
    {'name': 'joe',  'age': '34', 'email': 'joe@gmail.com',  'favorite color': 'blue'},
    {'name': 'jane', 'age': '43', 'email': 'jane@gmail.com', 'favorite color': 'green'},
    {'name': 'jill', 'age': '65', 'email': 'jill@gmail.com', 'favorite color': 'orange'}
    ]
'''
