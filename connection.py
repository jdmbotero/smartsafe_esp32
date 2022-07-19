import ujson
import network, time

def do_connect():
    with open('localdata.json') as data_file:
        data = ujson.load(data_file)
        wifiSSID = data["wifi"]["SSD"]
        wifiPassword = data["wifi"]["password"]
        print('SSD: {} & pass: ***'.format(wifiSSID))
        
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        if not wlan.isconnected():
            wlan.connect(wifiSSID, wifiPassword)
            print("Waiting for Wi-Fi connection", end="...")
            while not wlan.isconnected():
                print(".", end="")
                time.sleep(1)
            print()
    
def currenttime():
    return time.localtime()

def gm_time():
    gm = time.gmtime()
    return str("{}-{}-{}T{}:{}:{}Z".format(gm[0], gm[1], gm[2], gm[3], gm[4], gm[5]))