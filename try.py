# t = (1,2)
# print(hash(t))

if __name__=='__main__':
    n=int(input('enter value of n\n'))
    t = map(int, input('enter the numbers\n').split())
    t = tuple([i for i in t])
    print(t)
    print(hash(t))
