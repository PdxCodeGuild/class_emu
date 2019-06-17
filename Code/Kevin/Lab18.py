

def valleys(data):
    v_list = []
    for i in range(1, len(data)-1):
        current_number = data[i]
        if current_number < data[i-1] and current_number < data[i+1]:
            v_list.append(i)
    return v_list

def peaks(num_of_peaks):
    p_list = []
    for i in range(1, len(data)-1):
        current_number = data[i]
        if current_number > data[i-1] and current_number > data[i+1]:
            p_list.append(i)
    return p_list


data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
print(f"Valleys: {valleys(data)}")
print(f"Peaks: {peaks(data)}")