y = [ i for i in range(10) ]

print(y)

#nested loops
a=1
b=1
c= 2
n=3

y = [ [i,j,k ] for i in range(a+1) for j in range(b+1) for k in range(c+1) ]

z = [ i for i in y if sum(i)!=3]
print(y)
print('z',z)


l1 = ['a', 'b', 'c', 'd', 'e', 'a', 'c']
l2 = [ x if x in 'abcdef' else 'xx' for x in l1 ]

print(l2)