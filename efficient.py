from array import array

arr1 = array('i', [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
print(arr1.typecode)
print("Array 1 item size is: ", arr1.itemsize)

# arr1.insert(0,0)
# arr1.append(22)
# arr1.extend([24, 26, 28])
# print(arr1)
#
# for i,elem in enumerate(arr1):
#     arr1[i] = elem *2
#
# print(arr1)

# arr1.insert(0, 1.25)

arr2 = array('B', [18, 102, 182, 56, 89, 5, 254, 32, 64, 50])
