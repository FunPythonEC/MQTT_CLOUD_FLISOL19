from microWebSrv import MicroWebSrv
from machine import Pin
from neopixel import NeoPixel
import json

np = NeoPixel(Pin(13), 1)

def _httpHandlerLEDPost(httpClient, httpResponse):
    content = httpClient.ReadRequestContent()  # Read JSON color data
    colors = json.loads(content)
    blue, green, red = [colors[k] for k in sorted(colors.keys())]
    np[0] = (green, red, blue)
    np.write()
    httpResponse.WriteResponseJSONOk()

routeHandlers = [ ( "/led", "POST",  _httpHandlerLEDPost ) ]
srv = MicroWebSrv(routeHandlers=routeHandlers, webPath='/www/')
srv.Start(threaded=False)