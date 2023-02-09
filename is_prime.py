n = 50000 


def isPrime(n):
    for i in range (2, n//2 ):
        if n%i==0:
            return False
    return True


x = isPrime(n)
print('Is n Prime ?', x)