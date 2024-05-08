import serial
import paho.mqtt.client as mqtt
import time

# Configurações da porta serial
port = 'COM5'  # tools > port
baudrate = 9600

#broker MQTT - Mosquitto
mqtt_broker = 'localhost'
mqtt_port = 1883
mqtt_topic = 'qualidade do ar'


def on_publish(client, userdata, mid):
    print("Mensagem publicada com sucesso")

client = mqtt.Client()
client.connect(mqtt_broker, mqtt_port)

# Abre a porta serial
serial_port = serial.Serial(port, baudrate)

# Loop principal
while True:
    # Lê uma linha da porta serial
    data = serial_port.readline().decode().strip()
    print("Dados lidos:", data)

    # Publica os dados no tópico MQTT
    client.publish(mqtt_topic, data)
    time.sleep(3)
# Fecha a porta serial
serial_port.close()
