import numpy as np

arr = np.array([22,43,11, 45, 54])

filter_array = [True, False, True, True, False]

new_arr = arr[filter_array]
print(new_arr)

# ===========================================
# creating a dynamic filter array

arr1 = np.array([1,4,77,44,66,32,88,54,87,90,32,43])

filter_array1 = []

for i in arr1 :
    if i%2 == 0 :
        filter_array1.append(True)
    else:
        filter_array1.append(False)

print(filter_array1)
new_arr1 = arr1[filter_array1]
print("New array 1", new_arr1)

# =================================================

# creating filter array directly

filter_array2 = arr1<30
filter_array3 = arr%2 != 0

new_arr2 = arr1[filter_array2]
new_arr3 = arr1[filter_array3]

print('new_arr2', new_arr2)
print('new_arr3', new_arr3)