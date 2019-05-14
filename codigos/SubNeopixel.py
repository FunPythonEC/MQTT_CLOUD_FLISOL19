
from umqtt.robust import MQTTClient #permite la comunicación mqtt con el server
import time
import network #manejo para conexiones inalambricas WIFI
from neopixel import NeoPixel
import machine as m

lednum=20 #Numero de leds usados
nppin=22

nppin=m.Pin(nppin) #inicializacion de pin salida para leds
np=NeoPixel(nppin, lednum)

#funcion de callback para el subscribe mqtt
def cb(topic,msg):
	np[:]=(msg)
	np.write()

#conexión wifi y configuracion
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("SSID", "PASS")
time.sleep(5)

#para la conexión a ubidots es necesario un token
ubidotsToken = "TOKEN"
clientID = "CLIENTID"
topic=b"/v1.6/devices/{devicelabel}" #el topic define a que device en especifico es que se va a subir datos
                                 #b"/v1.6/devices/{NOMBRE_DISPOSITIVO}" en el que NOMBRE_DISPOSITIVO es quien
                                 #define entre los devices creados al cual se quiere subir el dato

#configuracion del mqtt cliente, se apunta al endpoint 'industrial.api.ubidots.com'
client = MQTTClient(clientID, "industrial.api.ubidots.com", 1883, user = ubidotsToken, password = ubidotsToken) #creacion de objeto
client.connect() #conexion a ubidots

#metodo de callback seteado
client.set_callback(cb)
#metodo para comenzar a escuchar a escuchar el topic                   
client.subscribe(bytes(topic, 'utf-8'))

while True:
	try:
        #se espera el mensaje
        client.wait_msg()        
    except Exception as e:
        print(e)
        client.disconnect()
		sys.exit()
