import json
import paho.mqtt.client as mqtt
import time


def on_message(client, userdata, message):
   # print("received message: " ,str(message.payload.decode("utf-8")))
    print("Mensaje recivido")

mqttBroker ="mqtt.eclipseprojects.io"

client = mqtt.Client("Grupo2sub")


def subscribir(dato, valor):
    
    client.connect("localhost") 
    
    client.loop_start()

    client.subscribe(dato)
    client.on_message=on_message

    

    time.sleep(30)
    client.loop_stop()

    
