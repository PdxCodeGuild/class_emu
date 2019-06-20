user_input = ""
nums = []
while True:
    user_input = input("Enter a number, or \'done\': ")
    user_input = user_input.lower()
    if user_input.lower() == 'done':
        break
    user_input = int(user_input)
    nums.append(user_input)
average_number = 0
total_sum = 0

# # loop over the indices
for i in range(len(nums)):
    total_sum += nums[i]
    average_number = total_sum/ len(nums)

print(f"Sum: {total_sum}\nAverage: {average_number}")
