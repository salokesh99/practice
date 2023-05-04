
# def print_rangoli(size):
#     # your code goes here
#     n = size
#     import string
#     l = list(string.ascii_lowercase)
#     # m = list(string.ascii_uppercase)
#     # s = string.ascii_letters
#     # print('l---------',l)
#     # print('m------------',m)
#     # print('n----------',s)

#     w = (4*n-3)
#     lines = (2*n-1)
#     for row in range(1,lines+1,1):
#         if row>n:
#             row = lines-row+1
#         x = "-".join(l[(n-1):(n-row):-1] + l[(n-row):n])
#         print(x.center(w,"-"))

# print_rangoli(5)



# generate list without zero
n = int(input('enter the val of n- '))
import string
l = list(string.ascii_lowercase)
l.insert(0, '-')
width = n*4-3
for i in range(1, n+1, 1):
    # print(list(range(n, n-i, -1)) + list(range((n+2-i),n+1)))
    x = list(l[n:n-i:-1]) + list(l[n+2-i:n+1:1])
    y = '-'.join(x)
    print(y.center(width, '-'))

for i in range(1, n, 1):
    y = list(l[n:i:-1])
    z = y[::-1][1:]
    # print(y+z)
    x = '-'.join((y+z))
    # print(x)
    print(x.center(4*n-3, "-"))


# for i in range(1, n+1, 1):
#     # print(list(range(n, n-i, -1)) + list(range((n+2-i),n+1)))
#     x = list(l[n:n-i:-1]) + list(l[n+2-i:n+1:1])
#     y = '-'.join(x)
#     print(y)

# for i in range(1, n, 1):
#     # print(list(range(n, n-i, -1)) + list(range((n+2-i),n+1)))
#     # x = list(l[n:i:-1]) + list(l[n-3+i:n+1:1])
#     # y = '-'.join(x)
#     # print(y.center(width, '-'))




# for i in range(1, n, 1):
#     # print(list(range(n-3+i, n+1, 1))) 
#     # print(list(l[n: i:-1]) + list(l[n-3+i:n+1: 1])) 
#     x = list(l[n: i:-1]) + list(l[n-3+i:n+1: 1])
#     y = '-'.join(x)
#     print(y.center(4*n-3, "-"))