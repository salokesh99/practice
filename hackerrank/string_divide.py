# s = 'sesasddadfsfsfds'
# k = 4
# ls = len(s)
# x = ls//k
# print(x)

# # s.split()
# # s.partition(sep)
# # for i in s[::x]:
# #     print(i)
# # print(list(s[::x]))
# for i in range(0, ls, x):
#     # print(s[i:i+x])
#     st = s[i:i+x]
#     temp_str = ''
#     for j in st :
#         if j not in temp_str :
#             temp_str += j
#     print(s[i:i+x], '==>', temp_str)


# def merge_the_tools(string, k):
#     # your code goes here
#     ls = len(string)
#     x = ls//k
#     for i in range(0, ls, x):
#         st = string[i:i+x]
#         temp_str = ''
#         for j in st :
#             if j not in temp_str :
#                 temp_str += j
#         print(string[i:i+x], '==>', temp_str)


# if __name__ == '__main__':
#     string, k = input(), int(input())
#     merge_the_tools(string, k)
# string = 'AAABCADDE'
# string = 'DAABCAAADABA'
# k = 3
# k=4

# ls = len(string)
# # x = ls//k
# for i in range(0, ls, k):
#     st = string[i:i+k]
#     temp_str = ''
#     for j in st :
#         if j not in temp_str :
#             temp_str += j
#     print(temp_str)


#final code 

def merge_the_tools(string, k):
    # your code goes here
    ls = len(string)
    # x = ls//k
    for i in range(0, ls, k):
        st = string[i:i+k]
        temp_str = ''
        for j in st :
            if j not in temp_str :
                temp_str += j
        print(temp_str)

    


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)