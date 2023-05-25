a = int(input())
b=list(map(int, (input().split())))
c=input()
d=list(map(int, (input().split())))

y = list(set(b) ^ set(d))
y.sort()
for i in y:
    print(i)
