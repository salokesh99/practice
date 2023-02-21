import numpy as np

#shape returns the length of elements at each stage
# The shape of an array is the number of elements in each dimension.


arr = np.array([[1,2,4,2,5], [1,5,3,2,4]])

print(arr.shape)
arr2= np.array([[[1,2,3], [1,2,4], [2,5,3], [2,4,5]]])
print(arr2.ndim)
print(arr2.shape)

arr3 = np.array([1,2,3,4,5], ndmin=5)
print(arr3)
print(arr3.shape)