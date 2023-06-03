import re
# # s = 'sadfasaea'
# # p = r'\w+'
# # p = re.match(p,s)
# # print(p.start())
# # print(p.end())
# # print((p.start(), p.end())) if p else print('-1')


# print('#######################1')

s ='aaadaa'

k = 'aa'
# z = ''
# y = [ '[{}]'.format((i)) for i in k ]
# print('y--->',*y)

# p = '(?=({aa}))'

# # p='aa'
# print('p', p)
# x = re.match(p,s)
# # x = re.match(pattern, string)
# x1 = re.search(p,s)
# x2 = re.findall(p,s)
# x3 = re.finditer(p,s)

# print(p.start())
# print(p.end())
# print('x',x)
# print('x1',x1)
# print('x2',x2)
# print('x3',list(x3))
# for i in list(x3):
#     # print('i', i, i.span)
#     print(i.span())
#     print(i.start(), i.end())



# # print((p.start(), p.end())) if p else print('-1')


# Enter your code here. Read input from STDIN. Print output to STDOUT
# import re
# s = input()
# k = input()
# y = [ '[{}]'.format(i) for i in k ]
# print('y',y)
# y = ''.join(y)
# print('y==',y)

# p = r'({})'.format(y)

# print('p', p)
# p = re.finditer(p,s)
# # print(p.start())
# # print(p.end())
# # print((p.start(), p.end())) if p else print('-1')

# for i in list(p) :
#     print('i', i)
#     print(i.span())
    
print('#################with lookahead assertion#######')

k = 'aa'
p = f'(?=({k}))'
m = re.finditer(p, s)

if re.search(k, s):
    for x in m:
        print((x.start(1), x.end(1)-1))
else:
    print((-1, -1))

print('####################without lookahead assertion#####')
print('###############################')

k = 'aa'
p = f'(({k}))'

m = re.finditer(p, s)
if re.search(k, s):
    for x in m:
        print((x.start(1), x.end(1)-1))
else:
    print((-1, -1))

print('####################with lookbehind assertion#####')
print('####################################')

k = 'aa'
p = f'(?<=({k}))'

m = re.finditer(p, s)
if re.search(k, s):
    for x in m:
        print((x.start(1), x.end(1)-1))
else:
    print((-1, -1))