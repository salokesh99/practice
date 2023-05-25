# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
a = int(input())
b = list(input().split())
k = int(input())

cnt_a = 0
x = list(combinations(b,k))
for i in x :
    if 'a' in i :
        cnt_a += 1

print('%.3f'%(cnt_a/len(x)))

