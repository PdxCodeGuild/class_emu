# filename: lab18_v1_peaks_and_valleys.py
'''
Lab 18:
Define the following functions:
peaks - Returns the indices of 'peaks'.
    A peak has a lower number on both the left and the right.
valleys - Returns the indices of 'valleys'.
    A valley is a number with a higher number on both the left and the right.
peaks_and_valleys - Returns a single list of the peaks and valleys in order of appearance in the original data
    using the peak() and valleys() functions
'''

# for num in range(1, len(input_string) - 1):
#     if input_string[num] in vowel_string and input_string[num-1] in consonant_string and input_string[num+1] in consonant_string:
#         print(input_string[num-1] + input_string[num] + input_string[num+1])

# Define the dataset
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data): # Returns the indices of 'peaks'

    list_of_peaks = []
    for i in range(1, len(data)-1):
        if data[i] > data[i-1] and data[i] > data[i+1]:
            list_of_peaks.append(i)
    return list_of_peaks

# print(peaks(data)) # => [6, 14] #  this is commented out since I'm calling the function from lab16_v2

def valleys(data): # Returns the indices of 'valleys'

    list_of_valleys = []
    for i in range(1, len(data)-1):
        if data[i] < data[i-1] and data[i] < data[i+1]:
            list_of_valleys.append(i)
    return list_of_valleys

# print(valleys(data)) # => [9, 17] #  this is commented out since I'm calling the function from lab16_v2

def peaks_and_valleys(data): # Returns a single list of peaks and valleys in order of appearance in the original data

    list_of_peaks_and_valleys = peaks(data) + valleys(data)
    list_of_peaks_and_valleys.sort()
    return list_of_peaks_and_valleys

# print(peaks_and_valleys(data)) #  this is commented out since I'm calling the function from lab16_v2
