# # import csv

# # input_file = csv.DictReader(open("Valid_data.xlsx"))
# # # You may iterate over the rows of the csv file by iterating ove input_file. (Similarly to other files, you need to re-open the file if you want to iterate a second time.)

# # for row in input_file:
# #     print("rows" , row)




# # import all required library
# import xlrd 
# import csv
# # import pandas as pd
  
# # open workbook by sheet index,
# # optional - sheet_by_index()
# file_name = "valid_data.xlsx"
# sheet = xlrd.open_workbook(file_name).sheet_by_index(0)
  
# # writer object is created
# csv_file = file_name.split(".", 1)
# print(csv_file)
# col = csv.writer(open(csv_file[0], 
#                       'w', 
#                       newline=""))
  
# # writing the data into csv file
# for row in range(sheet.nrows):
#     # row by row write 
#     # operation is perform
#     col.writerow(sheet.row_values(row))



#importing pandas as pd
# import pandas as pd



# file_name = "valid_data.xlsx"
  
# # Read and store content
# # of an excel file 
# read_file = pd.read_excel (file_name)
  
# # Write the dataframe object
# # into csv file
# read_file.to_csv ("Test.csv", 
#                   index = None,
#                   header=True)



# # input - 

# Filtered - 

# {
#     "COUPLING-PORT/COMMUNICATION-CONTROLLER" : "P_CEIC_M", 
#     "Source MAC-UNICAST-ADDRESS" : "3C:CE:15:00:00:17"


# }

# O/P

# # in txt format


# {
#     "header_ids" : [ ] 
# }


# Import pandas
import pandas as pd


file_name = "valid_data.xlsx"

# Load the xlsx file
excel_data = pd.read_excel(file_name)
# Read the values of the file in the dataframe
data = pd.DataFrame(excel_data, columns=[])
# Print the content
print("The content of the file is:\n", data)