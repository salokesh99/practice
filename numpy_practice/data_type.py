import numpy as np

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )

arr = np.array([1,2,3,4,5,6])

print(arr.ndim, arr.dtype)

arr2 = np.array(['apples', 'oranges', 'watermelons', 'muskmelons'])

print(arr2.ndim, arr2.dtype)

#Creating Arrays With a Defined Data Type

arr2 = np.array(['apples', 'oranges', 'watermelons', 'muskmelons'], dtype='S')
print(arr2.ndim, arr2.dtype)

# Create an array with data type 4 bytes integer

arr3 = np.array([1,2,4,6], dtype='i4')
print(arr3.ndim, arr3.dtype)

# errors
try:
    arr4 = np.array(['a',4, 'SS'], dtype='i')
except:
#value error raised.
    print('not possible!!!')

# Converting Data Type on Existing Arrays

arr4 = np.array([1.3,2.4,3.4])
print(arr4.ndim, arr4.dtype)

arr5 = arr4.astype('i')
print(arr5.ndim, arr5.dtype)
print(arr5)

#can also be done using int keyword

arr4 = np.array([1.3,2.4,3.4])
print(arr4.ndim, arr4.dtype)

arr5 = arr4.astype('int')
print(arr5.ndim, arr5.dtype)
print(arr5)

# converting arr5 to float

arr6 = arr5.astype('f')
print(arr6.ndim, arr6.dtype)
print(arr6)


#Change data type from integer to boolean:

arr7 = np.array([1,3,4,5,0])
arr8 = arr7.astype('bool')
print(arr8.ndim, arr8.dtype)
print('arr8', arr8)











