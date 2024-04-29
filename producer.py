from kafka import KafkaProducer
import time
import random
import string

# Configuración de Kafka
KAFKA_TOPIC = 'user_events'
KAFKA_BOOTSTRAP_SERVERS = ['localhost:29092']

# Productor de Kafka
producer = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)

while True:
    name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    addresses = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))
    flooNetworkID = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    mail = f"{name}@example.com"
    data = f"{name},{addresses},{flooNetworkID},{mail}"
    producer.send(KAFKA_TOPIC, data.encode('utf-8'))
    print(f"Enviado a Kafka: {data}")
    time.sleep(5)
