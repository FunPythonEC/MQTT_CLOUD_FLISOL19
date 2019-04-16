import gc
gc.collect()
gc.mem_free()

from microWebSrv import MicroWebSrv
from machine import Pin
from neopixel import NeoPixel
import json
import network
import time
#conexion wifi
sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
sta_if.connect("NETLIFE-Silva", "SASM3141")
time.sleep(5)

np = NeoPixel(Pin(13), 1)

def _httpHandlerLEDPost(httpClient, httpResponse):
    content = httpClient.ReadRequestContent()  # Read JSON color data
    colors = json.loads(content)
    blue, green, red = [colors[k] for k in sorted(colors.keys())]
    print("R:"+str(red))
    print("G:"+str(green))
    print("B:"+str(blue))
    np[0] = (green, red, blue)
    np.write()
    httpResponse.WriteResponseJSONOk()

routeHandlers = [ ( "/led", "POST",  _httpHandlerLEDPost ) ]
srv = MicroWebSrv(routeHandlers=routeHandlers, webPath='/www/')
srv.Start(threaded=False)
