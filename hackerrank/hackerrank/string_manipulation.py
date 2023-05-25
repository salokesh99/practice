s = 'rama rama janaki rama!!!'
print(s)
print(s[3])
# s[3] = 'aa'
# print(s)

# 1st approach  
s = list(s)
s[3] = 'aa'
print(s)
s1  = ''.join(s)
print(s1)


# 2nd apprach

# s = s[:3] + [ 'aa' ] + s[5:]
# print(s)
# l = [1,2,4,6,7,8]

a11 = s1.replace('a', 'aa')
print(a11)