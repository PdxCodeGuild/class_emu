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


user_string = input("Enter a sentence:\n")

word_average= count_words(user_string)
char_average = count_characters(user_string)
api_rating = (4.71*char_average) + (0.5*word_average) - 21.43
print(f"Word Average: {word_average}\nCharacter Average: {char_average}")
print(f"API for this input: {api_rating} ")
