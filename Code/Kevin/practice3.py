def common_elements(nums1, nums2):
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] == nums2[j]:
                new_list.append(nums1[i])
          
my_list = ['1', '2', '3', '4']
my_list2 = ['5', '2', '7', '3']
new_list = []
common_elements(my_list, my_list2)
print(new_list)