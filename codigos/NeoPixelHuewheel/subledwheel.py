from umqtt.robust import MQTTClient
import time
import network
from neopixel import NeoPixel
import machine as m

lednum=30
nppin=12

nppin=m.Pin(nppin)
global np
np=NeoPixel(nppin, lednum)

def cb(topic,msg):
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
        for i in range(0,lednum):
            np[i]=(r,g,b)
        np.write()
        time.sleep_ms(500)
    except Exception as e:
        print(e)
        

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("Asian Coffee Roaster.net", "espresso")
time.sleep(5)

ubidotsToken = "BBFF-s9KVriflqKas0akiIM4FhI4FoLLbV3"
clientID = "espcontrol"
topic=b"/v1.6/devices/espprueba/r/lv" #el topic define a que device en especifico es que se va a subir datos
                                 #b"/v1.6/devices/{NOMBRE_DISPOSITIVO}" en el que NOMBRE_DISPOSITIVO es quien
                                 #define entre los devices creados al cual se quiere subir el dato

client = MQTTClient(clientID, "industrial.api.ubidots.com", 1883, user = ubidotsToken, password = ubidotsToken) #creacion de objeto
client.connect() #conexion a ubidots

client.set_callback(cb)                    
client.subscribe(topic)
client.subscribe(b"/v1.6/devices/espprueba/g/lv")
client.subscribe(b"/v1.6/devices/espprueba/b/lv")

while True:
    try:
        client.wait_msg()      
    except Exception as e:
        print(e)
        client.disconnect()
        sys.exit()