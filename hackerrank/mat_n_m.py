# ---------.|.---------
# ------.|..|..|.------
# ---.|..|..|..|..|.---
# -------WELCOME-------
# ---.|..|..|..|..|.---
# ------.|..|..|.------
# ---------.|.---------



# 'ewew'.center(21,'-')


nm= input()
nm = nm.split()
print(nm)
print(nm)
n = int(nm[0])
m = int(nm[1])



s = '.|.'
s1 = 'WELCOME'

for i in range(1,n,2):
    print((s*i).center(m,'-'))
    x = i

print(s1.center(m, '-'))

for i in range(x,0,-2):
    print((s*i).center(m,'-'))
