import string

#  a = 1
# b = 2
# c = 3
# .
# .
# .
# z = 26

# aa = 27
# ab = 28
# ...
# az = 52
# ba = 53
# .
# .
# .

# zz = 


# # given an ip - ba - return 53

# print(chr(97))
# # print('a'.ascii_uppercase())
# # s = 'abc'
# # for i in s.ascii_u

# for i in string.ascii_letters:
#     print(i, end=' ')

# print(ord('a'))


# s = 'aa'
# number = 0
# # s = s[::-1]
# for i, j in enumerate(s):
#     print(i, j)
#     number += ord(j) + (i * 26 * (ord(j)-96) )

# print('number ', number-193)
# # print(96+71+26)

# a =


a='pythonprogram'
b='itspythoninterview'
c='itspythonprograminterview'
# a&b = python
# b&c= interview
# print(a&b)

st = a



l = []

# for i in st :
#     print(i)


for i in range(len(st)):
    # print('st[i]',st[i])
    for j in range(0, i):
        print('st[j]',st[j])
    print('done')
