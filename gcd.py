


def gcd(a, b):

    if a==0:
        return b
    elif b==0:
        return a
    else :
        pass


    while a!=b:
        if a > b:
            a=a-b
        else:
            b=b-a
        print(a, b)
    
    return a



def main():

    a = int(input('Enter the value of A \n'))
    b = int(input('Enter the value of B \n'))

    gcd_val = gcd(a,b)

    print('gcd val of the given numbers is - ', gcd_val)


main()