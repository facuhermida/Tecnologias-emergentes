import paho.mqtt.client as mqtt

mqttBroker ="mqtt.eclipseprojects.io"

def publicar(dato, valor):

    #mqttBroker ="46.183.113.253" 
    

    client = mqtt.Client("Grupo2")
    client.connect(mqttBroker) 

    client.publish("Grupo2", valor)
    print("Cola:"+ dato +" - Valor: "+ valor)