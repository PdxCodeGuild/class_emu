# filename: lab18_v2_peaks_and_valleys.py
'''
Lab 18:
Define the following functions:
peaks - Returns the indices of 'peaks'.
    A peak has a lower number on both the left and the right.
valleys - Returns the indices of 'valleys'.
    A valley is a number with a higher number on both the left and the right.
peaks_and_valleys - Returns a single list of the peaks and valleys in order of appearance in the original data
    using the peak() and valleys() functions

Version 2 (optional)
Using the data list above, draw the image of X's below.
                                              X                 X
                                           X  X  X           X  X
                      X                 X  X  X  X  X     X  X  X
                   X  X  X           X  X  X  X  X  X  X  X  X  X
                X  X  X  X  X     X  X  X  X  X  X  X  X  X  X  X
             X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
          X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
       X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
    X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
    -------------------------------------------------------------
#s  1  2  3  4  5  6  7  6  5  4  5  6  7  8  9  8  7  6  7  8  9
ids 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20
'''
import lab18_v1_peaks_and_valleys as lab18v1 #this makes an alias to reference in the code below (see line 27)

# Define the dataset
data = lab18v1.data # [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

# Define variables
lists_of_lists = []                     # base case, empty list
row_number = max(data)                  # this returns the highest value in 'data'

# Loop through rows and columns
for index1 in range(max(data)):         # range(max(data)) - highest value in 'data', (9) - ROWS
    temp_list = []                      # base case; empty list
    for index2 in range(len(data)):     # range(len(data)) - number of elements/items in the list, (20)- COLUMNS
        if data[index2] >= row_number:  # if the item in the list is greater than or equal to row number
            temp_list.append('X')       # then, print an 'X'
        else:                           # if the item in the list of less than the row number
            temp_list.append(' ')       # then, print a space ' '
    row_number = row_number - 1         # increment the row number
    lists_of_lists.append(temp_list)    # add the temp list to the lists_of_lists

for small_list in lists_of_lists:       # for each sub_list with lists_of_lists
    print('  '.join(small_list))        # convert the sub_list to string with 3 spaces between each element
                                        # and print each row
