digits = input("Enter a credit card number and I'll validate it:\n")
digits = digits.replace(" ", "")
digits = list(digits)
total_sum = 0
# loop over digits, convert each element to an int and assign it back
for i in range(len(digits)):
    digits[i] = int(digits[i])   

validation_digit = digits[len(digits)-1]
digits = digits[0: len(digits)-1]
digits.reverse()
print(f"Reversed String: {digits}")
for i in range(len(digits)):
    if i % 2 == 0:
        digits[i] *= 2
    if digits[i] > 9:
        digits[i] -= 9
    total_sum += digits[i]

print(total_sum)
if total_sum % 10 == validation_digit:
    print(f"{validation_digit} is valid!")