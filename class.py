#without init function

# class Persona :
#     name = "lokesh"
#
# p = Persona()
# print(p)
# print(p.name)

# ===================>
# class with init function
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# p = Person("lokesh", 29)
# print(p)
# print(p.name, p.age)

# ======================>>
# class with __str__ function

# class with init function
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# 
#     def __str__(self):
#         return f'Name - {self.name}, Age - {self.age}'
# 
# p = Person("lokesh", 29)
# print(p)
# print(p.name, p.age)
# 

# =========================>>>
# class with methods -
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# 
#     def __str__(self):
#         return f'Name - {self.name}, Age - {self.age}'
# 
#     def intro(self):
#         print(f'Hello my name is {self.name}, My age is {self.age}')
# 
# p = Person("lokesh", 26)
# print(p)
# print(p.name, p.age)
# p.intro()

# ============================>>>
#self can be named anything - yourself
class Person:
    def __init__(yourself, name, age):
        yourself.name = name
        yourself.age = age

    def __str__(yourself):
        return f'Name - {yourself.name}, Age - {yourself.age}'

    def intro(yourself):
        print(f'Hello my name is {yourself.name}, My age is {yourself.age}')

p = Person("lokesh", 26)
print(p)
print(p.name, p.age)
p.intro()

#we can modify object values
p.age = 28
p.intro()
# we can delete a parameter
del p.age
try:
    p.intro()
except AttributeError  as err:
    print('no age object', err)
# we can also delete objects
del p

