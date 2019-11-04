from kafka import KafkaProducer

topic = 'crm'

producer = KafkaProducer(bootstrap_servers=['192.168.33.77:9092'])

while True:
    value = input('value:')
    producer.send(topic, bytes(value, encoding='utf8'))
