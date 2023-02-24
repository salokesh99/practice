# a = input('enter a number from 1 to 10 \n')
# b = input('enter random space separated numbers with count exactly mentioned in input\n')
#
# print('a', a)
# print('b', b)
# c = b.split(' ')
# print('c', c)
# x = []
# for i in c :
#     x.append(int(i))
#
# print('integers list', x)


# ================or we can use a one liner here==============

b = map(int, input('enter the some values\n').split())
# print(dir(b))

arr = [ i for i in b]
# print(type(arr), type(b))
# m = max(arr)
# print(m)
(list(set(arr))).sort()
arr.sort()

print(arr[-2])


# =========================second highest grade=================


