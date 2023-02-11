import numpy as np

print(np.__version__)

#create an n dimensions array

arr = np.array((1,2,3,4,5,6))
print(arr)

#0 dimension arrays

arr1 = np.array(42)
print(arr1)
print(arr1.ndim)


# 1-D arrasys

arr2 = np.array([1,2,3,4,5,6], ndmin=4)
print(arr2)
print(arr2.ndim)


# 2-D arrays

arr3 = np.array([[1,2,2,3,5], [1,2,4,2,4]])
print(arr3)
print(arr3.ndim)


# 3-D arrays

arr4 = np.array([[[1,2,3], [1,3,5], [1,4,5]]])
print(arr4)
print(arr4.ndim)

