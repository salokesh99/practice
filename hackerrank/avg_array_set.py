def average(array):
    # your code goes here

    arr_set = set(array)
    avg = sum(arr_set)/len(arr_set)
    
    # return "%.3f"%avg
    return "%.2f"%avg



n = 10
array = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174]

a = average(array)
print(a)