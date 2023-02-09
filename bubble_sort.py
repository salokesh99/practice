arr = [ 33, 33, 34, 322, 343, 22, 34, 99, 992, 545, -55, -55, 8769 ]


n=len(arr)-1
m=n
for i in range(0, n) :
    swapped = False
    # print('Iteration - ' , i, 'n', n)
    # print('outer loop arr - ', arr)
    for j in range(0, m) :
        # print('j' , j, 'm', m)
        if arr[j] > arr[j+1] :
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swapped = True
            # print('inner loop arr - ', arr)
    m=m-1
    if swapped == False :
        break
    
    

print(arr)
