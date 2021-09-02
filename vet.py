import paho.mqtt.client as mqtt
from guizero import App, Text, PushButton, TextBox, Box
import config

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    mqttMessageBox.clear()
    output("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # Returned payload is a Byte string, need to decode to string
    payload = str(msg.payload.decode("utf-8"))
    print(msg.topic+" "+payload)
    output(msg.topic+" "+payload)
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

# Append messaegText to mqttMessageBox
def output(messageText):
    mqttMessageBox.append(messageText)
    mqttMessageBox.tk.see('end')

# Callback when HAPPY is received
def on_happy():
    # messageText = '>>> Yeaaaaaaah nice'
    # output(messageText)
    # print(messageText)
    pass

# Callback when DUCK is received
def on_duck():
    # messageText = '>>> QUACK!'
    # output(messageText)
    # print(messageText)
    pass

# Callback when SAD is received
def on_sad():
    # messageText = '>>> BOOHOO!'
    # output(messageText)
    # print(messageText)
    pass

# Callback when SKULL is received
def on_skull():
    # messageText = '>>> DOOOM!'
    # output(messageText)
    # print(messageText)
    pass

# Callback when HEART is received
def on_heart():
    # messageText = '>>> Loooooove!'
    # output(messageText)
    # print(messageText)
    pass

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(config.mqttUsername, config.mqttPassword)

def do_connect():
    try:
        client.connect("connect.nustem.uk", 1883, 60)
        print("Connection successful")
    except:
        print("Failed to connect to MQTT server")
        exit(1)

def send_message(messageText):
    client.publish("Connect/NUSTEM/MOOD", messageText)

def send_happy():
    send_message("HAPPY")

def send_sad():
    send_message("SAD")

def send_skull():
    send_message("SKULL")

def send_heart():
    send_message("HEART")

def send_duck():
    send_message("DUCK")

def mqtt_loop():
    # MQTT loop
    # Paho Python docs here: https://github.com/eclipse/paho.mqtt.python#network-loop
    client.loop()

app = App(title="Connect Vet")
# message = Text(app, text = "Connect Vet")

buttonBox = Box(app)
button = PushButton(buttonBox, align='left', width=5, command=send_happy, text="HAPPY")
button = PushButton(buttonBox, align='left', width=5, command=send_sad, text="SAD")
button = PushButton(buttonBox, align='left', width=5, command=send_skull, text="SKULL")
button = PushButton(buttonBox, align='left', width=5, command=send_heart, text="HEART")
button = PushButton(buttonBox, align='left', width=5, command=send_duck, text="DUCK")

mqttMessageBox = TextBox(app, width = 'fill', height = 'fill', multiline=True, scrollbar=True, text = "Starting up...")

button = PushButton(app, command=do_connect, text="Clear/Reconnect")

# Can use GUIZero's repeat timeer, but performance sucks...
# app.repeat(250, mqtt_loop)

# ...much better to use the built-in Paho threaded loop, which keeps the gui buttons responsive.
do_connect()
client.loop_start()

# Everything set up, so run the GUIzero loop
app.display()
