# # import xml.etree.ElementTree as ET

# # def timestamps_by_description(xml, description):
    
# #     root = ET.fromstring(xml)
# #     print(root.tag)
# #     for child in root:
# #         print(child.tag, child.attrib)
# #         print("===",child.find("description").text)
# #         descr = child.find("description").text
# #         if descr == description :
# #             print("found--- ", descr)
# #             print("just attrib type ",type(child.attrib), child.attrib["timestamp"])
# #             timestamp = child.attrib["timestamp"]
    
    
# #     return timestamp

# # xml = """<?xml version="1.0" encoding="UTF-8"?>
# # <log>
# #     <event timestamp="1614285589">
# #         <description>Intrusion detected</description>
# #     </event>
# #     <event timestamp="1614286432">
# #         <description>Intrusion ended</description>
# #     </event>
# # </log>"""
# # print(timestamps_by_description(xml, 'Intrusion ended'))



# import time

# # get the start time
# st = time.time()

# def find_unique_numbers(numbers):
#     unique_list =  []
#     counts_dict = {}
#     for i in numbers :
#         if str(i) in counts_dict :
#             counts_dict[str(i)] += 1
#         else:
#             counts_dict[str(i)] = 1
            
#     print("counts_dict--", counts_dict )
    
#     for key, val in counts_dict.items() :
#         if val == 1 :
#             unique_list.append(int(key))
    
#     return unique_list


# if __name__ == "__main__":
#     print(find_unique_numbers([1, 2, 1, 3]))

# et = time.time()

# print('it took - ', (et-st))


# st1 = time.time()

# def find_unique_numbers1(numbers):
#     non_unique_list =  []
#     counts_dict = {}
#     for i in numbers :
#         if str(i) not in non_unique_list and str(i) not in counts_dict :
#             del counts_dict[str(i)]
#             non_unique_list.append(str(i))

#         else:
#             counts_dict[str(i)] = 1
            
#     lst = list(counts_dict.keys())

#     print("counts_dict--", lst )
#     return lst


# if __name__ == "__main__":
#     print(find_unique_numbers1([1, 2, 1, 3]))

# et1 = time.time()

# print('it took - ', (et1-st1))



# # ====================================================
# import json
# def sort_by_price_ascending(json_string):
    
#     op = json.loads(json_string)
#     print(type(op), op)
#     for i in op:
#         print(i)
    
#     new_op = sorted(op, key = lambda d : d['price'])
#     print("op", new_op)
#     print('strop - ', str(op))
    
#     return str(op)

# print(sort_by_price_ascending('[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]'))

# # ===================================================


class MovingTotal:

    def __init__(self, numbers=[]) -> None:
        self.numbers = numbers
        

    def append(self, numbers):
        """
        :param numbers: (list) The list of numbers.
        """
        # print('numbers', numbers)
        # print('self.numbers', self.numbers)
        if len(self.numbers) == 0 :
            self.numbers = numbers
        else:
            for i in numbers :
                self.numbers.append(i)
        print('numbers after update --- > ')
        print('numbers', numbers)
        print('self.numbers', self.numbers)

        
        
    def contains(self, total):
        """
        :param total: (int) The total to check for.
        :returns: (bool) If MovingTotal contains the total.
        """
        numbers = self.numbers
        # if total in numbers :
        #     print("it is present---", self.numbers, numbers)

        found = False 

        for i in range(0, len(numbers)):
            # if (i+2) < len(numbers) and (i+3)<=len(numbers):
            if (i+3)<=len(numbers):
                t = sum(numbers[i:(i+3)])
                if t == total :
                    print('sum array slice - --- > ', f'numbers[{i}:{(i+3)}]',  numbers[i:(i+3)])
                    found = True
                    return True
        
        if not found :
            return False

                

    
if __name__ == "__main__":
    movingtotal = MovingTotal()
    
    movingtotal.append([1, 2, 3, 4])
    print(movingtotal.contains(6))
    print(movingtotal.contains(3))
    print(movingtotal.contains(12))
    print(movingtotal.contains(7))
    
    movingtotal.append([5])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    print(movingtotal.contains(12))
    print(movingtotal.contains(7))