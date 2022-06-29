import paho.mqtt.client as mqtt

#mqttBroker ="46.183.113.253" 
mqttBroker ="mqtt.eclipseprojects.io"

client = mqtt.Client("Temperature_Inside")
client.connect(mqttBroker) 

randNumber = random.uniform(20.0, 21.0)
client.publish("TEMPERATURE", randNumber)
print("Just published " + str(randNumber) + " to topic TEMPERATURE")