import re

#findall, sub, search, split, finditr, match
s = '''Thank You Sir for your help 
Your lectures are really helpful for understanding the language 
Could you please share re.txt for notes of the chapter
Thanks sir this is really helpful...
I have seen 2 videos 
before yours but couldn't understand anything. You are doing great job for students like me. 
Will you please lend me RE.txt file? it would be great help. Many thanks'''


# x = re.split("s", s)
# y = re.search("[a-d]", s)
# print(x)
# print(y)
# z = re.findall("[a-m]",s)
# print(z)
# a = re.sub("a","b", s)
# print(a)

p=re.split("s", s)
print("Split Results========>", p)
x=re.sub("a","b", s)
print("Substitute results======> ", x)
y=re.search("a", s)
print("search results=======> ", y)
# z=re.match("a",s)
m = 'aaa'
z = re.match("a", m)
print("match Results===>", z)
q=re.findall("o", s)
print("Findall Results===>", q)
f = re.finditer("o", s)
print("find Iter results", f)
for i in f:
    print(i)





