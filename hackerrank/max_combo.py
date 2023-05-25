# Enter your code here. Read input from STDIN. Print output to STDOUT

nm = list(map(int, input().split()))
n = nm[0]
m = nm[1]

def squarer(x):
    return x**2

    
mxrs = 0
for i in range(n):
    ip = list(map(int, input().split()))
    k = ip[0]
    l = ip[1:]
    # print(k,l)
    # print('max', max(l,key=squarer))
    # print(mxrs,  (max(l,key=squarer))**2)
    mxrs += ((max(l,key=squarer))**2)
    

print(mxrs%m)
    



# ==================================
from itertools import combinations, product
a = [5,5, 7, 8, 9, 10 ]
b = [1,6,7,7,9,5]
c = [5,6,8,4,4,9]
y = [3,9,5,3,3]

y = [a,b,c,y]

# print(list(combinations(a,1)))

# for a in list(combinations(a,1)):
#     print(a[0])


# for i in product(a,b):
#     print(i)

# for i in product([a,b,c]):
#     print(i)

# for i in product(a,b,c):
#     print(i)


# x = [a,b,c]
# for i in product(x):
#     print(i)

# x = [a,b,c]
# for i in product(x[:]):
#     print(i)


# x = [a,b,c]
# for i in product(j for j in x):
#     print(i)

# x = (a,b,c)
# for i in product(x):
#     print(i)

# h = sum(sum(j) for j in y)
# print(h)

# for i in product(list(j) for j in y):
#     print(i)

# for i in product(j for j in y):
#     print(i)

# for i in product(j for j in y):
#     print(i)


# print([i for i in y])
# print(list(product( list(combinations(i,1)) for i in y )))



# p = list(product(a,b,c))
# print(p)
print(*y)

# q = list(product(*y))
# print(q)

# # =================================================
# #solution
# # Enter your code here. Read input from STDIN. Print output to STDOUT
# from itertools import combinations, product
# nm = list(map(int, input().split()))
# n = nm[0]
# m = nm[1]

# def squarer(x):
#     x = sum(i**2 for i in x)
#     return x%m

# # lists = []
# cmd = 'product('
# for i in range(n):
#     ip = list(map(int, input().split()))
#     k = ip[0]
#     l = ip[1:]
#     cmd += str(l) + ', '
# cmd += ')'
# # print(cmd)
# x  = list(eval(cmd))
# # print(list(x))

# mx = 0

# for i in x:
#     s = squarer(i)
#     if s > mx :
#         mx = s

# print(mx)


# ==========================================================