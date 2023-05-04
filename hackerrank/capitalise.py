#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    # return s.title()
    temp_str = ''
    s = list(s.split(" "))
    for i in s:
        temp_str += i.capitalize() + ' '
    return temp_str
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input('Enter the string - > \n')

    result = solve(s)

    print('result is ', result)
    # fptr.write(result + '\n')

    # fptr.close()
