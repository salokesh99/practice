from operator import index


arr = [ 33, 33, 34, 322, 343, 22, 34, 99, 992, 545 ]
count=-1
for i in arr:
    # print(arr.index(i))
    count+=1
    print('arr', arr, 'min', min(arr[count:]), 'i', i, 'count', count)
    if min(arr[count:]) < i :
        print('arr1', arr)
        # arr[count], arr[arr.index(min(arr[count:]))] = min(arr[count:]), arr[count]
        # arr[count] = 1
        min_index=arr[count:].index(min(arr[count:]))
        print('count', count, 'min(arr[count:]', min(arr[count:] ))
        print('count', count, 'min_index', min_index)
        arr[min_index], arr[count] = arr[count], min(arr[count:])

        print('arr2', arr)
    
        # print(arr[arr.index(min(arr[count:]))])

#         break
    
# print(arr)
# print(arr.index(min(arr[count:])))
# arr[arr.index(min(arr[count:]))] = 443
# print(arr)
# min_index=arr.index(min(arr[count:]))
# arr[min_index] = 442
print(arr)
# print(arr)