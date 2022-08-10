import json
import paho.mqtt.client as mqtt
import time
from config.database import conn
from sqlalchemy.sql import text, table, column


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

    valor_json = json.loads(valor)

    conn.execute(table('datos', column('humedad'), column('temperatura'), column('fecha'), column('longitud'), column('latitud')).insert().values({ "humedad": valor_json.humedad, "temperatura": valor_json.temperatura, "fecha": valor_json.fecha, "longitud": valor_json.longitud, "latitud": valor_json.latitud}))
    

    time.sleep(30)
    client.loop_stop()

    
