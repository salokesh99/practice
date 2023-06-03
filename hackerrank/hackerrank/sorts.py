chars = sorted(input())
chars.sort(key=lambda x: (x.isdigit(), x.isupper(), x.islower(), x in "24680"))
print(*chars, sep="")

# Enter your code here. Read input from STDIN. Print output to STDOUT
# p = input()

# evn_d = []
# od_d = []
# lwr = []
# upr = []
# for i in p :
#     if i.islower():
#         lwr.append(i)
#     elif i.isupper():
#         upr.append(i)
#     elif int(i)%2 == 0 :
#         evn_d.append(i)
#     else :
#         od_d.append(i)

# lw = ''.join(sorted(lwr)) + ''.join(sorted(upr)) +''.join(sorted(od_d)) + ''.join(sorted(evn_d)) 
# print(lw)
# print("{}{}".format(,''.join(sorted(upr)) )
