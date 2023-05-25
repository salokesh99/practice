# def calculate_ascii_sum(word):
#     ascii_sum = 0
#     for char in word:
#         ascii_sum += ord(char)
#     return ascii_sum

# # Example usage
# word = input("Enter a word: ")
# total_ascii_sum = calculate_ascii_sum(word)
# print("The total ASCII sum for the word '{}' is: {}".format(word, total_ascii_sum-96))


# def calculate_sum(string):
#     total_sum = 0
#     occurrences = [0] * 27
#     for char in string:
#         if char.isalpha():
#             char_value = ord(char.lower()) - ord('a') + 1
#             # print(char_value, occurrences[char_value])
#             total_sum += char_value + occurrences[char_value]
#             occurrences[char_value] += 26
#     return total_sum

def calculate_sum(string):
    total_sum = 0
    occurrences = [0] * 27
    print(occurrences)
    for char in string:
        print(char)
        if char.isalpha():
            char_value = ord(char.lower()) - ord('a') + 1
            print('char_value', char_value)
            total_sum = (total_sum * 26) + char_value
            print('total_sum', total_sum)
            occurrences[char_value] += 1
            print('occurrences', occurrences)
    
    return total_sum

p = calculate_sum('aba')
print(p)