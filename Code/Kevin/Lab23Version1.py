with open(r'C:\Users\WrenJ\Desktop\class_emu\Code\Kevin\contacts.csv', 'r') as file:
    lines = file.read().split('\n')
temp_list = lines[0].split(',')
# contact1 = lines[1].split(',')


lists_of_contacts =[]

for j in range(1, len(lines)):
    each_contact = {}
    contact1 = lines[j].split(',')
    
    for i in range(len(temp_list)):
        
        key = temp_list[i]
        value = contact1[i]
        each_contact[key] = value
    print(each_contact)
    lists_of_contacts.append(each_contact)

print(lists_of_contacts)  


