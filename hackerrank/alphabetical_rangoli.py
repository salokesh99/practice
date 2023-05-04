
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

# print_rangoli(7)




# n = int(input('enter the val of N - '))
# lines = 2*n-1
# import string
# uppercase_letters = list(string.ascii_uppercase)
# width = 4*n - 3

# for i in range(1, lines+1, 1):
#     # if i > n :
#     #     i = lines - i + 1
#     x = '-'.join()
import string
l = list(string.ascii_lowercase)

# print(l[5:4:-1])
# print(l[5:3:-1])
# print(l[5:2:-1])
# print(list(range(5,4,-1)))
# print(list(range(5,3,-1)))
# print(list(range(5,2,-1)))

n = int(input('enter the val of n- '))
# for i in range(1, ((n*2)-1), 1) :
#     print(i)
#     print(l[(n-1):(n-i-1):-1]) 


# generate forward list
for i in range(n, 0, -1):
    print(list(range(n, n-i, -1)))
print("------------------------------")

# generate reverse list
for i in range(0, n+1, 1):
    print(list(range(n, n-i, -1))) 
print("------------------------------")

# generate combined list
for i in range(0, n, 1):
    print(list(range(n, n-i, -1)) + list(range(n-i, n+1, 1))) 


print("--------------this is the one----------------")
l.insert(0, '-')
# generate list without zero
for i in range(1, n+1, 1):

    # print(list(range(n, n-i, -1)) + list(range((n+2-i),n+1)))
    x = list(l[n:n-i:-1]) + list(l[n+2-i:n+1:1])
    y = '-'.join(x)
    print(y)

print("------------------------------")


for i in range(1,n,1):
    print(list(range(n,i,-1)))


print("------------------------------")



for i in range(1, n, 1):
    print(list(range(n-3+i,n+1,1)))

print("------------------------------")

# combined down list
for i in range(1, n, 1):
    print(list(range(n,i,-1)) + list(range(n-3+i,n+1,1)) )

print("------------------------------")

for i in range(1, n, 1):
    # print(list(range(n, n-i, -1)) + list(range((n+2-i),n+1)))
    x = list(l[n:i:-1]) + list(l[n-3+i:n+1:1])
    y = '-'.join(x)
    print(y)

print("------------------------------")
print("------------------------------\n")


# generate list without zero
# n = int(input('enter the val of n- '))

# width = n*4-3
# for i in range(1, n+1, 1):
#     # print(list(range(n, n-i, -1)) + list(range((n+2-i),n+1)))
#     x = list(l[n:n-i:-1]) + list(l[n+2-i:n+1:1])
#     y = '-'.join(x)
#     print(y.center(width, '-'))

# for i in range(1, n, 1):
#     # print(list(range(n, n-i, -1)) + list(range((n+2-i),n+1)))
#     x = list(l[n:i:-1]) + list(l[n-3+i:n+1:1])
#     y = '-'.join(x)
#     print(y.center(width, '-'))






# j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
# f-e-d-c-b-a-b-c-d-e-f
# g-f-e-d-c-b-a-b-c-d-e-f-g
# k-j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j-k


# 3 - 9   *3
# 4 - 13  *3 + 1
# 5 - 17  *3 + 2
# 6 - 21  *3 + 3
# 7 - 25  *3 + 4

# 2*n - 1 + 2*n - 2
# 4*n -3
