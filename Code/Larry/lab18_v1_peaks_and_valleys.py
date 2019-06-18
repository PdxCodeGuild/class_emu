# filename: lab18_v1_peaks_and_valleys.py
'''
Lab 18: Peaks and Valleys

Define the following functions:
1. peaks - Returns the indices of 'peaks'.
    A peak has a lower number on both the left and the right.
2. valleys - Returns the indices of 'valleys'.
    A valley is a number with a higher number on both the left and the right.
3. peaks_and_valleys - Returns a single list of the peaks and valleys in order of appearance
    in the original data using the peak() and valleys() functions
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


def valleys(data): # Returns the indices of 'valleys'

    list_of_valleys = []
    for i in range(1, len(data)-1):
        if data[i] < data[i-1] and data[i] < data[i+1]:
            list_of_valleys.append(i)
    return list_of_valleys


def peaks_and_valleys(data): # Returns a single list of peaks and valleys in order of appearance in the original data

    list_of_peaks_and_valleys = peaks(data) + valleys(data)
    list_of_peaks_and_valleys.sort()
    return list_of_peaks_and_valleys


if __name__ == '__main__': # only run these lines when THIS file is executed, not when imported to another file
    print(peaks(data)) # => [6, 14]

    print(valleys(data)) # => [9, 17]

    print(peaks_and_valleys(data)) # => [6, 9, 14, 17]
