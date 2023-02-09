import time

# get the start time
st = time.time()

n = 500000
l = list(range(1, n, 2 ))
l[0] = 2
d = l[-1]//2
# print(l)
for i in range(1,d):
    # for j in l[i+1:]:
        # if j%l[i] == 0 :
            # l.remove(j)
    # print('i', i, 'l', l)
    if i < len(l) :
        for j in range(2*l[i], n, l[i]) :
            # print(j)
            if j%2 != 0  and j in l :
                l.remove(j)
print(len(l))

# get the end time
et = time.time()
# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')



