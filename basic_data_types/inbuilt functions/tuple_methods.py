import traceback



mt = ()
print(mt)
mt = (1,4,2,3)
print(mt)
print(mt[0])
try:
    mt[1] = 1
    print(mt)
except:
    traceback.print_exc()

mt = 1,2,3,66
print(type(mt))
print(mt[1])

#amazing fact
x = ("shreeram")
print('type(x)--->',type(x))
x = ("shreeram",)
print('type(x)--->',type(x))
#amazing fact2
x = ["shreeram"]
print('type(x)--->',type(x))
x = ["shreeram",]
print('type(x)--->',type(x))

x = "shreeram"
print('type(x)--->',type(x))
x = "shreeram",
print('type(x)--->',type(x))
