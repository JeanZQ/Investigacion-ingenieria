from kafka import KafkaProducer
import time
import random
import string
import json

# Configuración de Kafka
KAFKA_TOPIC = 'user_events'
KAFKA_BOOTSTRAP_SERVERS = ['localhost:29092']

# Productor de Kafka
producer = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)

# Cargar datos desde los archivos JSON
with open('name.json', 'r', encoding='utf-8') as file:
    names = json.load(file)['name']
with open('lastName.json', 'r', encoding='utf-8') as file:
    last_names = json.load(file)['lastName']
with open('mail.json', 'r', encoding='utf-8') as file:
    suffixes = json.load(file)['mail']
with open('address.json', 'r', encoding='utf-8') as file:
    address = json.load(file)['address']

while True:
    name = random.choice(names)
    name2 = random.choice(names)
    lastName = random.choice(last_names)
    lastName2 = random.choice(last_names)

    addresses = random.choice(address)

    mailSuffix = random.choice(suffixes)
    mail = f"{name.lower()}.{lastName.lower()}{random.randint(1, 999)}{mailSuffix}"

    data = f"{name} {name2} {lastName} {lastName2}${addresses}${mail}"
    producer.send(KAFKA_TOPIC, data.encode('utf-8'))
    print(f"Enviado a Kafka: {data}")
    time.sleep(1)
