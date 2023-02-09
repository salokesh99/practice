arr = [ 33, 38, 34, 322, 343, -22, 34, 99, 99, 545 ]


for inx, item in enumerate(arr):
    if (inx+1) < len(arr) and item > min(arr[(inx+1):]):
        min_index = arr[inx:].index(min(arr[(inx+1):]))
        if inx != 0 :
            min_index = inx + min_index
        arr[inx], arr[min_index] = min(arr[inx:]), arr[inx]


print('arr', arr)

