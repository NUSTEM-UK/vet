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
        on_duck()
    elif (payload == "HAPPY"):
        on_happy()
    elif (payload == "SAD"):
        on_sad()
    elif (payload == "SKULL"):
        on_skull()
    elif (payload == "HEART"):
        on_heart()

# Callback when HAPPY is received
def on_happy():
    print(">>> Yeaaaaaaah nice")

# Callback when DUCK is received
def on_duck():
    print(">>> QUACK!")

# Callback when SAD is received
def on_sad():
    print(">>> BOOHOO!")

# Callback when SKULL is received
def on_skull():
    print(">>> DOOOM!")

# Callback when HEART is received
def on_heart():
    print(">>> Loooooove!")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(config.mqttUsername, config.mqttPassword)

client.connect("connect.nustem.uk", 1883, 60)

while True:
    # MQTT loop
    client.loop()
