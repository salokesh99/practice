# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# objectType   |  ordered     |  changeable | allow duplicates
    # List          Yes             Yes           Yes
    # Tuple         Yes             No            Yes
    # set           No              No            No
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
# print('my_dict before change---->', my_dict)
# my_dict.update(sample_dict)
# print('my_dict after change--->', my_dict)
# list_of_tuples = [('a', 15), ('b',15), ('c',15)]
# my_dict.update(list_of_tuples)
# print("list_of_tuples : my_dict_after update============>>>", my_dict)


# Trial of list of lists
# list_of_lists = [['a', 10], ['b',10], ['c',10]]
# list_of_lists_dict = dict(list_of_lists)
# print('list_of_list_dict', list_of_lists_dict)
# my_dict.update(list_of_lists)
# print("list_of_lists: my_dict_after update============>>>", my_dict)

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