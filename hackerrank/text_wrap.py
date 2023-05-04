import textwrap

# Sample Input 0
# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
# Sample Output 0
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

def wrap(string, max_width):
    max_width += 1
    for i in range(1, 1+len(string)//(max_width-1)):
        string = string[:(max_width*i)-1] + '\n' + string[(max_width*i)-1:]
    return string

if __name__ == '__main__':
    string, max_width = input('enter the string-\n'), int(input('enter the width - \n'))
    result = wrap(string, max_width)
    print(result)