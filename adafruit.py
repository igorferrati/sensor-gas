import serial
import paho.mqtt.client as mqtt
import time

port = "COM5"  # tools > port
baudrate = 9600

mqtt_broker = 'io.adafruit.com'
mqtt_port = 1883
mqtt_username = 'igorferrati'
mqtt_password = 'PASSWORD' 
mqtt_topics = ['igorferrati/feeds/data-output', 'igorferrati/feeds/gas', 'igorferrati/feeds/metrics']

client = mqtt.Client()

client.username_pw_set(mqtt_username, mqtt_password)
client.connect(mqtt_broker, mqtt_port, 60)

# Abre a porta serial
serial_port = serial.Serial(port, baudrate)

while True:
    # Lê uma linha da porta serial
    line1 = serial_port.readline().decode().strip()
    line2 = serial_port.readline().decode().strip()
    data = line1 + "\n" + line2
    print("Dados lidos:", data)

    # Publica os dados no tópico MQTT apropriado
    if line1.startswith("Sensor Analogico:"):
        gas_value = line1.split(":")[-1].strip()
        # client.publish(mqtt_topics[0], data)
        client.publish(mqtt_topics[1], gas_value)
        # client.publish(mqtt_topics[2], gas_value)
        
        #limit 30 publish por min
        time.sleep(2)

# Fecha a porta serial
serial_port.close()
