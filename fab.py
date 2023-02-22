# fabinocci series = 0, 1,1,2,3,.....for



a = 0
b = 1
print(a )
print(b )

count = 0

while count < 10:
    x = b
    b = a + b
    a = x
    print(b)
    count += 1


