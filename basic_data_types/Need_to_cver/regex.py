import re

# ASR_REGEX_PATTERN = re.compile("^[\w\s._,-]*$" )
ASR_REGEX_PATTERN = re.compile("^[\w\s.,-]*$" )

# "^[a-zA-Z1-9\s._\-]*$"



l = [
    'This is a sample LR - 123442',
    'This is, new.',
    'WE Need LR - 1234_1234',
    'New Comment$',
    'New LR - #123',
    'LR is . - _ , 1234'

]

for i in l :
    m = ASR_REGEX_PATTERN.match(i)
    print(m)