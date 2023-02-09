
# # a function can be assigned as a variable.
# def func1():
#     print(' This is Function 1')
# func2 = func1
# del func1
# func2()

# #a function can be returned from a function
# #1 inbuilt func returns
# def funcret(num):
#     if num == 0 :
#         return sum
#     elif num == 1:
#         return int
#     else:
#         return None
    
# a = funcret(0)

# print(a)

# def funcExecutor(func):
#     print('starting the function funcExecutor!!!')
#     func()
#     print('Func executor executed!!!')

# @funcExecutor


# def func():
#     print('inside the function func....')
#     print('exiting the function!!!')
#traditinal way
# func1 = funcExecutor(func)
# func()

def funcExecutor1(func):
    def executor():
        print('starting the function funcExecutor!!!')
        func()
        print('Func executor executed!!!')
    
    return executor

@funcExecutor1
def func():
    print('inside the function func....')
    print('exiting the function!!!')


func()

