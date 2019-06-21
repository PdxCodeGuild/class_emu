# user_string = input("Enter stuff separated by commas:\n")
# my_list = user_string.split(',')
# print(my_list)

# x = input("Input a number between 0 and 99:\n")
# x = int(x)
# hundreds_digit = x // 100
# tens_digit = (x // 10) % 10
# ones_digit = x % 10

# print(f"Hundreds: {hundreds_digit} Tens: {tens_digit} Ones: {ones_digit}")

# entered_word = input("Enter a word: ")
# reversed_word = ""
# for i in entered_word:
#     print(entered_word)

emotion_dict = {}
while True: # This REPL will run until the user types 'done'
    user_input = input("How are you feeling? (type 'done' to leave) >")
    if user_input == 'done':
        break 
    if user_input in emotion_dict.keys(): # If we've seen the emotion before
        emotion_dict[user_input] += 1 # make the counter go up by one
    else: # If this is the first time we're seeing the emotion
        emotion_dict[user_input] = 1 # set a new counter and start it at one
    print(emotion_dict)