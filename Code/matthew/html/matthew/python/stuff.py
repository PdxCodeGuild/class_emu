
word_dict = {'z': 12, 'a': 123, 'the': 234, 'at': 2341}
words = list(word_dict.items()) # .items() returns a list of tuples



def get_sort_value(tup):
    return tup[1]
words.sort(key=get_sort_value, reverse=True)  # sort largest to smallest, based on count

#
# print(words[0])
# print(words[1])
# print(words[0] > words[1])


words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count

print(words)

def add(a, b):
    return a + b

# add = lambda a, b: a + b

# def perform_operation(function, a, b):
#     return function(a, b)
#
# print(perform_operation(add, 5, 2))
