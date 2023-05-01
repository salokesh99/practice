p = 10

def double(n):
    global total
    total = 10
    if total >100:
        total = 0
        return 'reset now'
    
    return total



x = 20
total = 20
x = double(p)
print(total)
print(x)

