# iphone_counter.py
with open('how_many_iphones.csv') as f:
    iphone_info = f.read()

iphone_info = iphone_info.split('\n')
iphone_info.pop(-1)

iphone_list = []
for row in iphone_info:
    iphone_list.append(row.replace(' ', '').split(','))
# print(iphone_list)

list_of_dictionaries = []
key_row = iphone_info[0].replace(' ', '').split(',')
for value_row in iphone_list[1:]:
    list_of_dictionaries.append({key_row[0]: value_row[0], key_row[1]: value_row[1]})
print(list_of_dictionaries)
