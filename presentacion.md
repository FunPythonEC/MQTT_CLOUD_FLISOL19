<!--
$theme: gaia
template: invert
-->

![bg](recursos/iot.png)
# Uso de IoT servers con MicroPython
##### Ponentes:
* Jhon Merchan 
* Steven Silva


---

![bg original 100%](recursos/fpylogo.png)

---

![bg](recursos/bckimage.png)
## Infraestructura común de IoT

---

![very good|512x39 100%](recursos/iotdiagram.png)
Ejemplo de Internet of Things Architecture de Cloudcraft
[Cloudcraft](https://cloudcraft.co/app)

---

![bg](recursos/bckimage.png)

### MicroPython

* Python3 compacta
* Rapido de aprender
* Sencillo
* Multiplataforma
* Libre
![bg original 150%](recursos/tenor.gif)

---

![bg](recursos/bckimage.png)
![ original 270%](recursos/firmware-esp.jpg)

---

![bg](recursos/bckimage.png)

### Microcontroladores ESP

* Chip de bajo costo.
* Pila TCP/IP para conexión WiFi.
* Soporta una variedad de lenguajes.
* Procesador 32 bits
* Memoria flash y RAM

---

![bg](recursos/bckimage.png)
### Cloud Services

---

![bg](recursos/bckimage.png)
## MQTT y MicroPython

---

![bg](recursos/bckimage.png)
## Demostración

### Código

#### Imports

~~~~ python
import network
from umqtt.robust import MQTTClient
import time
~~~~

---
![bg](recursos/bckimage.png)
#### Conexión WiFi

~~~~ python
sta= network.WLAN(network.STA_IF)
sta.active(True)
sta.connect("SSID", "PASS")
time.sleep(5)
~~~~

---
![bg](recursos/bckimage.png)
#### Configuración Ubidots items
~~~~ python
ubidotsToken = "ubiotstoken"
clientID = "clientid"
topic=b"/v1.6/devices/{devicelabel}"
~~~~

#### Creación de objeto MQTT

~~~~ python
client = MQTTClient(clientID,"mqtt://things.ubidots.com", 
	1883, user = ubidotsToken, 
        password = ubidotsToken) #creacion de objeto
client.connect()
~~~~

---
![bg](recursos/bckimage.png)
#### Publish
~~~~ python
msg = b'{"temp":20}'
print(msg)
client.publish(topic, msg)
~~~~

#### Subscribe
~~~~ python
client.set_callback(cb)                    
client.subscribe(bytes(topic, 'utf-8'))

while True:
    try:
        client.wait_msg()
        
    except Exception as e:
        print(e)
        client.disconnect()
~~~~

---
![bg](recursos/bckimage.png)
##### Links a repos

* https://github.com/FunPythonEC/MQTT_CLOUD_FLISOL19
* https://github.com/FunPythonEC/ubidots_mqtt_upy

---

![bg](recursos/bckimage.png)

# Contacto

* GitHub: https://github.com/FunPythonEC
* Correo: funpython.ec@gmail.com
* Instagram: @funpython
![bg original 150%](recursos/cclicense.png)
---

<!-- $theme: default -->
![bg original 50%](recursos/fpyig.jpeg)





