

# CSV
# name age occupation
# joe  123 programmer
# jane 234 web developer

# list of dictionaries, the headers become keys
# [{'name': 'joe', 'age': 123, 'occupation': 'programmer'},{'name': 'jane', 'age': 234 ...}]


d = {} # empty dictionary
d = {'name': 'joe', 'age': 234} # define a dictionary with key-value pairs
d['favorite fruit'] = 'bananana' # adding a key-value pair
d['favorite fruit'] = 'pear' # overwriting a key-value pair

# iterating over the keys
for key in d:
    print(f'Key: {key}')
    print(f'Value: {d[key]}') # using the key to get the value


keys = list(d.keys()) # list of keys
values = list(d.values()) # list of values
items = list(d.items()) # list of tuples
print(d)
print(items)
print(dict(items))

del d['favorite fruit'] # remove a key-value pair
print(d)





def combine(keys, values):
    d = {}
    for i in range(len(keys)):
        d[keys[i]] = values[i]
    return d
fruits = ['apple', 'banana', 'pear']
prices = [1.2, 3.3, 2.1]
print(combine(fruits, prices)) # {'apple':1.2, 'banana':3.3, 'pear':2.1}



def average(d):
    
    values = list(d.values())
    return sum(values) / len(values)
    
    total = 0
    for key in d:
        total += d[key]
    return total / len(d)
    
    values = list(d.values())
    total = 0
    for value in values:
        total += value
    avg = total / len(values)
    return avg
    
combined = {'apple':1.2, 'banana':3.3, 'pear':2.1}
print(average(combined)) # 2.2

