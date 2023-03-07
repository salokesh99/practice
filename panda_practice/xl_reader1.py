
# Import pandas
import pandas as pd

def file_handler(file_path, columns, filter_dict):


    try:
        #create an executable query
        query_list = []
        for key, val in filter_dict.items() :
            unit_query = f'`{key}` == "{val}"'
            query_list.append(unit_query)
        executable_query = ' and '.join(query_list)
        # print('executable_query', executable_query)

        # Load the xlsx file
        excel_data = pd.read_excel(file_path)
        # Read the values of the file in the dataframe
        data = pd.DataFrame(excel_data, columns=columns)

        # filter the content using executable query
        data_op = data.query(executable_query)
        #prepare the header_id list
        # print the content of the file to a sample txt file
        with open('output.txt', 'w') as f:
            f.write('Filters - \n')
            f.write(str(filter_dict))
            header_id_list = list(data_op["HEADER-ID"])
            f.write(f'\n length of the header IDs - {len(header_id_list)}')
            f.write("\n Header IDs  - \n")
            f.write(str(header_id_list))
        print('filtered out the data successfully!!!')
    except Exception as err :
        print('Something Went Wrong!!!')
        print("Error - ", err)


#file path 
file_path = "practice/valid_data.xlsx"
#columns of the file
columns=["COUPLING-ELEMENT/ECU-INSTANCE","COUPLING-PORT/COMMUNICATION-CONTROLLER",	"VLAN",	"PDU",	"Port COMMUNICATION-DIRECTION",	"HEADER-ID",	"TP-CONFIGURATION",	"Source MAC-UNICAST-ADDRESS",	"Source IP-ADDRESS",	"Source PORT-NUMBER",	"Target MAC-ADDRESS-STRING",	"Target IP-ADDRESS",	"Target PORT-NUMBER"]
# filters to be added
filter_dict = {
    "COUPLING-PORT/COMMUNICATION-CONTROLLER" : "P_CEIC_M",
    "Source IP-ADDRESS" : "169.254.17.10",
    "Port COMMUNICATION-DIRECTION" : "IN",
    "Source PORT-NUMBER" : "60000",
    "Target MAC-ADDRESS-STRING" : "01:00:5E:01:00:10",
    "Target IP-ADDRESS" : "239.1.0.16",
    "Target PORT-NUMBER" : "60000"
}

file_handler(file_path, columns, filter_dict)