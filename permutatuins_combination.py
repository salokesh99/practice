# A Python program to print all
# permutations using library function
from itertools import permutations

# Get all permutations of [1, 2, 3]
st = 'cat'
s = list(st.split())
print(s)
s = []
for i in st :
    s.append(i)

print(s)

perm = permutations(st)

# Print the obtained permutations
for i in list(perm):
    # print(i)
    x=''
    for j in i:
        x = x+j
    # x = i.join()
    print(x)
#
# # A Python program to print all
# # combinations of a given length
# from itertools import combinations
#
# # Get all combinations of [1, 2, 3]
# # and length 2
# comb = combinations([1, 2, 3], 2)
#
# # Print the obtained combinations
# for i in list(comb):
#     print(i)