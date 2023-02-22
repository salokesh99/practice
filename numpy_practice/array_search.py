import numpy as np

arr = np.array([1,2,4,3,5,7,3,4,6])

x = np.where(arr==4)

#returns index of element
print(x)


#get the index of even elements

x = np.where(arr%2==0)

#get the index of odd elements
y = np.where(arr%2!=0)

print(x)
print('y--->', y)

# for sorted arrays
arr = np.array([5,6,7,8,9])
x = np.searchsorted(arr, 10 )
print('sorted search index where to put this number ', x)

# what if array is not sorted = Doesn't work
arr = np.array([5,6,7,4, 5, 8, 2, 8,9])
x = np.searchsorted(arr, 4 )
print('sorted search index where to put this number======>>> ', x)

# for sorted arrays
arr = np.array([3,4,5,6,7,8,9])
x = np.searchsorted(arr, 10, side = 'right')
print('sorted search index where to put this number with side ', x)

# for sorted arrays
arr = np.array([3,4,5,6,7,8,9])
x = np.searchsorted(arr, 10, side = 'left')
print('sorted search index where to put this number with side ', x)


# for sorted arrays, multiple items
arr = np.array([3,4,5,6,7,8,9])
x = np.searchsorted(arr, [2,2,4,6])
print('sorted search index where to put this number with side, multiple arrays ', x)