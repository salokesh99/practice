import numpy as np


arr1 = np.array([1,2,3])
arr2 = np.array([2,5,7])

arr3 = np.concatenate((arr1, arr2))
print('arr3', arr3)
print('base', arr3.base)

# joining 2d Arrays

arr4 = np.array([[1,2,4], [1,5,3]])
arr5 = np.array([[5,3,2], [4,3,5]])

arr6 = np.concatenate((arr4, arr5))

print('arr6', arr6)

# joining 2d Arrays with axis

arr4 = np.array([[1,2,4], [1,5,3]])
arr5 = np.array([[5,3,2], [4,3,5]])

arr6 = np.concatenate((arr4, arr5), axis=0)
arr7 = np.concatenate((arr4, arr5), axis=1)

print('arr6', arr6)
print("arr7", arr7)

#stacking 2 1-D arrays

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])


arr3 = np.stack((arr1, arr2), axis=1)
arr4 = np.stack((arr1, arr2), axis=0)
# arr5 = np.stack((arr1, arr2), axis=2)






print('Arr3', arr3)
print('Arr4', arr4)
# print('Arr5', arr5)
