


# split and join are opposites
# print('a, b, c'.split(', '))
# print(', '.join(['a', 'b', 'c']))


# returns True if s is a palindrome, False otherwise
def is_palindrome(word):
    word = word.replace(' ', '') # remove spaces
    # print(word)
    chars = list(word)
    # print(chars)
    chars_reversed = chars.copy()
    chars_reversed.reverse()
    # print(chars_reversed)
    # if word == ''.join(chars_reversed):
    
    # copy elements into a temporary list
    # chars_reversed2 = []
    # for char_reversed in chars_reversed:
    #     if char_reversed != ' ':
    #         chars_reversed2.append(char_reversed)
    # chars_reversed = chars_reversed2
    
    if chars == chars_reversed:
        return True
    return False
    
    


test_words = ['racecar', 'mom', 'dad', 'palindrome', 'a man a plan a canal panama']
for test_word in test_words:
    if is_palindrome(test_word):
        print(f'{test_word} is a palindrome')
    else:
        print(f'{test_word} is not a palindrome')







def check_anagram(word1, word2):    
    # 1) Convert each word to lower case (lower)
    word1 = word1.lower()
    word2 = word2.lower()

    # 2) Remove all the spaces from each word (replace)
    word1 = word1.replace(' ', '')
    word2 = word2.replace(' ', '')

    # 3) Sort the letters of each word (sorted)
    # 4) Check if the two are equal

    # word1 = list(word1)
    # word1.sort()
    # word1 = ''.join(word1)
    # 
    # word2 = list(word2)
    # word2.sort()
    # word2 = ''.join(word2)
    # 
    # return word1 == word2

    return sorted(word1) == sorted(word2)
    
    
print(check_anagram('anagram', 'nag a ram'))





def anagram_transform(word):
    word = word.lower()
    word = word.replace(' ', '')
    return ''.join(sorted(word))

def check_anagram2(word1, word2):
    return anagram_transform(word1) == anagram_transform(word2)

print(check_anagram2('anagram', 'nag a ram'))