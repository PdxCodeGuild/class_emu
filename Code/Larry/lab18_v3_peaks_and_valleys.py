# filename: lab18_v3_peaks_and_valleys.py
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

# get starts of the lakes, a.k.a. one position to the right of the peaks
def get_starts():
    starts = []
    for i in range(len(lab18v1.peaks(data))):
        start = lab18v1.peaks(data)[i] + 1
        starts.append(start)
    return starts

# get the depths of the lakes, caluculated from diff between the starts of the lake & the valleys
def get_depths():
    depths = []
    for i in range(len(lab18v1.valleys(data))):
        valley = lab18v1.valleys(data)[i]
        peak = lab18v1.peaks(data)[i] + 1
        depth = valley - peak + 1 #
        depths.append(depth)
    return depths

def get_ends():
    # calculate the end of the lake
    # 1: inelegant method
    # where the right side of the lake is based on a constant (the depth + n=1,2,3,etc)
    depths = get_depths()
    starts = get_starts()
    # print(depths)
    ends = []
    for i in range(len(lab18v1.peaks(data))):
        end = starts[i] + depths[i] + 1
        ends.append(end)
    return ends

    # 2: elegant method
    # where the right side of the lake is the same height as the left side

# put values (start, end, depth) in to a tuple
starts = get_starts()
ends = get_ends()
depths = get_depths()
output_tuple_cheat = [(starts[0], ends[0], depths[0]),(starts[1], ends[1], depths[1])]

# ### this isn't working yet ###
# output = []
# for i in range(3):
#     for j in range(len(get_ends())):
#         output.append((starts[j], ends[j], depths[j]))
# print(f"output: {output}")

if __name__ == '__main__':

    print(f"get_starts: {get_starts()}")
    print(f"get_ends: {get_ends()}")
    print(f"get_depths: {get_depths()}")
    print(f"output_tuple_cheat: {output_tuple_cheat}")
