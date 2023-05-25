from collections import Counter

s = 'eabbcccd'
s = list(s)
s.sort()
c = dict(Counter(s))
print(c)
x = list(c.keys())
x.sort(key=(lambda i : c[i]),reverse=True)
print(*x)