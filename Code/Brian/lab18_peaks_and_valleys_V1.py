# lab18_peaks_and_valleys_V1.py

'''
Lab 18: Peaks and Valleys

** Version 1 **

Define the following functions:

peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.

Visualization of test data:

Data	1	2	3	4	5	6	7	6	5	4	5	6	7	8	9	8	7	6	7	8	9
Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20
POI							P			V					P			V
Example I/O:

                                                      X                 X
                                                   X  X  X           X  X
                              X                 X  X  X  X  X     X  X  X
                           X  X  X           X  X  X  X  X  X  X  X  X  X
                        X  X  X  X  X     X  X  X  X  X  X  X  X  X  X  X
                     X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
                  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
               X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
            X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
>>> data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
>>> peaks(data)
[6, 14]
>>> valleys(data)
[9, 17]
>>> peaks_and_valleys(data)
[6, 9, 14, 17]
'''

# print(data)
def peaks(data): # defines fuction peaks with parameter data
    peaks_list = [] # defines variable peaks_list as an empty list
    for num in range(1, len(data)-1): # for loop for the number in range of data (-1 makes sure don't iterate past end of list)
        right = data[num+1] # defines variable right as data number + 1 to the right of it
        middle = data[num] # defines variable middle as data number
        left = data[num-1] # defines variable left as data number - 1 to the left of it
        if right < middle and left < middle: # if statement is true, below code will run
            peaks_list.append(num) # if the above statement is true, will append the peaks list with the number
    return peaks_list # returns the list of peaks

def valleys(data): # defines fuction valleys with parameter data
    valley_list = [] # defines variable valley_list as an empty list
    for num in range(1, len(data)-1): # for loop for the number in range of data (-1 makes sure don't iterate past end of list)
        right = data[num+1] # defines variable right as data number + 1 to the right of it
        middle = data[num] # defines variable middle as data number
        left = data[num-1] # defines variable left as data number - 1 to the left of it
        if right > middle and left > middle: # if statement is true, below code will run
            valley_list.append(num) # if the above statement is true, will append the valley list with the number
    return valley_list # returns the list of valleys

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9] # defines variable data as list of number data
print(peaks(data)) # prints the peaks data by calling the function peaks and applying it to data
print(valleys(data)) # prints the valleys data by calling the function valleys and applying it to data
pv_combined = sorted(peaks(data) + valleys(data)) # sorts the numbers and combines them
print(pv_combined)
