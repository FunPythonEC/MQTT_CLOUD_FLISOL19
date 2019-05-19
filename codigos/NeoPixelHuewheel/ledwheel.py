import gc
gc.collect()
gc.mem_free()

from microWebSrv import MicroWebSrv
from machine import Pin
from neopixel import NeoPixel
import json
import network
import time
from umqtt.robust import MQTTClient
#conexion wifi
sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
sta_if.connect("ssid", "pass")
time.sleep(5)

ubidotsToken = "token"
clientID = "espleds"
topic=b"/v1.6/devices/espprueba" #el topic define a que device en especifico es que se va a subir datos
                                 #b"/v1.6/devices/{NOMBRE_DISPOSITIVO}" en el que NOMBRE_DISPOSITIVO es quien
                                 #define entre los devices creados al cual se quiere subir el dato

client = MQTTClient(clientID, "industrial.api.ubidots.com", 1883, user = ubidotsToken, password = ubidotsToken) #creacion de objeto
client.connect() #conexion a ubidots

def _httpHandlerLEDPost(httpClient, httpResponse):
    content = httpClient.ReadRequestContent()  # Read JSON color data
    colors = json.loads(content)
    blue, green, red = [colors[k] for k in sorted(colors.keys())]
    msg=b'{"r": %s,"g": %s, "b": %s}' % (int(red),int(green),int(blue))
    print(msg)
    client.publish(topic, msg)
    httpResponse.WriteResponseJSONOk()

routeHandlers = [ ( "/led", "POST",  _httpHandlerLEDPost ) ]
srv = MicroWebSrv(routeHandlers=routeHandlers, webPath='/www/')
srv.Start(threaded=False)
