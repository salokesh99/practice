l = 6
List1 = list(range(1, l+1, 1))
List2 = list(range(0, l, 1))
w_l = []
w_l1 = []
string = 'BANANA'

import itertools
for i,j in itertools.product(List1, List2):
    print(j,i+j, end = ', ')
    if (i+j) > l :
        continue
    s = string[j:i+j]
    w_l.append(s)

print('\n==================================')
print(w_l)
print('\n==================================')


for i in range(1, l+1, 1):
    for j in range(0, l, 1):
        print(j,i+j, end = ', ')
        if (i+j) > l :
            break
        s = string[j:i+j]
        w_l1.append(s)


print('\n==================================')
print(w_l1)
print('\n==================================')
