import time

# get the start time
st = time.time()

n = 500000
l = list(range(1, n, 2 ))
l.remove(1)

for i in range(0,len(l)//2):
    # print('i',i)
    if i <= len(l)//2:
        for j in range(l[i],l[-1],l[i]):
            # print('len - l1111',len(l), l)
            # print('j',j)
            if j!=l[i] and j in l: 
                l.remove(j)
    else:
        break

# get the end time
et = time.time()
# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
print('len - l',len(l)) #, 'array', l)
