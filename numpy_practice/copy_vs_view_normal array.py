import numpy

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

#normal copy will affect the original array
arr = [1,3,5,6,7,8,9,0,1]
#this creates a view/reference, which is non isolated.
arr2 = arr
print('arr', arr)
print('arr2', arr2)
arr2[0] = 5
print('arr', arr)
print('arr2', arr2)
if arr == arr2 :
    print('they are same')
else:
    print('they are not same')
