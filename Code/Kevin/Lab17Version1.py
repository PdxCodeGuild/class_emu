#entered_word = input("Enter a word: ")
first_word = input("Enter the first word: ")
second_word = input("Enter the second word: ")



def check_palindrome(my_word):
    reversed_word = ""
    for i in my_word:
        reversed_word = i + reversed_word
    if my_word == reversed_word:
        print(f"{my_word} is a palindrome!")
    else:
        print(f"{my_word} is not a palindrome.")

def check_anagram(word_a, word_b):
    new_a = word_a.lower()
    new_b = word_b.lower()
    new_a = new_a.replace(" ", "")
    new_b = new_b.replace(" ", "")
    new_a = sorted(new_a)
    new_b = sorted(new_b)
    if new_a == new_b:
        print(f"\'{word_a}\' and \'{word_b}\' are anagrams!")
    else:
        print(f"\'{word_a}\' and \'{word_b}\' are not anagrams")
#check_palindrome(entered_word)
check_anagram(first_word, second_word)
