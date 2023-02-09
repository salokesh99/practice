arr = [ 33, 33, 34, 322, 343, 22, 34, 99, 992, -99, -55,545, 0, 23, 5, 3333 ]
print(len(arr))

for i in range(1,len(arr)):
    for j in range (i, 0, -1):
        print('i', i,'j',j)
        if arr[j] > arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:
            break

print(arr)



# for i in range(0, len(arr))