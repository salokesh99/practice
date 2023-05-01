# Function	Description
#1. abs()	Returns the absolute value of a number

# print(abs(1), abs(-1))
# l = [1,2,4,3,6,5,8]
# for i in l :
#     x = abs(i-10)
#     print('abs of i = ', i , x)


# all()	Returns True if all items in an iterable object are true
# any()	Returns True if any item in an iterable object is true


# l1 = [11, 12, 14, 49, 9]
# l11 = [11, 12, 14, 49, 9, 0]
# l2 = ['a', 'fs', 'ere', 'aaa']
# l21 =  ['a', 'fs', 'ere', 'aaa', '']
# l3 = [True, True, True]
# l31 = [True, True, True, False ]

# print(all(l1))
# print(all(l11))
# print(all(l2))
# print(all(l21))
# print(all(l3))
# print(all(l31))


# ascii()	Returns a readable version of an object. Replaces none-ascii characters with escape character

# print(ascii('aman is my colleague!!!'))
# print('H\xcbllo')
# print(ascii([]))


# ord()	returns an integer representing the Unicode of the specified character
# chr()	Returns a character from the specified Unicode code.

# for i in range(0,127):
# print(ord('a'), end = '')


# print(ord('a'), ord('z'), ord('A'), ord('Z'))
# print(chr(97), chr(122), chr(65), chr(90))


# bin()	Returns the binary version of a number

# print(bin(-100))



# bool()	Returns the boolean value of the specified 

# print(bool(22))
# print(bool(False))
# print(bool('a'))
# print(bool(''))
# print(bool([]), bool(()), bool({}), bool())




# bytearray()	Returns an array of bytes

# if int is given, empty bytearray of that size is created, 
# bytearray(x, encoding, error)
# bytes()	Returns a bytes object


# x = bytes(5)
# y = bytes('abdfgfsg054325', 'utf-16')
# print(x)
# print(y)
# y = bytes('abdfgfsg054325', 'utf-8')
# print(y)


# x= bytearray(5)
# print(x)
# y = bytearray('lokesh', 'ascii', 'replace')
# print(y)
# y = bytearray('lokesh', 'utf-8', 'replace')
# print(y)
# y = bytearray('lokesh', 'utf-16', 'replace')
# print(y)
# y=[1, 2,3 ] 
# z = bytearray(y)
# print(z)



# arr=bytearray(b'abcdef')
# print(arr)
# for i in arr :
#     print(i, chr(i))

# arr2 = bytearray(b'adfsdfddddd')
# print(arr2.count(b'd'))
# print(arr2.count(b'c'))

# a = bytes('abc', 'utf-8')
# b = bytearray('abcdef', 'utf-8')


# print(a)
# print(b)

# # a[0] = 99
# b[1] = 100

# for i in a :
#     print(i)

# print('#################################')


# for i in b:
#     print(i)



# print(a)
# print(b)



# callable()	Returns True if the specified object is callable, otherwise False

# a = 5
# def fi():
#     print('hifi')
# print(callable(a))

# print(callable(fi))



# classmethod()	Converts a method into a class method


# class Students:
#     marks = 0

#     def compute_marks(self, obtained_marks):
#         self.marks = obtained_marks

#         print("Obtained Marks - ", self.marks)



# #convert compute marks to classmethod

# Students.print_marks = classmethod(Students.compute_marks)
# Students.print_marks(88)
# print(Students.print_marks)

# Students.print_marks = Students.compute_marks
# Students.print_marks(88)



# compile()	Returns the specified source as an object, ready to be executed

# Syntax - compile(source, filename, mode)
# The compile() method takes in the following parameters:
# source - a normal string, a byte string, or an AST object
# filename - file from which the code is to be read
# mode - exec (can take a code block with statements, class and functions ), eval (accepts single expression) or single (has a single interactive statement)

# source = 'print("55")'
# filename = 'test'
# mode = 'eval'

# source1 = 'a=55\nb=33\nsum=a+b\nprint(sum)'
# mode1 = 'exec'

# x = compile(source=source1, filename=filename, mode=mode1)
# exec(x)


# complex()	Returns a complex number

# a=20
# print(complex(a))
# a = complex(1,20)
# print(a)
# x = a + 20j
# print(x)
# y = complex('20+29j')
# print(y)

# hasattr()	Returns True if the specified object has the specified attribute (property/method)
# getattr()	Returns the value of the specified attribute (property or method)
# setattr()	Sets an attribute (property/method) of an object
# delattr()	Deletes the specified attribute (property or method) from the specified object


class Person:
    name = 'Lokesh'
    age = 29
    country = 'India'

    def __init__(self, name, age, country):
        self.name = name
        self.age=age
        self.country=country

    
    def print_details(self) :
        print(f'The name of person is - {self.name}, Age - {self.age}, Country - {self.country}')



# # print(Person.age)
# # print(Person.age)
# # print(Person.name)
# p = Person(name = 'Lokesh', age = 29, country = 'India')
# p.print_details()
# # delattr(Person, 'print_details')
# x = hasattr('Person', 'print_details')
# print(x)
# q = hasattr(p, 'Jai Sia Ram')
# y= getattr(p, 'age')
# z = getattr(p, 'print_details')
# p1=getattr(p,'agee', 40)
# s=getattr(p, 'att', 'patt')
# print('x',x)
# print('y', y)
# print('Z', z)
# print('p1', p1)
# print('q',q)
# print('s', s)

# ax = getattr(p, 'agee', 0)
# # print(p.agee)
# setattr(p, 'age', 20)
# setattr(p, 'agee', 20)
# # ax = getattr(p, 'agee', 0)
# print('agee', p.agee)
# delattr(p, 'agee')
# print('agee', p.agee)
# print('ax', ax)
# Person.print_details()
# a = {
#     'a' : 1, 
#     'b' : 2, 
#     'c' : 3
# }
# print(a)
# x = hasattr(a, 'a')
# y = getattr(a, 'a')
# # delattr(a, 'b')
# print('A has a', x)
# print('val of a From A :', y)

# dict()	Returns a dictionary (Array)

# a = dict
# print(a)
# a = dict()
# print('a',a)
# b={'a': 1, 'b': 2, 'c': 3}

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
# print(mydict)

# for i in a:
#     print(type(i))

# print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

# for i in mydict:
#     print(type(i))



# # dir()	Returns a list of the specified object's properties and methods
# d = dir(p)
# print(d)
# print(type(d))


# divmod()	Returns the quotient and the remainder when argument1 is divided by argument2

# a = divmod(10, 2)
# print(a)

# a = divmod(11, 2)
# print(a)


# enumerate()	Takes a collection (e.g. a tuple) and returns it as an enumerate object
# The enumerate() function adds a counter as the key of the enumerate object.
# a = (1,2,3,4,5,2,23,4,2)

# a1 = enumerate(a)
# print(type(a1))
# print(dir(a1))
# for i,j in a1:
#     print(i, j)

# b = [[1,2],[2,2],[3,3], [4,4]]
# a1 = enumerate(b)
# print(type(b))
# print(dir(b))
# for i,j in a1:
#     print(i, j)


# eval()	Evaluates and executes an expression

# eval can't be a last param for multiliner code snippet
# c1 = compile("print(5)\nprint(5+5)", 'test', 'eval')
# eval(c1)
# c2= compile("print(5)\nprint(5+5)", 'test', 'exec')
# eval(c2)

# ex = 'print(5 ** 3)'
# eval(ex)


# exec()	Executes the specified code (or object)
# The exec() function accepts large blocks of code, unlike the eval() function which only accepts a single expression

# ex1 = '''print(5)
# print(5+5)
# '''
# try :
#     eval(ex1)
# except :
#     print('cant do it')
# exec(ex1)




# filter()	Use a filter function to exclude items in an iterable object

# x = [2,1,2,4,5,3,6,7,8,9,4,2,5]

# def filter_function(val):
#     if val%2==0 :
#         return True
#     else:
#         return False
    

# y = filter(filter_function, x )
# print(y)
# y = [i for i in y ]
# print(y)


# def float_filter(val):
#     if isinstance(val, float) :
#         return True
#     else:
#         return False
    
# x = [ 1,2,3,4,4.3,5,6]

# y = filter(float_filter, x)
# for i in x :
#     print(type(i))
# print('y...................... ', y)
# # for i in y:
# #     print(i)
# b = [i for i in y ]
# print(b)




# float()	Returns a floating point number

# a = float("3.5")
# print(a)
# b=float(3)
# print(b)


# format()	Formats a specified value

# y = format(-1222, '+')
# y = format(12/22, '%')
# y = format(1222, 'b')
# y = format(1222, 'd')
# y = format('Ramayana', '>')
# a = format('Ramayana', '<')
# b = format('Ramayana', '^')


# print(y)
# print(a)
# print(b)

# frozenset()	Returns a frozenset object

# make a list unchangeable

# l = [1,2,'4343',342, 'dfsafda']

# print(l[3])
# l[3] = 'Ramayana'
# print(l)
# l = frozenset(l)
# print(l, type(l))
# l[3] = 'Rama'
# print(l, type(l))



# globals()	Returns the current global symbol table as a dictionary
# y = globals()
# print(y)

# hash()	Returns the hash value of a specified object
# class Person:
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name

#     def __eq__(self, other):
#         return self.age == other.age and self.name == other.name

#     def __hash__(self):
#         print('The hash is:')
#         return hash((self.age, self.name))

# person = Person(23, 'Adam')
# print(hash(person))
# print(hash('ramanujan'))



# help()	Executes the built-in help system
# a = 4
# b= 'sanatan Dharma'
# c = [ 1,2,3,4]
# d = ['a', 'b', 'c', 'd']
# x = {
#     'a' : 1,
#     'b' : 2, 
#     'c' : 3
#  }
# help(x)



# hex()	Converts a number into a hexadecimal value

# print(type(hex(200)))

m = { 
'a' : 100,
'b' : 200,
'c' : 300.32,
'd' : 'ddd',
'e' : 12.111,
'f' : 1 + 2j,
'g' : 'sanatan Dharma',
'h' : [ 1,2,3,4],
'i' : ['a', 'b', 'c', 'd'],
'j' : {
  'a' : 1,
    'b' : 2, 
    'c' : 3
 } 
}



# print(hex(f))

# for k,i in m.items() :
#     try :
#         print(hex(i))
#     except Exception as e :
#         print("Error Is - > ", e)

# help(hex)

# print(hex(m['c']))
# print(float.hex(m['c']))


# id()	Returns the id of an object

# #id changes every time you pass it
# for k,i in m.items() :
#     try :
#         print(id(i))
#     except Exception as e :
#         print("Error Is - > ", e)




# input()	Allowing user input




# int()	Returns an integer number
# print(int(9.9))
# try:
#   print(int(9.9))
# except Exception as e :
#     print(e)
  
# try:
#   print(int('9.9'))
# except Exception as e :
#     print(e)



# try:
#   # print(int('8', base=8 ))
#   # print(int('9', 10))
#   print(int('255', base=16))#597
#   print(int(255, base=16))

# except Exception as e :
#     print(e)
  

# print("int(123.23) is:", int(123.23))


# print(float('9.9'))

# print()

# print(int(123))
# print(int(123.233))
# # not possible
# # print(int('123.222'))
# print(int('123'))

# print(bin(125))
# not possible
# print(int(0b1111101, base=2))
# print(int("0b1111101", base=2))

# print(hex(125))
# print(int('0x7d', 16))


# print(oct(125))
# s = oct(125)
# print(f'int of octal val - {s} is - > ',int(str(s), 8))



# isinstance()	Returns True if a specified object is an instance of a specified object

# a = isinstance(m['c'], int)
# print(a)
# a = isinstance(m['c'], float)
# print(a)


# class foo:
#     a = 2

# fooinstance = foo()

# print(isinstance(person, Person))
# print(type(fooinstance))
# print(isinstance(fooinstance, foo))
# print(isinstance(fooinstance, (list, tuple)))
# print(isinstance(fooinstance, (list, tuple,foo)))



# issubclass()	Returns True if a specified class is a subclass of a specified object

# class Polygon:
#   def __init__(polygonType):
#     print('Polygon is a ', polygonType)

# class Triangle(Polygon):
#   def __init__(self):

#     Polygon.__init__('triangle')
    
# print(issubclass(Triangle, Polygon))
# print(issubclass(Triangle, list))
# print(issubclass(Triangle, (list, Polygon)))
# print(issubclass(Polygon, (list, Polygon)))


# iter()	Returns an iterator object
# phones = ['a', 's', 'l', 'N']

# p_itr_obj = iter(phones)

# # for i in p_itr_obj:
# #     print(i)


# print(next(p_itr_obj))
# print(next(p_itr_obj))
# print(next(p_itr_obj))
# print(next(p_itr_obj))
# print(next(p_itr_obj))

# class PrintNumbers:
#     def __init__(self, max):
#         self.max = max

#     #iter method in a class
#     def __iter__(self):
#         self.num = 0
#         return self

#     def __next__(self):
#         if self.num >= self.max :
#             raise StopIteration
#         else :
#             self.num += 1
#             return self.num
        
# pm = PrintNumbers(5)
# p = iter(pm)
# print(p)

# print(next(pm))
# print(next(pm))

# print(next(pm))

# print(next(pm))
# print(next(pm))
# print(next(pm))


# class Doubleit:
#     def __init__(self):
#         self.start = 1
        
#         # return self
#     def __iter__(self):
#         return self
    

#     def __next__(self):
#         self.start = self.start * 2
#         return self.start
    
#     __call__=__next__



# x = Doubleit()

# y = iter(x, 20)
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))


# for i in y :
#     print(i)




# len()	Returns the length of an object
# list()	Returns a list
# s = 'ramayana'
# s = list(s)
# print(s)
# t=[]
# [ t.insert(0,i) for i in s]

# s=''

# # for i in t:
# #     s = s+i 

# x= s.join(t)
 
# print(x)

# print(s,t)

# y = list(m.items())
# z = list(m)

# print(y, z)


# class PowofTwo:
    
#     def __init__(self, max):
#         self.max = max
      
#     def __iter__(self):
#         self.num = 1
#         return self
    
#     def __next__(self):
#         if self.num > self.max:
#             raise StopIteration
#         result = 2 ** self.num
#         self.num += 1

#         return result
    
# a = PowofTwo(5)

# # for i in a :
# #     print(i)
        

# b = list(a)
# print(b)



# class Fabinocci:
    
#     def __init__(self, max) -> None:
#         self.max = max

    
#     def __iter__(self):
#         self.num1 = 0
#         self.num2 = 1
#         return self
    
#     def __next__(self):
#         if self.num1 == 0 :
#           print(self.num1)
#           print(self.num2)
#         if (self.num1 + self.num2) <= self.max :
#           temp = self.num2
#           self.num2 = self.num1 + self.num2 
#           self.num1 = temp
#           print(self.num2)
#           return self.num2
#         else :
#           print("list completed")
#           raise StopIteration
#         # return self.num2


# f = Fabinocci(10)

# x = iter(f)

# # next(x)
# # next(x)
# # next(x)
# # next(x)

# a = list(x)
# print(a)

# locals()	Returns an updated dictionary of the current local symbol table

# s = locals()
# print(s)


# map()	Returns the specified iterator with the specified function applied to each item


# a = ['1','2', '3', '4']

# x=map(int, a)
# z = [1,4,6,8]
# print(x)
# x=list(x)
# print(list(x))
# print(set(a))
# print(tuple(a))


# def square_func(n):
#     return n*n


# y = map(square_func, x)
# print(y)
# z = list(y)
# print(z)

# def product_func(n, m):
#     return n*m

# throws error
# x = [(1,2),(1,3), (10,5)]
# this is ok
# a = [ 1,2,3,4]
# b = [1,2,3,4]
# y = map(product_func, a,b)
# print(y)
# z = list(y)
# print(z)

# l1 = lambda a,b : a+b

# y = x(2,4)
# print(y)

# l = lambda n : 2**n
# s = l(5)
# print(s)

# iterator_obj = map(l1, x,z)
# y = list(iterator_obj)
# print(y)

# max()	Returns the largest item in an iterable
# max(iterable, *iterables, key, default)

# s = [1,2,2,3,4,5,7]
# m = max(s)
# print(m)
# s = ['akash', 'ramesh', 'Hanamantu','Rajarama']
# m = max(s)
# print(m)
# def abs1(n):
#     return abs(n)
# a = [ 1,2,55,-10, -100, 35, -22, 40, -42]
# d = max(a,key=abs1 )
# print(d)

#find max from a dict

d = {
    2: 4,
    6: 8,
    -10 : 55,
    -6 : 100
}


# l = lambda n : d.get(n)
# l1 = lambda n : abs(n) 
# print(l(3), l(2))


# m = max(d)
# print(m)
# m1 = max(d, key=l)
# print(m1)
# l = []

# f=max(l, default=0)
# print(f)
# m = max(1,2,3,4)
# print(m)
# l1 = [1,2,3,4]
# l11 = [42,1,234,412]
# l2 = d
# l3 = {5,3,2,55,5,67,100}

# # print(max(l1,l2,l3))
# print(max(l1, l11))

# l = []

# f=min(l, default=0)
# print(f)
# m = min(1,2,3,4)
# print(m)
# l1 = [1,2,3,4, -22, -232, -112,232]
# l11 = [0,1,234,412]
# l2 = d
# l3 = {5,3,2,55,5,67,100}

# # print(max(l1,l2,l3))
# print(min(l1, l11))

# x = lambda n : abs(n)

# y = min(l1, key=x, default=0)
# print(y)

# print(min(min([1,2,3,1,3,4], [1,2,3, -232, -323,32,232,3454])))



# memoryview()	Returns a memory view object

# rand_byte_arr = bytearray('ABC0123', 'utf-16')

# print(rand_byte_arr)
# mv = memoryview(rand_byte_arr)
# print(mv)
# print(mv[0])
# print(mv[1])
# print(mv[2])
# print(mv[3])
# print(mv[4])


# for i in mv:
#     print(i)


# min()	Returns the smallest item in an iterable
# next()	Returns the next item in an iterable

# l1 = [1,2,4,2,7,5,8,9]
# iter_obj = iter(l1)

# print(next(iter_obj))
# print(next(iter_obj))
# l1 = iter([])
# print(next(l1,0))






# object()	Returns a new object

# o = object()
# some featurelessobject. base for all classes



# oct()	Converts a number into an octal
# o = oct(144)
# print(o)



# # open()	Opens a file and returns a file object
# f = open('a.txt', 'r')
# print(f)
# print(type(f))

# read_file_content = f.read()
# print(read_file_content)


# f.close()


# with open('a.txt', 'r') as f:
    
#     # contents = f.read()
#     # print(contents)
#     # f.write('Shreeram ji is a living legend of the story')
#     c1 = f.read()
#     print(c1)


# pow()	Returns the value of x to the power of y

# p = pow(4,2, 3)
# print(p)


# print()	Prints to the standard output device
# f = open('a.txt', 'a')
# print("abcd", "EFGH", sep="$$$", end='', file=f)



# property()	Gets, sets, deletes a property
# range()	Returns a sequence of numbers, starting from 0 and increments by 1 (by default)


# r = range(5)
# for i in r :
#     print(i, "Hello World")



# repr()	Returns a readable version of an object
m = { 
'a' : 100,
'b' : 200,
'c' : 300.32,
'd' : 'ddd',
'e' : 12.111,
'f' : 1 + 2j,
'g' : 'sanatan Dharma',
'h' : [ 1,2,3,4],
'i' : ['a', 'b', 'c', 'd'],
'j' : {
  'a' : 1,
    'b' : 2, 
    'c' : 3
 } 
}

# a = repr(m)
# print(a)
# for i in m :
#     print(repr(i), repr(m[i]))

# eval(repr(m))

# reversed()	Returns a reversed iterator

# seq = "Python Progaming"
# print(type(seq))
# print(list(reversed(seq)))
# print(type(reversed(seq)))
# print(reversed(seq))

# x = [ i for i in reversed(seq)]
# print(x)

# r = reversed(m)
# print(list(r))


# print(list(reversed(range(10, 0, -1))))

# round()	Rounds a numbers
# m = 13.54534
# n = 13.353443


# r = round(n, 3)
# s = round(n)
# t = round(m)
# print(r)
# print(s)
# print(t)

# set()	Returns a new set object

# l = [1,2,3,1,2,5,6,8,9]
# m = {1,2,34234,234,234,234,25,34,223,34}
# print(set(l))
# print(m)
# print(set(m))
# a = 2.665
# b = 2.675
# print(round(a,2))
# print(round(b,2))

# s = {}
# print(type(s))
# r = set()
# print(type(r))


# #happens due to binary conversions. can be avaided by using str-decimal method


# from decimal import Decimal
# a = Decimal(2.665)
# b = Decimal(2.675)
# print(round(a,2))
# print(round(b,2))
# a = Decimal('2.665')
# b = Decimal('2.675')
# print(round(a,2))
# print(round(b,2))




# slice()	Returns a slice object

# s = "python Programming!!!"
# slice_obj = slice(6, 15, 2)
# t = s[slice_obj]
# print(t)

# print(s[6:15:2])



# sorted()	Returns a sorted list

l = [1,2,3,1,2,5,6,8,9]
# m = {1,2,34234,234,234,234,25,34,223,34}



# print(sorted(l, reverse=True))
# print(sorted(m))


# s = ['ds', 'dsfsdf', 'fsdfsa', 'dsfsf', 'd']
# t = sorted(s, key=len)
# print(t)


# def take_second(n):
#     return n[1]


# s = [(1,3), (4,1), (5,2), (6,4), (9,0)]

# print(sorted(s, key=take_second, reverse=True))


# def abs1(n):
#     return abs(n-50)

# s = [21,23, 50, 60, 30,-23, -55, -23]

# print(sorted(s, key = abs1))

# staticmethod()	Converts a method into a static method

marks = [
    ['Ramesh', 90, 32],
    ['Suresh', 85, 28],
    ['Balaji', 85, 50],
    ['Sumit',  65, 22],
    ['Ashok',  22, 40],
    ['PK',     22, 40]

]

def sort_on_order(data):
    mark = data[1]
    errors = 100-mark
    age = data[2]
    return (errors, age)

p = sorted(marks, key=sort_on_order)
print(p)

# m_list = [
# [90, 32],
# [85, 28],
# [85, 50],
# [65, 22],
# [22, 40],
# [22, 40]
# ]
# n_list = [ (100-i, j) for i,j in m_list]
# p = sorted(m_list)
# print(p)
# q = sorted(n_list)
# print(q)

# def sorters(data):
#     x=100-data[0]
#     y = data[1]

#     return (x, y)

# print(sorted(m_list, key=sorters))

# print(sorted(m_list, key=lambda val : (100-val[0], val[1])))


# str()	Returns a string object
s = "pythön is a programming Language"
print(str('ALOK'))
# print(str(m))
print(str(44))

b = bytes(s, encoding='utf=8')
print(b)

s = str(b, encoding='ascii', errors='ignore')
print(s)
# s = str(b, encoding='ascii', errors='strict')
# print(s)

b=bin(255)
print(b)

# print(str(bytes('\xc3\xb6n', encoding='utf-16')))
print('\xc3\xb6')




# sum()	Sums the items of an iterator
l = [1,2,3,1,2,5,6,8,9]
print(sum(l,10))
#for detailed float sum
import math

s = [12.22, 1.2323, 1.232, 1232.232, 23123, 122.1120009]
x = math.fsum(s)
y= sum(s)
print(x)
print(y)
s1 = [str(i) for i in s]
print(''.join(s1))

# super()	Returns an object that represents the parent class





# tuple()	Returns a tuple
t1 = tuple()
print('t1 =', t1)

# creating a tuple from a list
t2 = tuple([1, 4, 6])
print('t2 =', t2)

# creating a tuple from a string
t1 = tuple('Python')
print('t1 =',t1)

# creating a tuple from a dictionary
t1 = tuple({1: 'one', 2: 'two'})
print('t1 =',t1)


# type()	Returns the type of an object

print(type('lokesh'))

# vars()	Returns the __dict__ property of an object
p=Person(name='Lokesh', age=26, country='India')
print(vars(p))

# zip()	Returns an iterator, from two or more iterators

fruits = ['a', 'b', 'c', 'd', 'e']
counts = [1,3,2,4,6,7]
# counts = []
p =zip(fruits, counts)
x = list(p)
print(x)
# p =zip(fruits)
# l = list(p)
# print('bp-1',l)


# #unzip

l2,k2 = zip(*x)
print(l2, k2)

# print(list(l2))
