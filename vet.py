import paho.mqtt.client as mqtt
import config

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # Returned payload is a Byte string, need to decode to string
    payload = str(msg.payload.decode("utf-8"))
    print(msg.topic+" "+payload)
    if (payload == "DUCK"):
        print(">>> QUACK!")
    elif (payload == "HAPPY"):
        print(">>> Yeaaaaaaah nice")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(config.mqttUsername, config.mqttPassword)

client.connect("connect.nustem.uk", 1883, 60)

client.loop_forever()
