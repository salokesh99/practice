import numpy as np


arr1 = np.array([1,4,5,9,7,5,6,4,7,9,0,3,2,1,6])

print(type(arr1))

#slicing

arr2 = arr1[2::2]
print(arr2)
print(type(arr2))

#all same as conventional array

# negative slicing

arr3 = arr1[-3:-1]
print(arr3)


# slicing 2d arrays

arr2= np.array([[1,2,3,4,5], [1,2,3,5,7], [1,4,6,7,8]])

arr3 = arr2[1][1:3]
print(arr3)

# slicing 3d arrays

arr3 = np.array(
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

arr4 = arr3[1][2][1]

print(arr4)

# get second element from all the 3 elements

# arr5 = arr3[0:2][0:2][1]
# print(arr5)

# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
#
# print(arr[0:2, 2])

arr6 = np.array([[1,2,3,4,3,2], [1,5,6,7,8,7], [7,4,3,4,6,0]])
arr7 = arr6[0:3,2]
print('arr', arr7)

arr8 = arr6[2][2]
print(arr8)
arr9 = arr6[2,2]
print(arr9)


#works for all indexes
arr9 = arr6[0:3,2]
print('arr9', arr9)
arr9 = arr6[0:2,2]
print('arr9', arr9)
arr9 = arr6[0:1,2]
print('arr9', arr9)

#difference between arr6[0:2][1] and  arr6[0:2, 2]
print("difference between arr6[0:2][1] and  arr6[0:2, 2]")
print('arr6===>', arr6)
arr8 = arr6[0:3][2]
print('arr8', arr8)
try :
    arr9 = arr6[0:3, 2]
    print('arr9', arr9)
except:
    print('not possible')


arr10 = arr6[0:2, 1:3]
print('arr10', arr10)
arr11 = arr6[0:2][1:3]
print('arr11', arr11)
