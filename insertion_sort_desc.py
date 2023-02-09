arr = [ 33, 33, 34, 322, 343, 22, 34, 99, 992, -99, -55,545, 0, 23, 5, 3333 ]

for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if  arr[j] > arr[j-1]:
            arr[j-1], arr[j]= arr[j] , arr[j-1]
        else:
            break
print(arr)

