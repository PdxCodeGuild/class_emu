# print_board.py

list_of_lists = []
symbol_list = ['.', 'x', 'X', 'hello there']
for index1 in range(3):
    temp_list = []
    for index2 in range(3):
        temp_list.append(symbol_list[index1])
    list_of_lists.append(temp_list)

    for small_lisr in list_of_lists:
        print(small_list)
