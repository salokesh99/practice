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



# class Person:
#     name = 'Lokesh'
#     age = 29
#     country = 'India'

#     def __init__(self, name, age, country):
#         self.name = name
#         self.age=age
#         self.country=country

    
#     def print_details(self) :
#         print(f'The name of person is - {self.name}, Age - {self.age}, Country - {self.country}')



# # print(Person.age)
# # print(Person.age)
# # print(Person.name)
# p = Person(name = 'Lokesh', age = 29, country = 'India')
# # p=Person()
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

a = dict
print(a)
a = dict()
print('a',a)
b={'a': 1, 'b': 2, 'c': 3}

print('b', b)
a = {
    'a' : 1, 
    'b' : 2, 
    'c' : 3,
    'c' : 4
}

print(a)

#create dict 
mydict = dict(a=1, b=2, c=3)
print(mydict)

for i in a:
    print(type(i))

print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

for i in mydict:
    print(type(i))



# dir()	Returns a list of the specified object's properties and methods
# divmod()	Returns the quotient and the remainder when argument1 is divided by argument2
# enumerate()	Takes a collection (e.g. a tuple) and returns it as an enumerate object
# eval()	Evaluates and executes an expression
# exec()	Executes the specified code (or object)
# filter()	Use a filter function to exclude items in an iterable object
# float()	Returns a floating point number
# format()	Formats a specified value
# frozenset()	Returns a frozenset object
# globals()	Returns the current global symbol table as a dictionary
# hash()	Returns the hash value of a specified object
# help()	Executes the built-in help system
# hex()	Converts a number into a hexadecimal value
# id()	Returns the id of an object
# input()	Allowing user input
# int()	Returns an integer number
# isinstance()	Returns True if a specified object is an instance of a specified object
# issubclass()	Returns True if a specified class is a subclass of a specified object
# iter()	Returns an iterator object
# len()	Returns the length of an object
# list()	Returns a list
# locals()	Returns an updated dictionary of the current local symbol table
# map()	Returns the specified iterator with the specified function applied to each item
# max()	Returns the largest item in an iterable
# memoryview()	Returns a memory view object
# min()	Returns the smallest item in an iterable
# next()	Returns the next item in an iterable
# object()	Returns a new object
# oct()	Converts a number into an octal
# open()	Opens a file and returns a file object
# pow()	Returns the value of x to the power of y
# print()	Prints to the standard output device
# property()	Gets, sets, deletes a property
# range()	Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
# repr()	Returns a readable version of an object
# reversed()	Returns a reversed iterator
# round()	Rounds a numbers
# set()	Returns a new set object
# slice()	Returns a slice object
# sorted()	Returns a sorted list
# staticmethod()	Converts a method into a static method
# str()	Returns a string object
# sum()	Sums the items of an iterator
# super()	Returns an object that represents the parent class
# tuple()	Returns a tuple
# type()	Returns the type of an object
# vars()	Returns the __dict__ property of an object
# zip()	Returns an iterator, from two or more iterators


