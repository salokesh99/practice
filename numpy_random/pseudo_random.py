from numpy import random

#random integer
x = random.randint(100)
print(x)
#random float
x = random.rand()
print(x)
#create a randint array
x = random.randint(80, 100, size=5)
print(x)
#create 2d arrays
x=random.randint(10, 100, size=(3, 5))
print(x)
#create array of floats
x=random.rand(5)
print(x)
#create nd array of floats
x=random.rand(3,3)
print(x)
#random integers from choices
x=random.choice([3,4,5,6,7,8])
print(x)
# we can include size of an array to get
x = random.choice([1,3,4,5,6,7,8,9], size=(3,3))
print(x)