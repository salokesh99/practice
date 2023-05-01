import copy

#shallow copy
a = [[11,22,33], [1,2,4], [64,345,45]]
b = a.copy()
# b = copy.copy(a)

print(a)
print(b)
a[1][1] = 'AAA'
print(a)
print(b)
a[0][0] = 'Ram'
print(a)
print(b)
a.insert(0, 'Jai Shree Ram')
print(a)
print(b)
a[0] = 'Ram'
print(a)
print(b)
a[1][1] = 'AAA'
print(a)
print(b)
del a[0]
print(a)
print(b)

a[1][1] = 'Not A List'
print(a)
print(b)
a[1] = 'Not A List'
print(a)
print(b)

