from deliverycenters.ext_srv_cache import *
import json
import csv
from kafka import KafkaProducer
import settings
import time
import traceback
import logging

log_level = logging.INFO
logging.basicConfig(level=log_level)
log = logging.getLogger('kafka')
log.setLevel(log_level)

# prod = {
#     "KAFKA_URL": ['prod-dwh-kafka-1.delhivery.com:9092','prod-dwh-kafka-2.delhivery.com:9092','prod-dwh-kafka-3.delhivery.com:9092'],
#     "KAFKA_TOPIC": "dynamo-serviceability.info",
#     "NEW_KAFKA_TOPIC": "Dynamo-Newserviceability.info",
# }

# dev = {
#     "KAFKA_URL": ["dwh-dev-kafka-msk.delhivery.com:9092"],
#     "KAFKA_TOPIC": "dynamo-serviceability.info",
#     "NEW_KAFKA_TOPIC": "dynamo-newserviceability.info",
# }


#helper funcytions to stringify th data
def stringify_dwh_data(data):

    for value in data:
        if isinstance(data.get(value), list):
            data[value]= str(data.get(value))
    return data


def pre_process_dwh_data(data):

    for key in data:
        if key in ['pin','action_date']:
            continue
        data.update({key:stringify_dwh_data(data.get(key))})
    return data


#create Kafka client
def get_kafka_client():
    """
    Uncomment the dev/prod data based on the requirements
    """
    #for dev - KAFKA_URL
    # producer = KafkaProducer(bootstrap_servers=["dwh-dev-kafka-msk.delhivery.com:9092"], 
    #     api_version=(0,10,1),
    #     value_serializer=lambda x: json.dumps(x).encode('utf-8')
    #     )
    # for prod - KAFKA_URL
    producer = KafkaProducer(bootstrap_servers=['prod-dwh-kafka-1.delhivery.com:9092','prod-dwh-kafka-2.delhivery.com:9092','prod-dwh-kafka-3.delhivery.com:9092'], 
        api_version=(0,10,1),
        value_serializer=lambda x: json.dumps(x).encode('utf-8')
        )
    return producer


#fetch kafka topic
def get_dwh_kafka_topic():
    """
    Uncomment the prod/dev based on the requirements.
    """
    # #for dev - NEW_KAFKA_TOPIC
    # return "dynamo-newserviceability.info"
    # For prod - NEW_KAFKA_TOPIC
    return "Dynamo-Newserviceability.info"


#get pincodes from csv file
def get_data_from_csv(path):
    pincodes = []
    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            pincode = row.get('pincode')
            pincodes.append(pincode)

    return pincodes


#push the pincode data to kafka
def push_pin_data_to_dwh(data, producer):
    success = False
    try: 
      dwh_data = data
      dwh_data["action_date"] = str(int(time.time()*1000*1000))
      producer.send(topic = get_dwh_kafka_topic(),  value = dwh_data)
      success = True
      return success
    except Exception as err :
      print("something_went_wrong!!!")
      print("################## Error in pushing data to Kafka ############################!")
      print("Error - ", err)
      traceback.print_exc()
      return success


#process pincodes and push to kafka
def process_data(pincodes):
    db = SrvRedisClient().get_client()
    failed_data = []
    producer = get_kafka_client()
    counter = 0
    total_count = 0
    try: 
      for pin in pincodes :
          key = 'srv_{}'.format(pin)
          data = db.get(key) or '{}'
          data = json.loads(data)
          default_list = data.get('def', [])
          if default_list :
              for default_item in default_list :
                  sample_data_copy = data.copy()
                  sample_data_copy['def'] = default_item
                  ctrs = default_item.get('ctrs', None)
                  #if ctrs key is present on the def data, unpack the data
                  if ctrs :
                      for key, val in ctrs.items():
                          default_item[key] = val
                      del default_item['ctrs']
                  data = pre_process_dwh_data(sample_data_copy)
                  success = push_pin_data_to_dwh(data, producer)
                  counter += 1
                  #set counter and sleep after 100 messages
                  if counter == 250 :
                      total_count += counter
                      print('Messages Processed >>> ',total_count)             
                      counter = 0
                      time.sleep(3)

                  if not success :
                      failed_data.append(pin)
          else:
              failed_data.append(pin)
      print("List Processed Successfully!!!")
      #do not remove this timeout, as kafka would be closed forcefully, and messages 
      # might not show up if it is a older version of kafka
      time.sleep(5)
      return failed_data
    except Exception as err :
        print("something_went_wrong!!!")
        print("################## Exception while Processing the Data ############################!")
        print("Error - ", err)
        traceback.print_exc()
        return failed_data


def main():
    # File header should be 'pincode'
    # file_path = 'pincodes.csv'
    # pincodes = get_data_from_csv(file_path)
    pincodes = [122001, 999999, 400059 ]
    failed_data = process_data(pincodes)
    print('############################### Failed Data $$$$$$$$$$$$$$$$$$$$$$$$$\n',failed_data)


if __name__ == '__main__':
    main()