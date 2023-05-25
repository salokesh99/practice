# from collections import deque

# def pyr_maker(l):
#     s = [4, 3, 2, 1, 3, 4 ]
#     s = deque(s)
#     for i in range(len(s)):
#         m = max(s)
#         if len(s) <= 2 :
#             print('Yes')
#             break
#         if s[0] == m :
#             s.popleft()
#         elif s[-1] == m :
#             s.pop()
#         else :
#             print('No')
#             break
        
# pyr_maker('')

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque

# def pyr_maker(l):
#     s = deque(l)
#     for i in range(len(s)):
#         m = max(s)
#         if len(s) <= 2 :
#             print('Yes')
#             break
#         if s[0] == m :
#             s.popleft()
#         elif s[-1] == m :
#             s.pop()
#         else :
#             print('No')
#             break
    
# t = int(input())
# for i in range(t):
#     n = int(input())
#     l = list(map(int, input().split()))
#     pyr_maker(l)



# def pyr_maker(l):
#     s = deque(l)
#     lft = s[0]
#     rgt = s[-1]
#     mx = max(lft, rgt)
#     for i in range(len(s)):
#         if len(s) <= 2 :
#             print('Yes')
#             break
#         elif lft == mx :
#             s.popleft()
#             mx = lft
#         elif rgt == mx:
#             s.pop()
#             mx = rgt
#         elif mx < lft and mx < rgt :
#             print('No')
#             break
#         else:
#             continue

        

    
# t = int(input())
# for i in range(t):
#     n = int(input())
#     l = list(map(int, input().split()))
#     pyr_maker(l)


# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

t = int(input())

def pyr_maker(x, y):
    y = deque(y)
    l = y[0]
    u = y[-1]
    mx = max(l, u)
    
    for i in range(x):
        l = y[0]
        u = y[-1]
        if not (l <= mx and u <= mx ):
            print('No')
            break
        if l <= u :
            y.popleft()
            mx = u
        elif u <= l :
            y.pop()
            mx = l
        else:
            pass
        if len(y) == 1 :
            print('Yes')
            break


for i in range(t):
    x = int(input())
    y = list(map(int, input().split()))
    pyr_maker(x,y)