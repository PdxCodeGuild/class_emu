
# Lab: Sock Sorter
#
# You've just finished laundry and your expansive sock collection is in complete disorder. Sort your socks into pairs and pull out any loners.
#
# 1. Generate a list of 100 random socks, randomly chosen from a set of types: sock_types = ['ankle', 'crew', 'calf', 'thigh']
#
# 2. Find the number of duplicates and loners for each sock type. Hint: dictionaries are helpful here.
#
# Version 2
#
# Now you have a mix of types and colors. Represent socks using tuples containing one color and one type ('black', 'crew'). Randomly generate these, and then group them into pairs.
#
# sock_colors = ['black', 'white', 'blue']
import random





# sock_types = ['ankle']*3 + ['puppet']
sock_types = ['ankle', 'crew', 'calf', 'thigh', 'ski', 'toe', 'hiking', 'puppet', 'no show', 'knee high']

# sock_weights = [3, 1, 1, 2, 4, 5, 6, 3, 2, 1]
# sock_types_weighted = []
# for i in range(len(sock_types)):
#     sock_type = sock_types[i]
#     sock_weight = sock_weights[i]
#     sock_types_weighted += sock_weights[i]*[sock_types[i]]
#
# print(sock_types_weighted)
# exit()


# sock_list = []
# for i in range(100):
#     sock_list.append(random.choice(sock_types))
#
# print(sock_list)
# sock_dictionary = {}
# for i in range(len(sock_types)):
#     sock_dictionary[sock_types[i]] = 0
# for i in range(len(sock_list)):
#     sock_dictionary[sock_list[i]] += 1
#
# for sock_type in sock_types:
#     pairs = sock_dictionary[sock_type] // 2
#     loners = sock_dictionary[sock_type] % 2
#     print(f"Sock Type: {sock_type}, Pairs: {pairs}, Loners: {loners}")


sock_colors = ['black', 'white', 'blue']
sock_list = []
for i in range(10000):
    sock_list.append((random.choice(sock_types), random.choice(sock_colors)))

sock_dictionary = {}
sock_set = set(sock_list)
for sock_tuple in sock_set:
    sock_dictionary[sock_tuple] = 0
for i in range(len(sock_list)):
    sock_dictionary[sock_list[i]] += 1
for sock_tuple in sock_set:
    pairs = sock_dictionary[sock_tuple] // 2
    loners = sock_dictionary[sock_tuple] % 2
    print(f"Sock Type: {sock_tuple[0]}, Sock Color: {sock_tuple[1]}, Pairs: {pairs}, Loners: {loners}")


print(sock_set)
print(len(sock_set))
