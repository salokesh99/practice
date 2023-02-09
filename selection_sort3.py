arr = [ 33, 38, 34, 322, 343, -22, 34, 99, 99, 545 ]


for i in range(0,len(arr)-1):
    for j in range(i+1 , len(arr)):
        if arr[i] > arr[j] :
            arr[i], arr[j] = arr[j], arr[i]



print(arr)

