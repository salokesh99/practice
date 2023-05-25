a = [1,3,2,5,7,9]
b = [6,3,4,6,3,7,9]

y  = [(i,j) for i in a for j in b]
print(y)

a = [1,3,2,5,7,9]
b = [6,3,4,6,3,7, 9,0]

y  = [(i,j) for i in a for j in b]
print(y)

a = [1,4,9, 3,5,2]
b = [6,3, 9,0,2]

y  = [(i,j) for i in a for j in b]
print(y)