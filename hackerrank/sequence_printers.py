for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    # print((int((bin((2**i)-1))[2:])*i))
    print('============================')
    print(bin(i))
    print(bin(2**i))
    print((bin((2**i)-1)))
    print((bin((2**i)-1))[2:])
    print(int((bin((2**i)-1))[2:])*i)

    
