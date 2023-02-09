
s = "tmmzuxt"


current_char_list = []
max_len = 0
count = 0
if len(s) == 0 :
    print(max_len) 
if len(s) == 1 :
    print(max_len) 

for i in range(0, len(s)):
    current_char_list = [s[i]]
    count = 1
    if i+1 < len(s):
        print('i', i, 'i+1', i+1, 'len s ',len(s))
        for j in range(i+1,len(s[i:])+1):
            print('j', j, 'j+1', j+1, 'len s ',len(s))

            print('current_char_list', current_char_list)
            print('j',j)
            if j < len(s) :
                if s[j] in current_char_list :
                    # set_max_count(count, max_len)
                    if count > max_len :
                        max_len = count
                    print('breaking the loop repeated char', s[j])
                    break
                    
                else :
                    count += 1
                    current_char_list.append(s[j])
                    # print('current_char_list', current_char_list)
                    # print('count ', count)
        # set_max_count(count, max_len)
        if count > max_len :
            max_len = count
# set_max_count(count, max_len)
if count > max_len :
    max_len = count
print(max_len)
