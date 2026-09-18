import network

def setup_wifi():
    ap = network.WLAN(network.AP_IF)
    ap.config(essid='Boombox', password='BangBang')
    ap.active(True)
    while not ap.active():
        pass
    print("AP setup complete:", ap.ifconfig())