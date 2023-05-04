def minion_game(string):
    # your code goes here
    l = len(string)
    w_l = []
    Kevin = 0
    Stuart = 0
    vowels = ('A','E','I','O','U')
    
    # for i in range(1, l+1, 1):
    #     for j in range(0, l, 1):
    import itertools
    for i,j in itertools.product(range(1, l+1, 1), range(0, l, 1) ):
            if (i+j) > l :
                continue
            # s = string[j:i+j]
            # print('==>',string[j])
            # w_l.append(s)
            # if s.startswith(('A','E','I','O','U')):
            if string[j] in vowels :
                Kevin += 1
            else :
                Stuart += 1
    
    if Kevin > Stuart :
        print('Kevin {}'.format(Kevin))
    elif Kevin == Stuart :
        print('Draw')
    else:
        print('Stuart {}'.format(Stuart))
        
    # print(w_l, Kevin, Stuart)
    
    
            

if __name__ == '__main__':


#######################
# most efficient  - 
def minion_game(string):
    # your code goes here
    l = len(string)
    # w_l = []
    Kevin = 0
    Stuart = 0
    vowels = ('A','E','I','O','U')
 
    for i in range(0, l, 1):
            if string[i] in vowels :
                Kevin += l-i
            else :
                Stuart += l-i
    
    if Kevin > Stuart :
        print('Kevin {}'.format(Kevin))
    elif Kevin == Stuart :
        print('Draw')
    else:
        print('Stuart {}'.format(Stuart))
        
    # print(w_l, Kevin, Stuart)
    
    
            

if __name__ == '__main__':