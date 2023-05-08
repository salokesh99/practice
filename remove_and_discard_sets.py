import traceback

s = { 1,2,4,3,7}


print(s.discard(5))
print('======================')
try:
    # print(s.remove(5))
    print(s.remove(5))
except:
    traceback.print_exc()

s = [ 1,2,4,3,7 ]
try:
    print(s.remove(5))
except:
    traceback.print_exc()
# print(s.pop(5))
# print(s.)

