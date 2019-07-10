# practice2.py

def missing_char(input_string):
    missing_list = []
    for index in range(len(input_string)):
        missing_list.append(input_string[:index] + input_string[index + 1:])
    return missing_list


def count_letter(chosen_letter, my_string):
    counter = 0
    for letter in my_string:
        if letter == chosen_letter:
                counter = counter + 1
    return counter


def count_hi(input_string):
    starting_point = 0
    hi_counter = 0
    while True:

        recent_find = input_string[starting_point:].find('hi')
        starting_point += input_string[starting_point:].find('hi') + len('hi')
        if recent_find == -1:
            break
        hi_counter += 1
    return hi_counter


def count_hi2(input_string):
    counter = 0
    for num in range(len(input_string)):
        current_substring = input_string[num:num+2]
        if current_substring == 'hi':
            counter += 1
    return counter

def cat_dog(input_string):
    counter_cat = 0
    counter_dog = 0
    for cat in range(len(input_string)):
        current_substring = input_string[cat:cat+3]
        if current_substring == 'cat':
            counter_cat += 1
        if current_substring == 'dog':
            counter_dog += 1
    return counter_cat == counter_dog
    
    
    '''
    if counter_cat == counter_dog:
        return True
    else:
        return False
       ''' 

print(cat_dog('catadogbcatdog'))

'''
def count_hi(input_string):
    hi_start = 0
    hi_counter = 0
    while hi_start >= 0:
        location = input_string[hi_start:].find('hi')
        hi_start = location + 1
    return hi_counter

print(count_hi('hihihi'))
'''