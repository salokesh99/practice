b = [2,4,3,4,3,2,4,3,2,6,8,2,7,8,9,2,8,9]
b = [1,2,3,6,5,4,4,2,5,3,6,1,6,5,3,2,4,1,2,5,1,4,3,6,8,4,3,1,5,6,2]


# for i in b:
#     x = b.pop()
#     if x in b :
#         continue
#     else:
#         print(x)
#         break
c = set(b)
for i in c:
    if b.count(i) == 1:
        print(i)
