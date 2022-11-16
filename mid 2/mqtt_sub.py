import time
import paho.mqtt.client as paho
import json

broker="10.20.1.95"

def on_message(client, userdata, message):
    time.sleep(1)
    y = json.loads(message.payload)
    print("received message =")
    print("y['StudentID']=", y["StudentID"])
    print("y['Name']=", y["Name"])
    print("y['Surname']=", y["Surname"])
    print("y['Telephone']=", y["Telephone"])
    print("y['Grade']=", y["Grade"])


client= paho.Client() #create client object 

client.on_message=on_message
#####
print("connecting to broker ",broker)
client.connect(broker)#connect
client.loop_start() #start loop to process received messages
print("subscribing ")
client.subscribe("se443/midterm2")#subscribe
while(True):
	client.on_message=on_message