# palindrome17.py


#def is_palindrome(s)

#split and join are opposites
#print("a, b, c".split(", "))
#print(", ").join(["a", "b", "c"}))

#returns True if s is a palindrom, False otherwise
def is_palindrome(word):
#reomve spaces
    word = word.replace(' ', '')
    #print(word)
    chars = list(word)
    #print (chars)
    chars_reversed = chars.copy()
    chars.reversed.reverse()
    #print(chars_reversed)
    #if word == ''.join(chars_reversed):

    #copy elements into a temporary list
    #chars_reversed = []
    #for char_reversed in chars_reversed:
    #   if char_reversed != ' ':
    #
    if chars -- chars_reversed:
        return True
    return False


    test_words = ['racecar', 'mom', 'dad']
    for test_word in test_words:
        if is_palindrome(test_word):
            print(f'{test_words} is a palindrome')
        else:
            print(f'{test_word} is not a palindrome')


def check_anagrom(word1, word2):
    # 1) convert each word to lower case (lower)
    word1 = word1.lower()
    word2 = wprd2.lower()

    # 2) remove all the spaces from wach word (replace)
    word1 = word1.replace(' ', '')
    word2 = wprd2.lower(' ', '')

    # 3) sort the letters of each word (sorted)
    # 4) check if the two are equal

    word1 = word1.lower()
    word2 = wprd2.lower()
