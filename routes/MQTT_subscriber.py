import json
import paho.mqtt.client as mqtt
import time
from config.database import conn
from sqlalchemy.sql import text, table, column
from config.database import insert_datos


# MQTT Settings 
MQTT_Broker = "mqtt.eclipseprojects.io"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic = "Grupo2"

#Subscribe to all Sensors at Base Topic
def on_connect(mosq, obj, rc):
	mqttc.subscribe(MQTT_Topic, 0)

#Save Data into DB Table
def on_message(mosq, obj, msg):
	# This is the Master Call for saving MQTT Data into DB
	# For details of "sensor_Data_Handler" function please refer "sensor_data_to_db.py"
	print ("MQTT Data Received...")
	print ("MQTT Topic: " + msg.topic)  
	print ("Data: " + msg.payload)
	insert_datos(msg.payload)

def on_subscribe(mosq, obj, mid, granted_qos):
    pass

mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Connect
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))

# Continue the network loop
mqttc.loop_forever()


# def on_message(client, userdata, message):
#    # print("received message: " ,str(message.payload.decode("utf-8")))
#     print("Mensaje recivido")

# mqttBroker ="mqtt.eclipseprojects.io"

# client = mqtt.Client("Grupo2sub")


# def subscribir(dato, valor):
    
#     client.connect("localhost") 
    
#     client.loop_start()

#     client.subscribe(dato)
#     client.on_message=on_message

#     valor_json = json.loads(valor)

#     conn.execute(table('datos', column('humedad'), column('temperatura'), column('fecha'), column('longitud'), column('latitud')).insert().values({ "humedad": valor_json.humedad, "temperatura": valor_json.temperatura, "fecha": valor_json.fecha, "longitud": valor_json.longitud, "latitud": valor_json.latitud}))
    

#     time.sleep(30)
#     client.loop_stop()

    
