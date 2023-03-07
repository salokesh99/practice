#basic usage of lists

#mutable
#ordered
##allows duplicates

l1 = [ 1, 2, 3, 4, 5, 6, 4, 6]
l2 = ["fish", "banana", "aloo", "papaya", "Tortoise", "ship"]
l3 = [1.5, "banana", "red", 66, True, int]
l4 = ['tortoise', 'Tortoise', 'TORTOISE']

# methods -
# list.append()
# list.copy()
# list.count()
# list.insert()
# list.reverse()
# list.remove()
# list.sort()

# list.pop()
# list.extend()
# list.index()
# list.clear()

# 1] appends an item to the end===============================
# list.append(object)
# print('==================$$$=====================')

# l1.append(4)
# print('l1 append',l1)

# print('==================$$$=====================')

# doesn't take multiple arguments'
#throws TypeError
# l1.append(3,4,5,6)
# print('l1 append',l1)

# 2] copy a list and assign it to next variable==================
# list.copy()

# l = l1.copy()
# print('list after copy - ', l)
#changes made to list copy will not affect original list

# print('==================$$$=====================')

# print('old array before change', l1)
# l[0] = 55
# print('old array after change', l1)
# print('new array after change -', l)
#
# # if you want to ake the shallow copy
# print('shallow copy data - ')
# l = l1
# print('old array before change -', l1)
# l[0] = 55
# print('old array after change -', l1)
# print('new array after change -', l)


# print('==================$$$=====================')

# 3) counts the number of a given 'value' in a list =======================
# list.count(object)

# print('==================$$$=====================')
# val = input('enter the item to find on the list l1 - (only digits) \n')
# c = l1.count(int(val))
# print(f'count of the {val} is - {c}')
# print('==================$$$=====================')

# 4) to insert an element to the list at a given index -
# list.insert(index, object)

# print('==================$$$=====================')
# value = int(input('enter the value to insert\n'))
# index = int(input('enter the index to insert the value\n'))
# l1.insert(index, value )
# print(f'l1 after inserting {value} at {index} ', l1)
# print('==================$$$=====================')

# 5) reverse a string
# l1.reverse()
# print('==================$$$=====================')
# print('l1 before reverse - ', l1)
# l1.reverse()
# print('l1 after reversing - ', l1)
# print('==================$$$=====================')

# 6) remove an element from list, only the first occurance will be removed.
# list.remove()
# print('==================$$$=====================')
# print('l1 - ', l1)
# val = int(input('Enter the value to remove from list - \n'))
# l1.remove(val)
# print('l1 after removing {val} - ', l1)
# print('==================$$$=====================')

# # 7) sort a list in ascending/descending order.

# # list.sort(key, reverse=True/False)
# # print('==================$$$=====================')
# print('l1 - ', l1)
# print('l2 - ', l2)
# print('l3 - ', l3)
# print('l4 - ', l4)

# #without keywords
# l1.sort()
# l2.sort()
# #throws an error, as it contains values which belong to different types
# # l3.sort()
# l4.sort()
# print('After sorting these lists -')
# print('l1 - ', l1)
# print('l2 - ', l2)
# print('l4 - ', l4)

# # with keywords
# l1.sort(reverse=True)
# l2.sort(reverse=True)
# #throws an error, as it contains values which belong to different types
# # l3.sort()
# l4.sort(reverse=True)
# print('After sorting these lists in reverse order -')
# print('l1 - ', l1)
# print('l2 - ', l2)
# print('l4 - ', l4)

# # with keywords we can use sorting in a definitive filters.

#8) extend method 

# l1 = ['a', 'b', 'c']
# l2 = ['e', 'f', 'g']

# l1.extend(l2)
# print('l1 , l2----->', l1, l2)

# # even tuples can be added
# l1 = ['a', 'b', 'c']
# l2 = ('e', 'f', 'g')
# l1.extend(l2)
# print('l1 , l2----->', l1, l2)

# # lets try for sets
# l1 = ['a', 'b', 'c']
# l2 = {'e', 'f', 'g'}
# l1.extend(l2)
# #result is unordered
# print('l1 , l2----->', l1, l2)

#9) remove method - removes first element mentioned

# l1 = ['a', 'b', 'c', 'd', 'e', 'a', 'c']

# l1.remove('a')
# print('l1==>', l1)


# 10) pop method - removes specified index, or last if left blank

# l1 = ['a', 'b', 'c', 'd', 'e', 'a', 'c']
# l1.pop(3)
# print('l1==>', l1)
# l1.pop()
# print('l1==>', l1)

# 11) delete anitem from the list

# l1 = ['a', 'b', 'c', 'd', 'e', 'a', 'c']
# del l1[3]
# print('l1==>', l1)
# del l1
# # throws error
# print('l1==>', l1)

#12) clear the list

l1 = ['a', 'b', 'c', 'd', 'e', 'a', 'c']
# print('l1==>', l1)
# l1.clear()
# # this will not throw the error, just empties the list
# print('l1==>', l1)

l2 = [ x if x in 'abcdef' else 'xx' for x in l1 ]

print(l2)










