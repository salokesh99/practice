# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n = int(input())
Std = namedtuple('Std',input().split())
sums = 0
for i in range(n):
    x = input().split()
    s = Std(*x)
    sums += int(s.MARKS)
print(sums/n)
