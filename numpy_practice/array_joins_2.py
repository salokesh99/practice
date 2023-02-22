import numpy as np


arr1 = np.array(
    [
        [
            [1,2,4],[1,2,4], [4,5,6], [1,5,7]
        ],
        [
            [6,3,6], [3,5,7], [4,6,4], [3,6,3]
        ],
        [
            [1,8,9], [12,5,77], [3,6,9], [3,6,2]
        ]
    ])

arr2 = np.array(
    [
        [
            [2,6,4],[8,9,8], [8,2,6], [8,2,7]
        ],
        [
            [6,3,6], [3,2,7], [8,6,8], [1,6,1]
        ],
        [
            [1,8,9], [19,2,77], [1,6,9], [1,6,9]
        ]
    ])

arr3 = np.concatenate((arr1,arr2), axis=0)
arr4 = np.concatenate((arr1,arr2), axis=1)
arr5 = np.concatenate((arr1,arr2), axis=2)
# 3 goes out of bound
# arr6 = np.concatenate((arr1,arr2), axis=3)

print("arr3", arr3)
print("arr4", arr4)
print("arr5", arr5)
# print("arr6", arr6)


arr3 = np.stack((arr1,arr2), axis=0)
arr4 = np.stack((arr1,arr2), axis=1)
arr5 = np.stack((arr1,arr2), axis=2)
# 3 goes out of bound
# arr6 = np.concatenate((arr1,arr2), axis=3)

print("arr3", arr3)
print("arr4", arr4)
print("arr5", arr5)
# print("arr6", arr6)

# no axis needed for h stack
arr3 = np.hstack((arr1,arr2))
arr4 = np.hstack((arr1,arr2))
arr5 = np.hstack((arr1,arr2))
# 3 goes out of bound
# arr6 = np.concatenate((arr1,arr2), axis=3)

print("arr3===>>", arr3)
print("arr4===>>", arr4)
print("arr5===>>", arr5)
# print("arr6", arr6)

arr4 = np.vstack((arr1,arr2))
arr5 = np.vstack((arr1,arr2))
arr3 = np.vstack((arr1,arr2))
# 3 goes out of bound
# arr6 = np.concatenate((arr1,arr2), axis=3)

print("arr3$$$$$$$$$$$$$$$$$$>>>", arr3)
print("arr4$$$$$$$$$$$$$$$$$$>>>", arr4)
print("arr5$$$$$$$$$$$$$$$$$$>>>", arr5)
# print("arr6", arr6)


print("==============================================")

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

print(arr)

print("==============================================")

#stack along depth

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

print(arr)

# split just splits the array into given number of splits and returns array objects
print('***********************')

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 2)

print(newarr)

