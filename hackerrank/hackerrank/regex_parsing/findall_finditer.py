# import re
# p = r'[a|e|i|o|u|A|E|I|O|U]+'

# i = 'rabcdeefgyYhFjkIoomianpOeorteeeeet'
# i = 'escapespecialcharacters'

# # x = re.findall(p, i)
# x = re.finditer(p, i)
# # print(x)
# for i in x:
#     if len(i.group()) > 1 :
#         print(i.group()) 

# if not x :
#     print(-1)

# print('######################################1')
# vowels = r'aeiouAEIOU'
# # p = r'[^aeiouAEIOU][aeiouAEIOU]{2,}[^aeiouAEIOU]'
# p = r'[^{vowels}][{vowels}]{2,}[^{vowels}]'


# i = 'aaarabcdeefgyYhFjkIoomnpOeorteeeeet'
# # i = 'escapespecialcharacters'

# x = re.findall(p, i)
# # x = re.finditer(p, i)
# print(x)
# for i in x:
# #     if len(i.group()) > 1 :
#     print(i)

# # if not x :
# #     print(-1)

# print('######################################2')

# p = r'[^aeiouAEIOU][aeiouAEIOU]+[^aeiouAEIOU]'

# i = 'aaarabcdeefgyYhFjkIoomnpOeorteeeeetuuuu'

# x = re.findall(p, i)
# # x = re.finditer(p, i)
# print(x)
# for i in x:
# #     if len(i.group()) > 1 :
#     if len(i[1:-1]) > 1:
#         print(i[1:-1])

# print('######################################3')

# import re
# p = r'[^aeiouAEIOU][aeiouAEIOU]+[^aeiouAEIOU]'
# # i = input()
# i = 'escapespecialcharacters'

# x = re.findall(p, i)
# print('x---->>>', x)
# for i in x:
#     if len(i[1:-1]) > 1:
#         print(i[1:-1])

# if not x:
#     print('-1')


# print('######################################4')

# import re
# p = r'[^aeiouAEIOU][aeiouAEIOU]{2,}[^aeiouAEIOU]'
# # i = input()
# i = 'escaeeiapesOOOpecialciahaoOoracters'
# i='escapespecialcharaaacters'

# x = re.findall(p, i)
# print('x---->>>', x)
# for i in x:
#     print('==============>',i)


# if not x:
#     print('-1')

import re
p = r'(?<=[^aeiouAEIOU])[aeiouAEIOU]{2,}(?=[^aeiouAEIOU])'

i = 'escaeeiape sOOOpecialc iahaoOoracters'
# i='escapespecialcharaaacters'

x = re.findall(p, i)
print('x---->>>', x)
for i in x:
    print('==============>',i)


if not x:
    print('-1')