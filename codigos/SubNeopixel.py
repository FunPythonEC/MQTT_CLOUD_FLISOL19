from umqtt.robust import MQTTClient
import time
import network
from neopixel import NeoPixel
import machine as m


lednum=20
nppin=22

nppin=m.Pin(nppin)
np=NeoPixel(nppin, lednum)

def cb(topic,msg):
	np[:]=(msg)

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

client.set_callback(cb)                    
client.subscribe(bytes(topic, 'utf-8'))

while True:
	try:
        client.wait_msg()        
    except Exception as e:
        print(e)
        client.disconnect()
		sys.exit()
