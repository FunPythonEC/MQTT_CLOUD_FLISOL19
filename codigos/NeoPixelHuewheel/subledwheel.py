from umqtt.robust import MQTTClient #libreria para la comunicación MQTT
import time
import network
from neopixel import NeoPixel
import machine as m

#config para neopixel
lednum=29
nppin=12

nppin=m.Pin(nppin) #pin instanciado para neopixel
global np
np=NeoPixel(nppin, lednum) #array de neopixel inicializada

#funcion de callback para captar datos
def cb(topic,msg):
    #variables globales por las funciones
    global r
    global b
    global g

    col=str(topic).split("/")

    if col[-2]=='r':
        print("rojo")
        r=int(msg)
        
    elif col[-2]=='b':
        print("azul")
        b=int(msg)   
    else:
        print("verde")
        g=int(msg)

    try:
        print(r,g,b)
        
        #llenado de variables
        for i in range(0,lednum):
            np[i]=(r,g,b)
        np.write() #envio de colores a la tira led
    except Exception as e:
        print(e)
        
#conexion a red wifi
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("ssid", "pass")
time.sleep(5)

#credenciales para conexion a ubidots
ubidotsToken = "token"
clientID = "espcontrol"
topic=b"/v1.6/devices/espprueba/r/lv" #el topic define a que device en especifico es que se va a subir datos
                                 #b"/v1.6/devices/{NOMBRE_DISPOSITIVO}" en el que NOMBRE_DISPOSITIVO es quien
                                 #define entre los devices creados al cual se quiere subir el dato

#inicializacion de cliente para mqtt y conexion
client = MQTTClient(clientID, "industrial.api.ubidots.com", 1883, user = ubidotsToken, password = ubidotsToken) #creacion de objeto
client.connect() #conexion a ubidots

client.set_callback(cb) #seteo de funcion de callback                  
client.subscribe(topic) #conectarse a topics definidos
client.subscribe(b"/v1.6/devices/espprueba/g/lv")
client.subscribe(b"/v1.6/devices/espprueba/b/lv")

while True:
    try:
        client.wait_msg() #recepcion del dato     
    except Exception as e:
        print(e)
        client.disconnect()
        sys.exit()