from machine import Pin

r = Pin(2, Pin.OUT)
g = Pin(0, Pin.OUT)
b = Pin(4, Pin.OUT)

def rgb_on(R, G, B):
    r.value(R)
    g.value(G)
    b.value(B)
    
def rgb_on_red():
    return rgb_on(1, 0, 0)

def rgb_on_green():
    return rgb_on(0, 1, 0)

def rgb_on_blue():
    return rgb_on(0, 0, 1)

def rgb_on_yellow():
    return rgb_on(1, 1, 0)

def rgb_on_turquesa():
    return rgb_on(0, 1, 1)

def rgb_on_white():
    return rgb_on(0, 1, 1)

def rgb_on_fucsia():
    return rgb_on(1, 0, 1)

if __name__==("__main__"):
    while True:
        rgb_on_turquesa()