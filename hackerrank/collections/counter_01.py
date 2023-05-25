from collections import Counter

total_count = int(input())
sizes = list(map(int, input().split()))
custs = int(input())

x = dict(Counter(sizes))

# print(x)
total_amt = 0
for i in range(custs):
    size_price = list(map(int, input().split()))
    size = size_price[0]
    price = size_price[1]
    # print(size, ' ', price)
    if size in x and x[size] > 0:
        x[size] -= 1
        total_amt += price
    
    
print(total_amt)
