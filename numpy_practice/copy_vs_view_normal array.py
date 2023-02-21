import numpy


# The Difference Between Copy and View
# The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

#slicing copy will not affect the original array
arr = [1,3,5,6,7,8,9,0,1]
#this creates a copy, which is isolated
arr2 = arr[:]
print('arr', arr)
print('arr2', arr2)
arr2[0] = 5
print('arr', arr)
print('arr2', arr2)
if arr == arr2 :
    print('they are same')
else:
    print('they are not same')

#normal copy will affect the original  - it is known as a view of original array.
arr = [1,3,5,6,7,8,9,0,1]
#this creates a view/reference, which is non isolated.
arr2 = arr
#copy operation on normal arrays
arr3 = arr2.copy()

print('arr3', arr3)
print('arr', arr)
print('arr2', arr2)
arr2[0] = 5
print('arr', arr)
print('arr2', arr2)
if arr == arr2 :
    print('they are same')
else:
    print('they are not same')

#there is no view function on normal array
arr = [1,3,5,6,7,8,9,0,1]
# arr5 = arr.view()
# print('arr5', arr5)

