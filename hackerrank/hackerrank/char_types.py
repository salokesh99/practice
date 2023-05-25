if __name__ == '__main__':
    
    # s = input()
    # s = '$ab30'
    s = '123'
    print('s---------->', s)

    
    # print(s.isalnum())
    # # print(s.isalpha())
    # af = 0
    # for i in s :
    #     if i.isalpha():
    #         print(True)
    #         af = 1
    #         break
    # if not af :
    #     print(False)
    # df = 0
    # for i in s :
    #     if i.isdigit():
    #         print(True)
    #         df = 1
    #         break
    # if not df :
    #     print(False)
    # lf = 0
    # for i in s :
    #     if i.islower():
    #         print(True)
    #         lf = 1
    #         break
    # if not lf :
    #     print(False)
    
    # uf = 0
    # for i in s :
    #     if i.isupper():
    #         print(True)
    #         uf = 1
    #         break
    # if not uf :
    #     print(False)
    
    # print(s.isalnum())
    # alp = 0
    # num = 0
    # for i in s :
    #     if i.isalpha() :
    #         alp = 1
            
    #     if i.isnumeric():
    #         num = 1
            
    #     if alp and num :
    #         print(True)
    #         break
        
    # else:
    #     print(False)

    # af = 0
    # for i in s :
    #     if i.isalpha():
    #         print(True)
    #         af = 1
    #         break
    # if not af :
    #     print(False)
    # df = 0
    # for i in s :
    #     if i.isdigit():
    #         print(True)
    #         df = 1
    #         break
    # if not df :
    #     print(False)
    # lf = 0
    # for i in s :
    #     if i.islower():
    #         print(True)
    #         lf = 1
    #         break
    # if not lf :
    #     print(False)
    
    # uf = 0
    # for i in s :
    #     if i.isupper():
    #         print(True)
    #         uf = 1
    #         break
    # if not uf :
    #     print(False)
    
    
        
if __name__ == '__main__':
    
    s = input()

    # print(s.isalnum())
    alp = 0
    num = 0
    for i in s :
        if i.isalpha() :
            alp = 1
            print(True)
            break
        elif i.isnumeric():
            num = 1
            print(True)
            break
        else:
            pass
            
        
    if not (alp or num) :
        print(False)

    af = 0
    for i in s :
        if i.isalpha():
            print(True)
            af = 1
            break
    if not af :
        print(False)
    df = 0
    for i in s :
        if i.isdigit():
            print(True)
            df = 1
            break
    if not df :
        print(False)
    lf = 0
    for i in s :
        if i.islower():
            print(True)
            lf = 1
            break
    if not lf :
        print(False)
    
    uf = 0
    for i in s :
        if i.isupper():
            print(True)
            uf = 1
            break
    if not uf :
        print(False)
    
    
    
        
    
