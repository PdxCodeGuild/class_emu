nums = [5, 0, 8, 3, 4, 1, 6]
average_number = 0
total_sum = 0

# loop over the indices
for i in range(len(nums)):
    total_sum += nums[i]
    average_number = total_sum/ len(nums)

print(f"Sum: {total_sum}\nAverage: {average_number}")
