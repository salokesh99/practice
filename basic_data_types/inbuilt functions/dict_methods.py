import traceback
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# objectType   |  ordered     |  changeable | allow duplicates
    # List          Yes             Yes           Yes
    # Tuple         Yes             No            Yes
    # set           No              Yes            No
    # dict          NO/Yes          Yes           Key:No/Val:Yes

# *Set items are unchangeable, but you can remove and/or add items whenever you like.
# **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# a = dict
# print(a)
# a = dict()
# print('a',a)
# b={'a': 1, 'b': 2, 'c': 3}
# #declared as a tuple of items
# c = dict((('x',1), ('y',2), ('z',3)))
# #declared as a list of items
# d = dict([('x',1), ('y',2), ('z',3)])

# print(c)




# print('b', b)
# a = {
#     'a' : 1, 
#     'b' : 2, 
#     'c' : 3,
#     'c' : 4
# }

# print(a)

# #create dict 
# mydict = dict(a=1, b=2, c=3)
# mydetails = dict(name='Lokesh', age=26, country='India')

# #throws an error
# # mydict = dict('a'=1, 'b'=2, 'c'=3)

# print(mydict)

# for i in a:
#     print(type(i))

# print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

# for i in mydict:
#     print(type(i))

# print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

# for i in mydetails:
#     print(type(i))

# print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

# #access items 
# print('age',mydetails['age'])
# #throws key error
# # print('agee',mydetails['agee'])

# p=mydetails.get('age')
# #Doesnt throw key error
# q=mydetails.get('agee')
# print('age===>', p)
# print('agee===>', q)


# print(a.keys())
# print(a.values())
# print(a.items())

# update dictionary
my_dict = {
    'a' : 1,
    'b' : 2, 
    'c' : 3,
    'd' : 4
}

sample_dict = {
    'e' : 5,
    'f' : 6, 
    'g' : 7,
    'h' : 8
 }
print('my_dict before change---->', my_dict)
my_dict.update(sample_dict)
print('my_dict after change--->', my_dict)
list_of_tuples = [('a', 15), ('b',15), ('c',15)]
my_dict.update(list_of_tuples)
print("list_of_tuples : my_dict_after update============>>>", my_dict)


# Trial of list of lists
list_of_lists = [['a', 10], ['b',10], ['c',10]]
list_of_lists_dict = dict(list_of_lists)
print('list_of_list_dict', list_of_lists_dict)
my_dict.update(list_of_lists)
print("list_of_lists: my_dict_after update============>>>", my_dict)

list_of_tuples = [('a', 15), ('b',15), ('c',15), ('z',10)]
list_of_lists =  [['a', 10], ['b',10], ['c',10], ['z',11]]
tuples_of_tuples = (('a', 15), ('b',15), ('c',15), ('z',12))
tuple_of_lists =  (['a', 10], ['b',10], ['c',10], ['z',13])

print('my_dict=============>>>>>', my_dict )
my_dict.update(list_of_tuples)
print('my_dict=============>>>>>', my_dict )
my_dict.update(list_of_lists)
print('my_dict=============>>>>>', my_dict )
my_dict.update(tuples_of_tuples)
print('my_dict=============>>>>>', my_dict )
my_dict.update(tuple_of_lists)
print('my_dict=============>>>>>', my_dict )
d = dict(list_of_tuples)
print('d==================> ', d)
d = dict(list_of_lists)
print('d==================> ', d)
d = dict(tuples_of_tuples)
print('d==================> ', d)
d = dict(tuple_of_lists)
print('d==================> ', d)



# ValueError: dictionary update sequence element #1 has length 1; 2 is required
# just_list = ['a', 'b', 'c', 'd']
# my_dict.update(just_list)
# print("my_dict_after update-------------------->>>", my_dict)

# Trial 2
# just_list = ['aa', 'b', 'c', 'd']
# print('length of just list #sequence element #1============>', len(just_list[0]))
# my_dict.update(just_list)
# print("my_dict_after update-------------------->>>", my_dict)
#still failed with  ValueError: dictionary update sequence element #1 has length 1; 2 is required



m = {
    'a' : 1,
    'b' : 2, 
    'c' : 3,
    'd' : 4
}

# 1. clear


# print(m)
# m.clear()
# print(m)


# 2. copy

d = m.copy()

# print(m)
# m['a'] = 'Jai Shree Ram'
# d['b'] = 'Jai Sia Raam'
# print(d)
# print(m)
# print(id(m))
# print(id(d))
# d.clear()
# print(d)
# print(m)

# 3.d.fromkeys

# k = ['a', 'b', 'c', 'd']
# v = 1

# d = dict.fromkeys(k,v)

# print(d)

# v = 2

# print(d)

# v = [ 1]

# d = dict.fromkeys(k,v)

# print(d)

# v = [1,2]

# print(d)
# d = dict.fromkeys(k,v)
# print(d)
# v.append(2)
# print('bbbbb',d)


# l = ['a','b', 'c', 'd','e']

# m = [ 1]
# dn = dict.fromkeys(l, m)
# print(dn)

# m.append(2)
# print(dn)

# # set of vowels
keys = {'a', 'e', 'i', 'o', 'u' }

# # list of number
# value = [1]

# vowels = dict.fromkeys(keys, value)
# print(vowels)

# # updates the list value
# value.append(2)

# print(vowels)




# k= keys
# v = [1]
# d = { key : v for key in keys }
# print(d)
# v.append(0)
# print(d)


# #dict.setdefault(key, default_val)


# d = {
#     'name': 'Lokesh', 
#     'age' : 26,
#     'city' : 'Hyd'
# }


# print('d - > ', d)
# rv = d.setdefault('age', 28)
# print('rv--->', rv)
# print('d.....>>>>...', d)
# rv = d.setdefault('ageee', 28)
# print('rv--->', rv)
# print('d.....>>>>...', d)

# #pop
# import traceback
# x = d.pop('city')
# print('x->', x, 'dddd - > ',d)
# try: 
#     x = d.pop('cityyyyy')
#     print('x->', x, 'dddd - > ',d)
# except  :
#     print('e--->>>')
#     traceback.print_exc()


# x = d.pop('cityyyyy', "city not found!!!")
# print('x->', x, 'dddd - > ',d)


# ds = d.popitem()
# print('ds........', ds)
# c = {}
# # dc = c.popitem()
# # print('dc...........>>>', dc)


# print(c)
# x = c.setdefault('name', "Lokesh")
# print(c)
# print(x)

# #update


# d = {'a':1,'b':2}
# d.update({'b':5})
# print(d)
# d.update({'r':55})
# print(d)
# try:
#     d.update((1,2))
#     print(d)
# except:
#     traceback.print_exc()

# d.update([(1,2)])
# print(d)



try:
    d.update(((11,2)))
    print(d)
except:
    print("can't add ((11,2))")
    traceback.print_exc()


try:
    d.update(((11,2),))
    print('Type==============>>>',type(((11,2),)))
    print('Type===============>>>',type(((11,2))))
    print(d)
except:
    traceback.print_exc()


# try:
#     d.update(11,2)
#     print(d)
# except:
#     traceback.print_exc()

# try:
#     d.update([11,2])
#     print(d)
# except:
#     traceback.print_exc()

try:
    d.update([(11,2)])
    print(d)
except:
    traceback.print_exc()




try:
    d.update([(11,2), (12, 13)])
    print(d)
except:
    traceback.print_exc()

