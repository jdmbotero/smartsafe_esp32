import ujson
import network, time

def do_connect():
    with open('localdata.json') as data_file:
        data = ujson.load(data_file)
        wifiSSID = data["wifi"]["SSD"]
        wifiPassword = data["wifi"]["password"]
        print('SSD: {} & pass: ***'.format(wifiSSID))
        
        sta_if = network.WLAN(network.STA_IF)
        if not sta_if.isconnected():
            print('connecting to network...')
            sta_if.active(True)
            sta_if.connect(wifiSSID, wifiPassword)
            while not sta_if.isconnected():
                pass
        print('Network connected, with this config:', sta_if.ifconfig())
    
def currenttime():
    return time.localtime()