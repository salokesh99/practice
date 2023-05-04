# a = 'ssd'
# b='fsda7dfggd'

# print(a.capitalize())
# print(b.upper())



def print_rangoli(size):
    # your code goes here
    n = size
    import string
    l = list(string.ascii_lowercase)
    m = list(string.ascii_uppercase)
    s = string.ascii_letters
    print('l---------',l)
    print('m------------',m)
    print('n----------',s)

    w = (4*n-3)
    lines = (2*n-1)
    for row in range(1,lines+1,1):
        if row>n:
            row = lines-row+1
        x = "-".join(l[(n-1):(n-row):-1] + l[(n-row):n])
        print(x.center(w,"-"))

print_rangoli(3)