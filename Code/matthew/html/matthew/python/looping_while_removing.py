





# crash
# for i in range(len(letters)):
#     print(i, letters)
#     if (letters[i] == 'c'):
#         letters.pop(i)


letters = ['a', 'b', 'c', 'c', 'd', 'e']
letters_temp = []
for i in range(len(letters)):
    if letters[i] != 'c':
        letters_temp.append(letters[i])
letters = letters_temp
print(letters)


letters = ['a', 'b', 'c', 'c', 'd', 'e']
i = 0
while i < len(letters):
    if letters[i] == 'c':
        letters.pop(i)
    else:
        i += 1
print(letters)


letters = ['a', 'b', 'c', 'c', 'd', 'e']
for i in range(len(letters)-1, -1, -1):
    if letters[i] == 'c':
        letters.pop(i)

print(letters)
