import traceback
# Method	Description
# add()	Adds an element to the set
# clear()	Removes all elements from the set
# copy()	Returns a copy of the set
# difference()	Returns the difference of two or more sets as a new set
# difference_update()	Removes all elements of another set from this set
# discard()	Removes an element from the set if it is a member. (Do nothing if the element is not in set)
# intersection()	Returns the intersection of two sets as a new set
# intersection_update()	Updates the set with the intersection of itself and another
# isdisjoint()	Returns True if two sets have a null intersection
# issubset()	Returns True if another set contains this set
# issuperset()	Returns True if this set contains another set
# pop()	Removes and returns an arbitrary set element. Raises KeyError if the set is empty
# remove()	Removes an element from the set. If the element is not a member, raises a KeyError
# symmetric_difference()	Returns the symmetric difference of two sets as a new set
# symmetric_difference_update()	Updates a set with the symmetric difference of itself and another
# union()	Returns the union of sets in a new set
# update()	Updates the set with the union of itself and others




# s = set()
# print('........................>>>',s, type(s))
# r = {}
# print('........................>>>',r, type(r))
# s_id = {111,21,323,400,421,403, 50, 3,5}
# print(',,,,,,,,,,,,,,,,,,,,,,>> sid', s_id, type(s_id))
# import traceback
# try:
#     i = s_id[0]
#     print('i--->>>', i)
# except:
#     traceback.print_exc()


# #add and update
# print(',,,,,,,,,,,,,,,,,,,,,,>> sid', s_id)
# s_id.add(3223)
# print(',,,,,,,,,,,,,,,,,,,,,,>> sid', s_id)
# s_id.update({212,3246,21,34,340})
# print(',,,,,,,,,,,,,,,,,,,,,,>> sid', s_id)
# print(sorted(s_id))
# print(enumerate(s_id))
# y = { i : j for i,j in enumerate(s_id) }
# print(',,,,,,,,,,,,,,,,,,,,,,>> Y', y)

# for i in s_id:
#     print(i, end = ', ')
# print('??????????????????????>>>>>>>.',s_id)



# #maths methods

# s1 = {1,3,5,0,9,2,4}
# s2 = {8,6,9,4,3,2,0}

# # perform union operation using |
# print('Union using |:', s1 | s2)
# # perform union operation using union()
# print('Union using union():', s1.union(s2)) 

# # perform intersection operation using  & and intersection
# print('Union using &:', s1 & s2)
# # perform union operation using union()
# print('Union using intersection():', s1.intersection(s2)) 

# # perform intersection operation using  & and intersection
# print('Union using &:', s1 & s2)
# # perform union operation using union()
# print('Union using intersection():', s1.intersection(s2)) 

# # first set
# A = {2, 3, 5}

# # second set
# B = {1, 2, 6}

# # perform difference operation using &
# print('Difference using - :', A - B)

# # perform difference operation using difference()
# print('Difference using difference():', A.difference(B)) 

# # first set
# A = {2, 3, 5}

# # second set
# B = {1, 2, 6}

# # perform difference operation using &
# print('using ^:', A ^ B)

# # using symmetric_difference()
# print('using symmetric_difference():', A.symmetric_difference(B)) 





# 1. remove


# s1 = {1,3,5,0,9,2,4}
# s2 = {8,6,9,4,3,2,0}
# print('..............>>>>>>>>> S1',s1)
# s1.remove(1)
# print('..............>>>>>>>>> S1',s1)
# try:
#     s1.remove(8)
#     print('done')
# except:
#     print('can not remove non existing key')
#     traceback.print_exc()


# 2. add
# s1 = {1,3,5,0,9,2,4}
# s2 = {8,6,9,4,3,2,0}
# print('..............>>>>>>>>> S1',s1)
# s1.add(8)
# print('..............>>>>>>>>> S1',s1)
# s1.add(5)
# print('..............>>>>>>>>> S1',s1)

# d= (1,2,3)
# s1.add(d)
# print('..............>>>>>>>>> S1',s1)
# try:
#     e = [1,2,4]
#     s1.add(e)
#     print('..............>>>>>>>>> S1',s1)
# except :
#     traceback.print_exc()


#3. copy

# s1 = {1,3,5,0,9,2,4}
# s2 = {8,6,9,4,3,2,0}


# s3 = s1.copy()
# print('..............>>>>>>>>> S1, s3',s1,s3)
# s1.add(8)
# print('..............>>>>>>>>> S1, s3',s1, s3)
# s3.remove(5)
# print('..............>>>>>>>>> S1, s3',s1, s3)
# #shows that they are a seperate copies

# s1 = {1,3,5,0,9,2,4}
# s2 = {8,6,9,4,3,2,0}

# #if created like this, it will affext the existing data
# s4 = s1
# print('..............>>>>>>>>> S1, s4',s1,s4)
# s1.add(8)
# print('..............>>>>>>>>> S1, s4',s1, s4)
# s4.remove(5)
# print('..............>>>>>>>>> S1, s4',s1, s4)
# s4.clear()
# print('..............>>>>>>>>> S1, s4',s1, s4)
#shows that they are a seperate copies

# 4. set.difference

# s1 = {1,3,5,0,9,2,4}
# s2 = {8,6,9,4,3,2,0}

# s5 = s1.difference(s2)
# s6 = s2.difference(s1)
# print('..............>>>>>>>>> S5, s6',s5, s6)
# s7 = s1-s2
# s8 = s2-s1
# print('..............>>>>>>>>> S7 s8',s7, s8)


# 5. set.difference_update

# s1 = {1,3,5,0,9,2,4}
# s2 = {8,6,9,4,3,2,0}

# s1.difference_update(s2)
# print('..............>>>>>>>>> s1, s2',s1, s2)
# s2.difference_update(s1)
# s7 = s1-s2
# s8 = s2-s1
# print('..............>>>>>>>>> S7 s8',s7, s8)


# 6. set.intersection

# s1 = {1,3,5,0,9,2,4}
# s2 = {8,6,9,4,3,2,0}
# s3 = { 5, 3, 634, 2, 1, 0}

# p = s1.intersection(s2)
# print('p========================>>>', p)
# p1 = s1.intersection(s2,s3)
# print('p1========================>>>', p1)

# p3 = s1 & s2
# print('p3========================>>>', p3)

# 6. set.intersection_update


# s1 = {1,3,5,0,9,2,4}
# s2 = {8,6,9,4,3,2,0}
# s3 = { 5, 3, 634, 2, 1, 0}

# print('s1========================>>>', s1)
# s1.intersection_update(s2)
# print('s1========================>>>', s1)
# s1.intersection_update(s2,s3)
# print('s1========================>>>', s1)
# s1 = s1 & s2
# print('s1========================>>>', s1)


# 7. set.isdisjoint

# A = {1, 2, 3}
# B = {4, 5, 6}
# C = {6, 7, 8}

# create a set A
# A = {'a', 'e', 'i', 'o', 'u'}

# # create a list B
# B = ['d', 'e', 'f']

# # create two dictionaries C and D 
# C = {1 : 'a', 2 : 'b'}
# D = {'a' : 1, 'b' : 2}


# print('A1========================>>>', A.isdisjoint(B))
# print('A1========================>>>', A.isdisjoint(C))
# print('A1========================>>>', A.isdisjoint(D))

# 8. set.issubset

# # create a set A
# A = {'a', 'e', 'i', 'o', 'u'}

# # create a list B
# B = {'a', 'e', 'o'}

# # create two dictionaries C and D 
# C = {1 : 'a', 2 : 'b'}
# D = {'a' : 1, 'b' : 2}

# print('A1========================>>>', A.issubset(B))
# print('A1========================>>>', B.issubset(A))

# 9. set.pop()

# A = {'a', 'e', 'i', 'o', 'u'}
# print('p========================>>>', A)
# p = A.pop()
# print('p========================>>>', p, A )

# try :
#     a = set()
#     b = a.pop()
# except :
#     traceback.print_exc()


# 10. set.symmetric_difference

# s1 = {1,3,5,0,9,2,4}
# s2 = {8,6,9,4,3,2,0}

# s5 = s1.symmetric_difference(s2)
# s6 = s2.symmetric_difference(s1)
# print('..............>>>>>>>>> S5, s6',s5, s6)
# s7 = s1^s2
# s8 = s2^s1
# print('..............>>>>>>>>> S7 s8',s7, s8)


# 11. set.symmetric_difference_update

# s1 = {1,3,5,0,9,2,4}
# s2 = {8,6,9,4,3,2,0}

# s1.symmetric_difference_update(s2)
# print('..............>>>>>>>>> s1, s2',s1, s2)
# s2.symmetric_difference_update(s1)
# print('..............>>>>>>>>> s1, s2',s1, s2)

# s1 = s1^s2
# s2 = s2^s1
# print('..............>>>>>>>>> S7 s8',s7, s8)
# print('..............>>>>>>>>> s1, s2',s1, s2)

# # 12. set.union

# s1 = {1,3,5,0,9,2,4}
# s2 = {8,6,9,4,3,2,0}

# s5 = s1.union(s2)
# print('..............>>>>>>>>> s5',s5, '\n', s1)
# s6 = s2.union(s1)
# print('..............>>>>>>>>> s6,',s6)

# s7 = s1|s2
# s8 = s2|s1
# print('..............>>>>>>>>> S7 s8',s7, s8)
# print('..............>>>>>>>>> s1, s2',s7, s8)


# 12. set.update

A = {1, 2, 3}
B = {4, 5, 6}
C = {6, 7, 8}

print('..............>>>>>>>>> A',A,B)
A.update(B)
print('..............>>>>>>>>> A',A,B)
B.update(A)
print('..............>>>>>>>>> A',A,B)
D = 'Lokesh'
A.update(D)
print('..............>>>>>>>>> A',A,D)
e = {
    'a':1,
    'b':2,
    'c':3
}
A.update(e)
print('..............>>>>>>>>> A',A,e)




