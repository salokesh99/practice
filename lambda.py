sample_func = lambda x : x*2

a = sample_func(5)

print(a)

#===================>>

sample_fumc2 = lambda a,b,c : a*b*c

b = sample_fumc2(2,4,5)

print(b)

# ========================>>>>

def my_func(n):
    return lambda a : a**n

square_finder = my_func(2)
cube_finder = my_func(3)
print("cube_finder", cube_finder)

x= square_finder(5)
y=cube_finder(5)
print("x", x, "y", y)