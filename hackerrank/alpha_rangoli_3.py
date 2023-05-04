n = int(input('enter the val of n- '))
import string
l = list(string.ascii_lowercase)
l.insert(0, '-')
width = n*4-3

# for i in range(1, n+1, 1):
#     # print(list(range(n, n-i, -1)) + list(range((n+2-i),n+1)))
#     a = list(l[n:n-i:-1]) 
#     b = a[::-1][1:]
#     #  list(l[n+2-i:n+1:1])
#     y = '-'.join((a+b))
#     print(y.center(width, '-'))



# for i in range(1, n, 1):
#     y = list(l[n:i:-1])
#     z = y[::-1][1:]
#     # print(y+z)
#     x = '-'.join((y+z))
#     # print(x)
#     print(x.center(4*n-3, "-"))



for i in range(1, n+1, 1):
    # print(list(range(n, n-i, -1)) + list(range((n+2-i),n+1)))
    a = list(l[n:n-i:-1]) 
    b = a[::-1][1:]
    #  list(l[n+2-i:n+1:1])
    y = '-'.join((a+b))
    print(y.center(width, '-'))
    # if i > n :

for i in range(1, n, 1):
    y = list(l[n:i:-1])
    z = y[::-1][1:]
    # print(y+z)
    x = '-'.join((y+z))
    # print(x)
    print(x.center(4*n-3, "-"))

