import serial
import paho.mqtt.client as mqtt
import ssl

# Configurações da porta serial
port = "COM5"  # tools > port
baudrate = 9600

mqtt_broker = 'io.adafruit.com'
mqtt_port = 1883
mqtt_username = 'igorferrati'
mqtt_password = '' 
mqtt_topics = ['igorferrati/feeds/data-output', 'igorferrati/feeds/gas', 'igorferrati/feeds/metrics']

def on_connect(client, userdata, flags, rc):
    print("Conectado ao broker MQTT com código de resultado: "+str(rc))

def on_publish(client, userdata, mid):
    print("Mensagem publicada com sucesso")

client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish

# Conecta ao broker MQTT com SSL
client.username_pw_set(mqtt_username, mqtt_password)
# client.tls_set_context(context=ssl.create_default_context())
client.connect(mqtt_broker, mqtt_port, 60)

# Abre a porta serial
serial_port = serial.Serial(port, baudrate)

# Loop principal
while True:
    # Lê uma linha da porta serial
    data = serial_port.readline().decode().strip()
    print("Dados lidos:", data)

    # Publica os dados no tópico MQTT apropriado
    if data.startswith("Sensor Analogico:"):
        gas_value = data.split(":")[-1].strip()
        client.publish(mqtt_topics[0], data)
        client.publish(mqtt_topics[1], gas_value)
        client.publish(mqtt_topics[2], gas_value)
    else:
        print("Formato de dados não reconhecido.")

# Fecha a porta serial
serial_port.close()
