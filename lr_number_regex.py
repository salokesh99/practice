import re

s = "000000011"


# patt = re.compile("^(?!0+$)\d{8,12}$")
p="^(?!0+$)\d{8,12}$"
m = re.match( p, s)
if m :
    print("Value exists", m)
else:
    print("No val Exists!!!")