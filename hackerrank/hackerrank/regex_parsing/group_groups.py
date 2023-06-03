import re
# p = r'(\w+)@(\w+)\.(\w+)'

# g = re.match(p, 'ajjaloky@gmail.com')

s = '12345678910111213141516171820212223'
p = r'([0-9a-zA-Z])\1+'

i = s
m = re.match(p, i)
print(m)
    # print(m.groups())
print('####################################')
m = re.search(p, i)
print(m)
print(m.groups())

print('####################################')
p = r'[0-9a-zA-Z]+'

m = re.search(p, i)
print(m)
print('####################################')
p = r'([0-9a-zA-Z])+'

m = re.search(p, i)
print(m)
print('####################################')
p = r'([0-9a-zA-Z])\1+'

m = re.search(p, i)
print(m)
print('####################################')
i = '12344445678910213141516171820212223'
p = r'([0-9a-zA-Z])\1+'

m = re.search(p, i)
print(m)
# print(m.groups())

# print(m.group(1)) if m else print('-1')
