# lab22_compute_automated_readability_index.py

'''
Lab 22: Compute Automated Readability Index

Compute the ARI for a given body of text loaded in from a file.
The automated readability index (ARI) is a formula for computing the U.S. grade level for a given block of text.
The general formula to compute the ARI is as follows:

4.71 * (characters/words) + 0.5 * (words/sentences) - 21.43

ARI Formula

The score is computed by multiplying the number of characters divided by the number of words by 4.71,
adding the number of words divided by the number of sentences multiplied by 0.5, and subtracting 21.43.
If the result is a decimal, always round up.
Scores greater than 14 should be presented as having the same age and grade level as scores of 14.

Scores correspond to the following ages and grad levels:

    Score  Ages     Grade Level               Score  Ages     Grade Level
     1       5-6    Kindergarten               8     12-13    Seventh Grade
     2       6-7    First Grade                9     13-14    Eighth Grade
     3       7-8    Second Grade              10     14-15    Ninth Grade
     4       8-9    Third Grade               11     15-16    Tenth Grade
     5      9-10    Fourth Grade              12     16-17    Eleventh grade
     6     10-11    Fifth Grade               13     17-18    Twelfth grade
     7     11-12    Sixth Grade               14     18-22    College

Once you’ve computed the ARI score, you can use the following dictionary to look up the age range and grade level.

#Note I moved ari_scale below to save room. DOES NOT reflect valid dictionary.

ari_scale = {
1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
2: {'ages':   '6-7', 'grade_level':    '1st Grade'},     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},     10: {'ages': '14-15', 'grade_level':   '9th Grade'},
4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},     11: {'ages': '15-16', 'grade_level':   '10th Grade'},
5: {'ages':  '9-10', 'grade_level':    '4th Grade'},     12: {'ages': '16-17', 'grade_level':   '11th Grade'},
6: {'ages': '10-11', 'grade_level':    '5th Grade'},     13: {'ages': '17-18', 'grade_level':   '12th Grade'},
7: {'ages': '11-12', 'grade_level':    '6th Grade'},     14: {'ages': '18-22', 'grade_level':      'College'}
}
The output should look something like the following:

--------------------------------------------------------

The ARI for gettysburg-address.txt is 12
This corresponds to a 11th Grade level of difficulty
that is suitable for an average person 16-17 years old.

--------------------------------------------------------
'''
import requests # imports the requests module

url = 'http://www.gutenberg.org/cache/epub/41481/pg41481.txt' # defines variable url
response = requests.get(url) # gets url
contents = response.text # defines variable contents as url/file and .text grabs the body of the data
# contents = "Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal. Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this. But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth."

# print(contents)
def count_char(contents): # defines a function called count_char
    char_count = 0 # defines variable char_count and sets it to 0
    for char in contents: # for loop to iterate over contents
        if char in 'abcdefghijklmnopqrstuvwxyz': # if a character is in this string, below code runs
            char_count += 1 # if above is true, increases char_count by 1
    return char_count # returns the char_count
# print(count_char(contents))

characters = count_char(contents) # defines variable characters and applies the function char_count to contents

words = len(contents.split()) # defines variable words and counts the length of the list that .split creates from contents

# print(characters)
# print(words)

def count_sentences(contents): # defines a function called count_sentences
    sentence_count = 0 # defines variable sentence_count and sets it to 0
    for char in contents: # for loop to iterate over contents
        if char in '.!?': # if a character is in this string, below code runs
            sentence_count += 1 # if above is true, increases sentence_count by 1
    return sentence_count # returns the sentence_count
# print(count_sentences(contents))
contents = contents.replace("...", ',') # replaces ... with ,
sentences = count_sentences(contents) # defines variable sentences and applies the function count_sentences to contents
# print(sentences)

ari = round(4.71*(characters/words) + 0.5*(words/sentences) - 21.43) # computes the number for ARI
# print(ari)
ari_scale = { # defines variable ari_scale as dictionary with ages and grade_level data
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

if ari < 0: # if statement in the event ari is less than 0, below code will run
    ari == 1 # if the above is true, will make ari 1
if ari > 14: # if statement in the event ari is greater than 14, below code will run
    ari == 14 # if the above is true, will make ari 14

grade = ari_scale[ari] # defines variable grade and set's it to pull data from the dictionary ari_scale based on ari
# print(grade)

print('The ARI for ' + url + ' is ' + str(ari))
print('This corresponds to a ' + grade['grade_level'] + ' level of difficulty')
print('that is suitable for an average person ' + grade['ages'] + ' years old')
