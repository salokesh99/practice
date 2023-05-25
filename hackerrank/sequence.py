# for i in range(1,int(input('enter the val of n = > '))+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
#     # print(int(''.join(list(map(str, list(range(1,i))+list(range(i,0,-1)))))))
#     print( int((bin(2**i-1))[2:]) **2)

# print('====================================')

# print(type((bin(2**i-1))))

# for i in range(1,int(input('enter the val of n = > '))+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
#     # print(int(''.join(list(map(str, list(range(1,i))+list(range(i,0,-1)))))))
#     print( int((bin(2**i-1))[2:]) * i)


print('====================================')
for i in range(1,int(input('enter the val of n = > '))+1):
    print(((10**i) -1)//9)