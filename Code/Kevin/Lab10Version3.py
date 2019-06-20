user_input = ""
nums = []
while True:
    user_input = input("Enter a number, or \'done\': ")
    user_input = user_input.lower()
    if user_input.lower() == 'done':
        break
    user_input = int(user_input)
    nums.append(user_input)
sorted_list = sorted(nums)
if len(sorted_list) % 2 == 1:
    middle_number = len(sorted_list) // 2
    print(f"Middle number: {sorted_list[middle_number]}")
else:
    middle_number = len(sorted_list) // 2
    print(f"Middle numbers: {sorted_list[middle_number]} and {sorted_list[middle_number] -1}")
average_number = 0
total_sum = 0
