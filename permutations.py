from itertools import permutations, combinations

p = permutations([1,2,3])
c = combinations([1,2,3],2)

for i in list(p):
    print(i)
print('Done')

for i in list(c):
    print(i)
