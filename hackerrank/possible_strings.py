def minion_game(string):
    # your code goes here
    l = len(string)
    # w_l = []
    Kevin = 0
    Stuart = 0
    
    for i in range(1, l+1, 1):
        for j in range(0, l, 1):
            if (i+j) > l :
                break
            s = string[j:i+j]
            # w_l.append(s)
            if s.startswith(('A','E','I','O','U')):
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
    string='BANANA'
    minion_game(string)
