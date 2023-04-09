
a = dict
print(a)
a = dict()
print('a',a)
b={'a': 1, 'b': 2, 'c': 3}

print('b', b)
a = {
    'a' : 1, 
    'b' : 2, 
    'c' : 3,
    'c' : 4
}

print(a)

#create dict 
mydict = dict(a=1, b=2, c=3)
#throws an error
# mydict = dict('a'=1, 'b'=2, 'c'=3)

print(mydict)

for i in a:
    print(type(i))

print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

for i in mydict:
    print(type(i))
