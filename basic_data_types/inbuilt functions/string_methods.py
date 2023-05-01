import traceback

# Python String Methods
# Python String capitalize()
# Python String center()
# Python String casefold()
# Python String count()
# Python String endswith()
# Python String expandtabs()
# Python String encode()
# Python String find()
# Python String format()
# Python String index()
# Python String isalnum()
# Python String isalpha()
# Python String isdecimal()
# Python String isdigit()
# Python String isidentifier()
# Python String islower()
# Python String isnumeric()
# Python String isprintable()
# Python String isspace()
# Python String istitle()
# Python String isupper()
# Python String join()
# Python String ljust()
# Python String rjust()
# Python String lower()
# Python String upper()
# Python String swapcase()
# Python String lstrip()
# Python String rstrip()
# Python String strip()
# Python String partition()

# Python String maketrans()
# Python String rpartition()
# Python String translate()
# Python String replace()
# Python String rfind()
# Python String rindex()
# Python String split()
# Python String rsplit()
# Python String splitlines()
# Python String startswith()
# Python String title()
# Python String zfill()
# Python String format_map()



# Python String capitalize()
s = 'i am a python Developer'
# print('s----------------------->', s)
# s1 = s.capitalize()
# print('s1-------------------->>', s1)
# print('s----------------------->', s)

# Python String center()
# s = 'i am a python Developer'

# s1=s.center(50,"*")
# print('s1-------------------->>', s1)
# print('s----------------------->', s)
# try:
#     s1=s.center(50,"*#")
#     print('s1-------------------->>', s1)
#     print('s----------------------->', s)
# except:
#     traceback.print_exc()

# s1=s.center(50,"#")
# print('s1-------------------->>', s1)
# print('s----------------------->', s)


# #whitespace is the default
# s1=s.center(50)
# print('s1-------------------->>', s1)
# print('s----------------------->', s)

# s1=s.center(10, '*')
# print('s1--------------------->>', s1)
# print('s----------------------->', s)

# s='pythons'
# s1=s.center(30, '*')
# print('s1--------------------->>', s1)
# print('s----------------------->', s)
# ***********pythons************


# Python String casefold()
#this is similar to lower()
# s = "This is PYTHON"
# s1 = s.casefold()
# print(s1)

# Python String count()
# counts substring

# string.count(substring, start=..., end=...)

# s = "This is PYTHON this is most popular language"
# c = s.count('p')
# print(c)
# c = s.count('P')
# print(c)
# c = s.count('is')
# print(c)
# c = s.count('is', 0, 15)
# print(c)

# Python String endswith()
# str.endswith(suffix[, start[, end]])

# s = "This is PYTHON this is most popular language"
# print(s.endswith('age'))
# print(s.endswith(('age','n ', 'sure'), 0, 15))
# print(s.endswith('age'))
# print(s.endswith(('age','N ', 'sure'), 0, 15))

# Python String expandtabs()

# str = 'xyz\t12345\tabc'

# # no argument is passed
# # default tabsize is 8
# result = str.expandtabs()

# print(result)

# Python String encode()

# string.encode(encoding='UTF-8',errors='strict')
# s = "This is PYTHON this is the most popular language"
# s1 = s.encode(encoding='utf-8', errors='strict')
# print(s1)
# s1 = s.encode(encoding='utf-16', errors='strict')
# print(s1)
# s1 = s.encode(encoding='utf-32', errors='strict')
# print(s1)

# Python String find()
# s = "This is PYTHON. python is the most popular language"
# t = s.find('is')
# print('index of is ->', t )
# t = s.rfind('is')
# print('index of is ->', t )
# # not found cases return -1
# t = s.find('gas')
# print('index of is ->', t )


# q = 'Do small things with great love'
# t = q.find('ing', 10)
# print('index of is ->', t )

# q = 'Do small things with great love'
# t = q.find('ing', 1, 15)
# print('index of is ->', t )

# Python String format()
#positional
# s = '{} is a pragramming language. This is a {} language'.format('python', 'garbage collected')
# print('---------------------------------->>',s)

# try:
#     s = '{1} is a pragramming language. This is a {2} language'.format('python', 'garbage collected')
#     print('---------------------------------->>',s)
# except :
#     traceback.print_exc()


# #numbered
# s = '{0} is a pragramming language. This is a {1} language'.format('python', 'garbage collected')
# print('---------------------------------->>',s)
# s = '{1} is a pragramming language. This is a {0} language'.format('python', 'garbage collected')
# print('---------------------------------->>',s)

# #keywords formatting
# b = 'Hi {name}, your balance is {bal:9.3f}'.format(bal=98999.76382, name = 'Lokesh')
# print("..........", b)
# b = 'Hi {name}, your balance is {bal}'.format(bal=98999.76382, name = 'Lokesh')
# print("..........", b)

# # mixed arguments
# print("Hello {0}, your balance is {blc}.".format("Adam", blc=2300000.2346))


# # numbering formats
# s = 'Hi Ramesh, your balance is : {:d}'.format(100000)
# print(s)
# s = 'Hi Ramesh, your secret char is : {:c}'.format(90)
# print(s)
# num = 100
# s = 'The binary conversion of given number is {:b}'.format(100)
# print(s)
# s = 'hi Lokesh your salary is -Rs {}'.format(95000)
# print(s)
# s = 'hi Lokesh your salary is -Rs {:n}'.format(95000)
# print(s)


# # integer numbers with minimum width
# print("{:5d}".format(12))

# # width doesn't work for numbers longer than padding
# print("{:2d}".format(1234))

# # padding for float numbers
# print("{:8.3f}".format(12.2346))

# # integer numbers with minimum width filled with zeros
# print("{:05d}".format(12))
# # integer numbers with minimum width filled with zeros
# print("{:15d}".format(12))

# # padding for float numbers filled with zeros
# print("{:08.3f}".format(12.2346))

# # padding for float numbers filled with zeros
# print("{:.3f}".format(12.2346))

# # define Person class
# class Person:
#     age = 23
#     name = "Adam"

# # format age
# print("{p.name}'s age is: {p.age}".format(p=Person()))

# # define Person dictionary
# person = {'age': 23, 'name': 'Adam'}

# # format age
# print("{p[name]}'s age is: {p[age]}".format(p=person))

# # define Person dictionary
# person = {'age': 23, 'name': 'Adam'}

# # format age
# print("{name}'s age is: {age}".format(**person))


# Python String index()
# p = 'Ramayana is a Sacred Book'
# i = p.index('is')
# print("..........", i)
# i = p.rindex('is')
# print("..........", i)
# try:
#     i = p.rindex('om')
#     print("..........", i)
# except: 
#     traceback.print_exc()


# i = p.rindex('is', 0,15)
# print("..........", i)
# try:
#     i = p.rindex('is', 15,30)
#     print("..........", i)
# except:
#     traceback.print_exc()


# Python String isalnum()



# string contains either alphabet or number 
# name1 = "Python3"

# print(name1.isalnum()) #True

# name2 = "Lokesh@"

# print(name2.isalnum()) #

# if name1.isalnum() == True :
#     print('yes they are alnumeric')
# else:
#     print('No not alnumeric!!!')


# Python String isalpha()
d = {
'n' : 'monika',
'n1': 'saransh',
'n2': 'Nikhil Manoj',
'n3': 'lokesh.',
'n4': 'lokesh.k4'
}

# for j,k in d.items():
#     print('{} is alphabetic - > '.format(k),k.isalpha())

# s = ''
# print('{} is alphabetic - > '.format(s),s.isalpha())

# # Python String isdecimal()

# s = "28212"
# print(s.isdecimal())

# # contains alphabets
# s = "32ladk3"
# print(s.isdecimal())

# s = "282.12"
# print(s.isdecimal())


# s = '23455'
# print(s.isdecimal())

# #s = '²3455'
# s = '\u00B23455'
# print(s.isdecimal())

# # s = '½'
# s = '\u00BD'
# print(s.isdecimal())

# #isdecimal

# s = '23455'
# print(s.isdigit())


# s = '23.455'
# print('23.455',s.isdigit())

# #s = '²3455'
# # subscript is a digit
# s = '\u00B23455'
# print(s.isdigit())

# # s = '½'
# # fraction is not a digit
# s = '\u00BD'
# print(s.isdigit())


#isnumeric()

# string with superscript 
# superscript_string = '²3455'
# print(superscript_string.isnumeric())

# # string with fraction value 
# fraction_string = '½123'
# print(fraction_string.isnumeric())

# fraction_string = '1.23'
# print(fraction_string.isnumeric())
# fraction_string = '1/23'
# print(fraction_string.isnumeric())

# fraction_string = '123%'
# print(fraction_string.isnumeric())

# Python String isidentifier()

d = {
'n' : '__monika',
'n1': '11saran_sh',
'n2': 'Nikhil Manoj',
'n3': 'lo_kesh.',
'n4': 'lokesh.k4',
'n5': 'lokeshk4'
}

# for i, j in d.items():
#     print('{j}.isidentifier--->'.format(j=j), j.isidentifier())


#python islower

# s = 'this is good'
# print(s.islower())

# s = 'th!s is a1so g00d'
# print(s.islower())

# s = 'this is Not good'
# print(s.islower())

# s = '1234'
# print(s.islower())



# Python String isprintable()
# for i, j in d.items() :
#     print(j, 'is printble', j.isprintable())

# p = 'Python Programming\n'
# print(p, 'is printable', p.isprintable())



# p = ''
# print(p, 'is printable', p.isprintable())


# t = chr(27) 
# print('t--->', t)
# print(t, 'is printable', t.isprintable())

# t = chr(97)
# print('t--->', t)
# print(t, 'is printable', t.isprintable())


# t = chr(27)  + chr(97)
# print('t--->', t)
# print(t, 'is printable', t.isprintable())


#is space

# s = '   \t'
# print(s.isspace())

# s = ' a '
# print(s.isspace())

# s = ''
# print(s.isspace())

# s = ' '
# print(s.isspace())

# s = ' _'
# print(s.isspace())

# s = '45'
# print(s.isascii())
# s = '145'
# print(s.isascii())
# s = 'wer.145'
# print(s.isascii())


# istitle()
# s = 'Python Is Good.'
# print(s.istitle())

# s = 'Python is good'
# print(s.istitle())

# s = 'This Is @ Symbol.'
# print(s.istitle())

# s = '99 Is A Number'
# print(s.istitle())

# s = 'PYTHON'
# print(s.istitle())


#  isupper()
# example string
# string = "THIS IS GOOD!"
# print(string.isupper());

# # numbers in place of alphabets
# string = "THIS IS ALSO G00D!"
# print(string.isupper());

# # lowercase string
# string = "THIS IS not GOOD!"
# print(string.isupper());


# Python String join()
# helper_string.join(iterable)
# d = {
# 's' : ['this', 'is', 'good', 'join'],
# 'p' : ('This', 'is', 'also', 'a', 'good', 'join'),
# 'r' : 'this is not a good join',
# 't' : {'this', 'is', 'a', 'set', 'example'}

# }

# for i, j in d.items():
#     empty_string = ' '
#     joined_string = empty_string.join(j)
#     print(' j is ->',j, 'it is joined\n',  joined_string )


# Python String ljust()

# s = 'cat'
# width = 6
# fc='*'

# print(s.ljust(width))
# print(s.ljust(width, fc))

# s = 'cat'
# width = 6
# fc='*'


#string.rjust

# print(s.rjust(width))
# print(s.rjust(width, fc))

# text = 'Ninja Turtles'

# # width equal to length of string 
# result1 = text.rjust(13, '*')
# print(result1)

# # width less than length of string 
# result2 = text.rjust(10, '*')
# print(result2)


# Python String lower()

# p = ["Python Is a Good Language", 'PTHION', 'python is good' , '234324', '@34###'] 

# for i in p :
#     print(i.lower())

# # Python String upper()

# p = ["Python Is a Good Language", 'PTHION', 'python is good' , '234324', '@34###'] 

# for i in p :
#     print(i.upper())


# Python swapcase

# p = ["Python Is a Good Language", 'PTHION', 'python is good' , '234324', '@34###'] 
# for i in p :
#     print(i.swapcase())


# string.strip([chars])

# Python String lstrip()
# Python String rstrip()
# Python String strip()


# ex = ['this ', ' this ', '   this is food  ', ' 3423 332', 'ramanuja', 'ramanu  jan' ]

# for i in ex :
#     print('i--->>', i)
#     print('i.lstrip()', i.lstrip())
#     print('i.rstrip()', i.rstrip())
#     print('i.strip()', i.strip())



# ex = ['this ', ' this ', '   this is food  ', ' 3423 332', 'ramanuja', 'ramanu  jan' ]

# for i in ex :
#     print('i--------------------------------------->>', i)
#     print('i.lstrip()', i.lstrip('sti'))
#     print('i.rstrip()', i.rstrip('sti'))
#     print('i.strip()', i.strip('sti'))


# for i in ex :
#     print('i---------------##############------------------------>>', i)
#     print('i.lstrip()', i.lstrip('thi'))
#     print('i.rstrip()', i.rstrip('thi'))
#     print('i.strip()', i.strip('thi'))


# for i in ex :
#     print('i---------------$$$$$$$$$$$$$------------------------>>', i)
#     print('i.lstrip()', i.lstrip('stir'))
#     print('i.rstrip()', i.rstrip('stir'))
#     print('i.strip()', i.strip('stir'))


# random_string = '   this is good '

# # Leading whitepsace are removed
# print(random_string.lstrip())

# # Argument doesn't contain space
# # No characters are removed.
# print(random_string.lstrip('sti'))

# print(random_string.lstrip('s ti'))

# website = 'https://www.programiz.com/'
# print(website.lstrip('htps:/.'))


# str.partition()


# p = ["Python Is a Good Language", 'PTHION', 'python is good' , '234324', '@34###'] 

# for i in p :
#     print(i.partition(' '))




# example dictionary
# dict = {"a": "123", "b": "456", "c": "789", 'd':'011'}
# string = "abc"
# print(string.maketrans(dict))

# # example dictionary
# dict = {"a": "123", "b": "456", "c": "789", 'd':'011'}
# string = " "
# print(string.maketrans(dict))

# # example dictionary
# dict = {97: "123", 98: "456", 99: "789"}
# string = "abc"
# print(string.maketrans(dict))\


# dict = {97: "123", 'a': "456", 99: "789"}
# string = "  "
# print(string.maketrans(dict))


# Python String rpartition()

# string.rpartition(separator)

# string = "Python is fun"

# # 'is' separator is found
# print(string.rpartition('is '))

# # 'not' separator is not found
# print(string.rpartition('not '))

# string = "Python is fun, isn't it"

# # splits at last occurence of 'is'
# print(string.rpartition('is'))

# Python String replace()


# s = 'the bat and the ball'
# n_s = s.replace('ba', 'ab')
# print(n_s)
# n_s = s.replace('ba', 'ab', 1)
# print(n_s)



# quote = 'Let it be, let it be, let it be'
# result = quote.find('let it')
# print("Substring 'let it':", result)
# result = quote.rfind('let it')
# print("Substring 'let it':", result)
# result = quote.rfind('small')
# print("Substring 'small ':", result)
# result = quote.rfind('be,')
# if  (result != -1):
#   print("Highest index where 'be,' occurs:", result)
# else:
#   print("Doesn't contain substring")

# s = 'Kahsd sdfksjadflk dfsaf efse sdsd'
# p=s.rfind('dfs')
# print('p---->>>',p)
# quote = 'Do small things with great love'
# # Substring is searched in 'hings with great love'
# print(quote.rfind('things', 10))
# # Substring is searched in ' small things with great love' 
# print(quote.rfind('t', 2))
# # Substring is searched in 'hings with great lov'
# print(quote.rfind('o small ', 10, -1))
# # Substring is searched in 'll things with'
# print(quote.rfind('th', 6, 20))

# Python String rindex()
#index and find are similar, but Index raise exceptions when item is not found

# p = 'Ram was a great personality. He was a all time king!!!'
# q = p.rindex('m')
# print(q)


# quote = 'Do small things with great love'

# # Substring is searched in ' small things with great love' 
# print(quote.rindex('t', 2))

# # Substring is searched in 'll things with'
# print(quote.rindex('th', 6, 20))

# # Substring is searched in 'hings with great lov'
# print(quote.rindex('o small ', 10, -1))


#python split
# str.split(separator, maxsplit)
# str.rsplit([separator [, maxsplit]])

# p = 'Ram was a great personality. He was a all time king!!!'
# q = p.split('a')
# print(q)
# r = p.rsplit('a')
# print(r)


# q = p.split('a',3)
# print(q)
# r = p.rsplit('a',3)
# print(r)
# x = p.split()
# print(x)

# Python String splitlines()

# p = 'Ram was a great personality. He was a all time king!!!'
# q= p.splitlines()
# print(q)
# p = '''Ram was a great personality. 
# He was a all time king
# !!!'''
# q= p.splitlines()
# print(q)
# q= p.splitlines(True)
# print(q)
# q= p.splitlines(0)
# print(q)
# q= p.splitlines(5)
# print(q)


# Python String startswith()
# str.startswith(prefix[, start[, end]])


# p = "Python Is Fun"
# print(p.startswith('Py'))
# print(p.startswith('py'))
# # print(p.startswith())
# print(p.startswith('n ', 5))
# print(p.startswith('N ',5,10))
# print(p.startswith('n ',5,10))

# text = "programming is easy"
# result = text.startswith(('python', 'programming'))

# # prints True
# print(result)

# result = text.startswith(('is', 'easy', 'java'))

# # prints False
# print(result)

# # With start and end parameter
# # 'is easy' string is checked
# result = text.startswith(('programming', 'easy'), 12, 19)
# result = text.endswith(('programming', 'easy'), 12, 19)
# # prints False
# print(result)

#python title()

# t = 'Python DeveloPEr'
# z = t.title()
# print(z)
# text = "He's an engineer, isn't he?"
# print(text.title())
# text = "He's @an #engineer, ?isn't he?--->>> Yes"
# print(text.title())

# Python String zfill()
#fills zeroes if the specified width is more than the string length
# 

# a = '123.456'
# a1 = a.zfill(10)
# print(a1)
# b='+2111'
# a1 = b.zfill(10)
# print(a1)
# b='-2111'
# a1 = b.zfill(10)
# print(a1)
# b='-2111'
# a1 = b.zfill(3)
# print(a1)



# Python String format_map()
# str.format_map(mapping)
# 

point = {'x':4,'y':-5}
print('{x} {y}'.format(**point))

point = {'x':4,'y':-5}
print('{x} {y}'.format_map(point))

point = {'x':4,'y':-5, 'z': 0}
print('{x} {y} {z}'.format_map(point))




