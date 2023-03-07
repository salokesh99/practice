# # t = (1,2)
# # print(hash(t))

# if __name__=='__main__':
#     n=int(input('enter value of n\n'))
#     t = map(int, input('enter the numbers\n').split())
#     t = tuple([i for i in t])
#     print(t)
#     print(hash(t))


# Import pandas
import pandas as pd


file_name = "practice/valid_data.xlsx"

filters = {
    "COUPLING-PORT/COMMUNICATION-CONTROLLER" : "P_CEIC_M",
    "Source IP-ADDRESS" : "169.254.17.10",
    "Port COMMUNICATION-DIRECTION" : "IN",
    "Source PORT-NUMBER" : "60000",
    "Target MAC-ADDRESS-STRING" : "01:00:5E:01:00:10",
    "Target IP-ADDRESS" : "239.1.0.16",
    "Target PORT-NUMBER" : "60000"
}


# Load the xlsx file
excel_data = pd.read_excel(file_name)
# Read the values of the file in the dataframe
data = pd.DataFrame(excel_data, columns=["COUPLING-ELEMENT/ECU-INSTANCE","COUPLING-PORT/COMMUNICATION-CONTROLLER",	"VLAN",	"PDU",	"Port COMMUNICATION-DIRECTION",	"HEADER-ID",	"TP-CONFIGURATION",	"Source MAC-UNICAST-ADDRESS",	"Source IP-ADDRESS",	"Source PORT-NUMBER",	"Target MAC-ADDRESS-STRING",	"Target IP-ADDRESS",	"Target PORT-NUMBER"])

# data = pd.DataFrame(excel_data, columns=["HEADER-ID"])

# head = list(data[data['Source IP-ADDRESS'] == '169.254.17.10'])

query_list = []

for key, val in filters.items() :
    unit_query = f'`{key}` == "{val}"'
    query_list.append(unit_query)

executable_query = ' and '.join(query_list)
print('executable_query', executable_query)
# Print the content
# c='Source IP-ADDRESS'
# print("The content of the file is:\n", data[data['Source IP-ADDRESS'] == '169.254.17.10'])
# print("len(headers)-----------------> ", len(head), '\n', head)

data_op = data.query(executable_query)
print("The content of the file is:\n", list(data_op["HEADER-ID"]))






