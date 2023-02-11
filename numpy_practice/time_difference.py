import numpy
import time
from datetime import datetime

#excluding declaration

arr = [1,2,3,4,5]
start_time = datetime.now()
for i in arr:
    print(i)
end_time = datetime.now()

arr = numpy.array([1,2,3,4,5])
start_time1 = datetime.now()
for i in arr:
    print(i)
end_time1 = datetime.now()
print("time for normal list ---- %s seconds ---" % (end_time - start_time))
print("time for numpy list  ---- %s seconds ---" % (end_time1 - start_time1))

percentage_diff = 100*((end_time1 - start_time1)/(end_time - start_time))
print('percentage_diff', percentage_diff)