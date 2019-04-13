
#para mas informacion sobre ubidots y mqtt:
#https://help.ubidots.com/developer-guides/ubidots-mqtt-broker

import network
from robust import MQTTClient #no esta incluida en el firmware para el esp32, deben ser agregados los scripts de mqtt
import time

#conexion wifi
sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
sta_if.connect("SSID", "PASS")
time.sleep(5)

#se debe especificar el token de acuerdo a la cuenta de ubidots y el clientid con el que se subscribira el esp
ubidotsToken = "ubiotstoken"
clientID = "clientid"
topic=b"/v1.6/devices/esp32lora" #el topic define a que device en especifico es que se va a subir datos
								 #b"/v1.6/devices/{NOMBRE_DISPOSITIVO}" en el que NOMBRE_DISPOSITIVO es quien
								 #define entre los devices creados al cual se quiere subir el dato

client = MQTTClient(clientID, "mqtt://things.ubidots.com", 1883, user = ubidotsToken, password = ubidotsToken) #creacion de objeto
client.connect() #conexion a ubidots

#ejemplo de uso del metodo de publicacion
temp, humid = msg.split('|')
msg = b'{"temp":%s, "humid":%s}' % (temp, humid)
print(msg)
client.publish(topic, msg)