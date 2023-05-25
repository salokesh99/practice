import string
from collections import Counter

l = dict([(j,i) for i,j in enumerate((string.ascii_lowercase),1)])
print(l)
# for i in range(1,53):
#     print(l[i])
# s = list(string.ascii_lowercase)
# l = dict.fromkeys(s,range(1,27))
# print(l)
# l = dict(s, range(1,27))
# print(l)

s = 'aa'

# def al_nm(s):
#     s = s[::-1]
#     sm = 0
#     for i in range(len(s)-1,0,-1):
#         # print('u', i, s[i])/\
#         sm += l[s[i]] * 26
#     sm += l[s[0]]
#     print(sm)

def al_nm(s):
    s = s[::-1]
    sm = 0
    for i in range(len(s)):
        sm += l[s[i]] * (26 ** i)
    print(sm)


al_nm(s)
