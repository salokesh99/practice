import numpy as np

# By reshaping we can add or remove dimensions or change number of elements in each dimension.

arr1 = np.array([1,2,3,4,2,4,6,6,7,8,9,0,3,2,1,3])
print(arr1.shape)
new_arr = arr1.reshape(4,4)
# not possible
# new_arr = arr1.reshape(4,5)
print(new_arr.shape)
print(new_arr)

# if we have enough integers, we can reshape into any dimension

#arr.reshape( total outer count, inner count, elements in each array ) read from end.
arr2 = arr1.reshape(2, 2, 4)
print('arr2', arr2)
arr3 = arr1.reshape(4, 2, 2)
print('arr3', arr3)

print("copy or view - > ", arr3.base)
# it is a view....



# Uknown integer - you can use -1 as unknown elements, calculated on the runtime

newarr = arr1.reshape(2, 2, -1)
print(newarr)


# Flattening array means converting a multidimensional array into a 1D array.
#
# We can use reshape(-1) to do this.

arr4 = arr3.reshape(-1)
print('arr4', arr4)
print(arr4.base)