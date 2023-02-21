import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  for y in x:
    for z in y:
      print(z)


arr1 = np.array([[[1,2,3], [4,3,2], [1,2,6], [1,2,5]]])
for i in np.nditer(arr1):
    print(i)

print("step - Array iteration with steps!!!!")

for j in np.nditer(arr1[:, ::2]):
    print(j)
    

# Enumerated Iteration Using ndenumerate()
arr4 = np.array([1,2,3])

for idx, x in np.ndenumerate(arr4):
    print("arr", idx, x)

for i, j in np.ndenumerate(arr1):
    print("i, j ", i, j)

