from itertools import permutations, combinations
# combinations - is all possible combinations
# permutations - is all possible arrangements of possible combinations, focuses on order as well

a = 'abc'

x = list(combinations(a,3))
print(x)
y = list(permutations(a))
print(y)
print('---------------------------')
x = list(combinations(a,2))
print(x)
y = list(permutations(a))
print(y)
print('---------------------------')
x = list(combinations(a,2))
print(x)
y = list(permutations(a,2))
print(y)

print('=======================================')
a = 'abcd'

x = list(combinations(a,3))
print(x)
y = list(permutations(a))
print(y)
print('---------------------------')
x = list(combinations(a,2))
print(x)
y = list(permutations(a))
print(y)
print('---------------------------')
x = list(combinations(a,2))
print(x)
y = list(permutations(a,2))
print(y)

# =======================================

A = [1,1,3,3,3]

from itertools import combinations, combinations_with_replacement

print(list(combinations_with_replacement(A, 2)))
print('=======================================')
print(list(combinations(A,2)))
print('=======================================')
print(list(permutations(A,2)))
 
 from itertools import groupby