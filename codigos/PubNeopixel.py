from umqtt.robust import MQTTClient
import time
import network
from neopixel import NeoPixel
import machine as m

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("SSID", "PASS")
time.sleep(5)

ubidotsToken = "TOKEN"
clientID = "CLIENTID"
topic=b"/v1.6/devices/{devicelabel}" #el topic define a que device en especifico es que se va a subir datos
                                 #b"/v1.6/devices/{NOMBRE_DISPOSITIVO}" en el que NOMBRE_DISPOSITIVO es quien
                                 #define entre los devices creados al cual se quiere subir el dato

client = MQTTClient(clientID, "industrial.api.ubidots.com", 1883, user = ubidotsToken, password = ubidotsToken) #creacion de objeto
client.connect() #conexion a ubidots

while True:
	time.sleep(2)
	msg='20|30|200'
	R, G, B = msg.split('|')
	msg = b'{"R":%s, "G":%s, "B":%s}' % (int(R), int(G), int(B))
	print(msg)
	client.publish(topic, msg)