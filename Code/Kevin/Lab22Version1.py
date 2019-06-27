import re

def count_words(user_input):
    word_count = 0
    list_of_words = []
    puncutation_amount = 0
    for h in range(len(user_input)):
        if user_input[h] == '.':
            puncutation_amount +=1
        elif user_input[h] == '!':
            puncutation_amount +=1
        elif user_input[h] == '?':
            puncutation_amount +=1
        elif user_input[h] == ';':
            puncutation_amount += 1

    temp_list = re.split(r'[,\.\?!]', user_input)
    for i in range(len(temp_list)):
        temp_words = temp_list[i].split()

        for j in range(len(temp_words)):
            list_of_words.append(temp_words[j])

    for words in list_of_words:
        word_count +=1

    average_words = word_count/puncutation_amount

    return average_words
    

def count_characters(user_input):
    space_count = 0
    character_count = 0
    for j in range(len(user_input)):
        if user_input[j] == ' ':
            space_count +=1
    
    for puncutation in '!?;.':
       user_input =  user_input.replace(puncutation, '')
    user_input = user_input.replace(' ', '')    
    
    for i in range(len(user_input)):
        character_count += 1
    average_characters = character_count/space_count
    return average_characters

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}
user_string = input("Enter a sentence:\n")

word_average= count_words(user_string)
char_average = count_characters(user_string)
api_rating = (4.71*char_average) + (0.5*word_average) - 21.43
print(f"Word Average: {word_average}\nCharacter Average: {char_average}")
print(f"API for this input: {api_rating} ")
