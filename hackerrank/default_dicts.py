from collections import defaultdict

d = defaultdict(list)

n_m = list(map(int, input().split()))
n = n_m[0]
m = n_m[1]

for i in range(1,n+1):
    x = input()
    d[x].append(i)

for i in range(m):
    y = input()
    op = d[y] if d[y] != [] else [-1]
    print(*op)