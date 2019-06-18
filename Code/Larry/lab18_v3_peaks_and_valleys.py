# filename: lab18_v3_peaks_and_valleys.py
'''
Lab 18: Peaks and Valleys

Define the following functions:
1. peaks - Returns the indices of 'peaks'.
    A peak has a lower number on both the left and the right.
2. valleys - Returns the indices of 'valleys'.
    A valley is a number with a higher number on both the left and the right.
3. peaks_and_valleys - Returns a single list of the peaks and valleys in order of appearance
    in the original data using the peak() and valleys() functions

Version 2 (optional)
Using the data list above, draw the image of X's below.
                                              X  O  O  O  O  O  X
                                           X  X  X  O  O  O  X  X
                      X  O  O  O  O  O  X  X  X  X  X  O  X  X  X
                   X  X  X  O  O  O  X  X  X  X  X  X  X  X  X  X
                X  X  X  X  X  O  X  X  X  X  X  X  X  X  X  X  X
             X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
          X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
       X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
    X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
    -------------------------------------------------------------
#s  1  2  3  4  5  6  7  6  5  4  5  6  7  8  9  8  7  6  7  8  9
ids 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20

Version 3 (optional)
Make a function that takes in the dataset and a list of peaks, and returns a list of tuples representing lakes.
Each tuple should have a starting x coordinate, an ending x coordinate, and a height(depth).
The height is relative to the base of the graph.
'''

import lab18_v1_peaks_and_valleys as lab18v1 #this import also makes an alias

# Define the dataset
data = lab18v1.data # [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def get_lakes():
# get starts of the lakes, a.k.a. one position to the right of the peaks
    starts = []
    peaks = lab18v1.peaks(data)
    for i in range(len(peaks)):
        start = peaks[i] + 1
        starts.append(start)

    # get the depths of the lakes
    depths = []
    valleys = lab18v1.valleys(data)
    for i in range(len(valleys)):
        depth = valleys[i] - (peaks[i] + 1) + 1
        depths.append(depth)

    # calculate the end of the lake
    ends = []
    for i in range(len(starts)):
        end = starts[i] + depths[i] + 1
        ends.append(end)

    # put values (start, end, depth) in to a tuple
    output = []
    for i in range(len(ends)):
        output.append((starts[i], ends[i], depths[i]))

    # return the final result
    return output

if __name__ == '__main__':

    print(f"output_tuples: {get_lakes()}")
