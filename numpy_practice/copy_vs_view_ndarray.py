# applied = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
# print(f"applied for {applied} cases")
# applied_session2 = 1 + 1 + 1 + 1
#

import numpy as np

#copy function

arr1 = np.array([1,2,3,4,5])
arr2 = arr1.copy()
arr2[2] = 30
print('arr1', arr1)
print('arr2', arr2)

# view function
arr3 = arr1.view()
arr3[2] = 40
arr1[3] = 50
print('arr2', arr2)
print('arr1', arr1)
print('arr3', arr3)

# base parameter can tell us if the data is owned by any element

#returns none as it is a literal copy
print(arr2.base)
#retuens base as it is based on arr1
print(arr3.base)
