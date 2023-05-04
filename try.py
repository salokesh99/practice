n = int(input('enter n = '))

for i in range(1, n, 1):
    print(list(range(n, i, -1))) 
    y = list(range(n, i, -1))
    z = y[::-1][1:]
    print(z)


# print("------------------------------")
import string
l = list(string.ascii_lowercase)
l.insert(0,'-')
for i in range(1, n, 1):
    y = list(l[n:i:-1])
    z = y[::-1][1:]
    # print(y+z)
    x = '-'.join((y+z))
    print(x)
# print("------------------------------")
import string
l = list(string.ascii_lowercase)
# for i in range(1, n, 1):
#     print(list(l[n:i:-1])) 



# for i in range(1, n, 1):
    # print(list(range(n-3+i, n+1, 1))) 
    # print(list(range(n, i, -1)) + 
    # list(range(n-3+i, n+1, 1))


# for i in range(1, n, 1):
#     print(list(range(n-3+i, n+1, 1))) 

#     # print(list(l[n: i:-1]) + list(l[n-3+i:n+1: 1])) 
#     x = list(l[n: i:-1]) + list(l[n-3+i:n+1: 1])
#     y = '-'.join(x)
#     print(y.center(4*n-3, "-"))

