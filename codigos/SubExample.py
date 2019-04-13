import network
from umqtt.robust import MQTTClient #no esta incluida en el firmware para el esp32, deben ser agregados los scripts de mqtt
import time

#conexion wifi
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
    time.sleep(3)
    client.publish(topic, b'{"temp":20}')