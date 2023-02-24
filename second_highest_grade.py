# if __name__ == '__main__':
#     total_data = []
#     for _ in range(int(input('enter the no of records - '))):
#         name = input('enter the name of the student - ')
#         score = float(input('enter the marks - '))
#         temp = [name, score]
#         total_data.append(temp)
#
#
# print(total_data)

total_data = [['a', 23.0], ['b', 22.0], ['c', 20.4], ['d', 40.0]]

grades = list(set([ j for i,j in total_data ]))
grades.sort()
second_highest_grade = grades[1]
print(second_highest_grade)

students_with_second_higest_grade = [ i for i,j in total_data if j == second_highest_grade ]
for i in students_with_second_higest_grade :
    print(i)
# print(students_with_second_higest_grade)