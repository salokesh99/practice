import re


#
# pattern = re.compile("[a-zA-Z\s]+$")
#
#
# print(pattern.search("Hello World"))
# print(pattern.search("hello world"))
# print(pattern.findall("HELLOWORLD"))
# itr = pattern.finditer("HeLlo WORLD")
# for i in itr:
#     print(i)



#3 lowercase letters
#3-5 digits
#a special char
#upto two uppercase chars
#ans
# pattern = re.compile("^[a-z]{3}[\d]{3,5}[@#$%-][A-Z]{0,3}$")
# p= 'asd1212@RZP'
# print(pattern.search(p))


#3 lowercase letters
#3-5 digits
#a special char not pre defined, but definitely not a-zA-Z0-9
#upto two uppercase chars
# pattern = re.compile("^[a-z]{3}[\d]{3,5}[^a-zA-Z0-9]{1}[A-Z]{0,3}$")
# p= 'asd12123$RZP'
# print(pattern.search(p))


# pattern = re.compile("^[a-z.-]{3}[\d.-]{3,5}[@][a-z]{3,7}.com")
#
# s = 'aaa2123@gmail.com'
# print(pattern.search(s))

#emailID
#
# pattern2 = re.compile("^[a-z][1-9a-z\d\.\-_]*@{1}[a-z]+\.com")
# #
# s = 'lokesh.ajja@razorpay.com'
#
# print(pattern2.search(s))

# #whatever char 10 times
# pattern = re.compile("^.{10}$")
# p= 'd12123RZP'
# print(pattern.search(p))



#any char between 45 to 69
# pattern = re.compile("^([5-6][0-9]|[4][5-9])$")
# #any char between 45 to 64
# pattern = re.compile("^([5][0-9]|[4][5-9]|[6][0-4])$")
# #grouping is imprtant
# a = [2,3,24,54,656,3434, 347,34,54,32,43,54, 46,65,75,67,44, 51,49, 60, 34, 69]
# for i in a :
#     print(pattern.search(str(i)))
#

#date Pattern

# pattern = re.compile("^(19|20)[0-9]{2}[\-/](1[0-2]|0[1-9])[\-/](0[1-9]|[1][0-9]|[3][0-1])$")
# a = ['2022-12-13', '1945-23-21', '2012-12-12', '3212-23-32', '2032-11-12', '2022-11-32', '2023-10-00', '2025-00-22', '1912-01-13', '1913-09-09']
# for i in a :
#     print(pattern.search(str(i)))
# 


#avoid all zeroes value 

pattern = re.compile("^(?!0+$)\d+$")
p= '0000000000'
print(pattern.search(p))

#avoid all 1's
pattern = re.compile("^(?!1+$)\d+$")
p= '11111111'
print(pattern.search(p))
