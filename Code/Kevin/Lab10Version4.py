user_input = ""
nums = []
count_dict = {}
while True:
    user_input = input("Enter a number, or \'done\': ")
    user_input = user_input.lower()
    if user_input.lower() == 'done':
        break
    user_input = int(user_input)
    if user_input in count_dict.keys():
        count_dict[user_input] += 1
    else:
        count_dict[user_input] = 1
print(count_dict)  

mode_number = 0
for numbers in count_dict:
    if count_dict[numbers] > mode_number:
        mode_number = numbers

print(f"Mode: {mode_number}")