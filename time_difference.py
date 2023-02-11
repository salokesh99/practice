import time
from datetime import datetime

start_time = time.time()
start_time1 = datetime.now()

arr = [1,2,3,4,5]
print(arr)
end_time = time.time()
end_time1 = datetime.now()
print("--- %s seconds ---" % (end_time - start_time))
print("--- %s seconds ---" % (end_time1 - start_time1))
