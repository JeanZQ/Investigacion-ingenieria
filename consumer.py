import time
from kafka import KafkaConsumer
import mysql.connector

# Configuración de Kafka
KAFKA_TOPIC = 'user_events'
KAFKA_BOOTSTRAP_SERVERS = ['localhost:29092']

# Configuración de MySQL
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'root'
MYSQL_DATABASE = 'bank'

# Crear la tabla User si no existe
mydb = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DATABASE
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS User (IdUser INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255), addresses VARCHAR(255), FlooNetworkID VARCHAR(50), mail VARCHAR(100), timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)")

# Consumidor de Kafka
consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS, auto_offset_reset='earliest')

while True:
    try:
        for message in consumer:
            data = message.value.decode('utf-8').split(',')
            name, addresses, flooNetworkID, mail = data
            sql = "INSERT INTO User (name, addresses, FlooNetworkID, mail) VALUES (%s, %s, %s, %s)"
            val = (name, addresses, flooNetworkID, mail)
            mycursor.execute(sql, val)
            mydb.commit()
            print(f"Guardado en la base de datos: {name}, {addresses}, {flooNetworkID}, {mail}")
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)
        continue
