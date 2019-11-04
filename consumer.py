from kafka import KafkaConsumer

topic = 'crm'

# consumer = KafkaConsumer(topic, bootstrap_servers=['192.168.33.77:9092'])
consumer = KafkaConsumer(topic, bootstrap_servers=['192.168.33.77:9092'], auto_offset_reset='earliest')

for message in consumer:
    print("topic={} partition={} offset={} key={} value={}".format(message.topic,
                                                                   message.partition,
                                                                   message.offset,
                                                                   message.key,
                                                                   message.value))
