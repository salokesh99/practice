# digits = [0, 1, 5]

# for i in digits:
#     print(i)
# else:
#     print("No items left.")



# for i in digits :
#     print(i)
# else:
#     print('Done!!!')


# counter = 0

# while counter < 3:
#     print('Inside loop')
#     counter = counter + 1
# else:
#     print('Inside else')

x = 10
try :
    for i in range(3):
        print(x)
        x += 10
        if x > 30 :
            raise StopIteration
except Exception as e :
    print('error occured', e)

finally:
     print('this is printed after try except.!!!')