def factorial(x):

    if x == 1 :
        return 1
    else:
        return (x * factorial(x-1))

number = 6

y = factorial(number)
print(f'factorial of {number} is {y}')
