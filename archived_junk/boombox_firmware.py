import network
import socket
import time
from machine import Pin

# GPIO configuration
cue_pins = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
            10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
cues = [Pin(pin, Pin.OUT) for pin in cue_pins]

# Setup Wi-Fi Access Point
ssid = 'Boombox'
password = 'BangBang'
ap = network.WLAN(network.AP_IF)
ap.config(essid=ssid, password=password)
ap.active(True)

while not ap.active():
    pass

print('Access Point active')
print('Connect to Wi-Fi SSID:', ssid)
print('IP address:', ap.ifconfig()[0])

# HTML Page Template
html = """HTTP/1.0 200 OK

<!DOCTYPE html>
<html>
<head>
  <title>Fireworks Control</title>
  <style>
    body { font-family: sans-serif; background: #111; color: #eee; text-align: center; }
    button { padding: 20px; margin: 10px; font-size: 20px; background: red; color: white; border: none; }
    .group { margin-bottom: 40px; }
  </style>
</head>
<body>
  <h1>Boombox Control Panel</h1>
  %s
</body>
</html>
"""

# Button Generator
def generate_buttons():
    content = ""
    for group in range(4):
        content += f"<div class='group'><h2>Box {group+1}</h2>"
        for cue in range(5):
            pin_index = group * 5 + cue
            content += f"<form method='GET'><button name='cue' value='{pin_index}'>Cue {pin_index+1}</button></form>"
        content += "</div>"
    return content

# Fire Cue
def fire_cue(index):
    try:
        pin = cues[int(index)]
        pin.high()
        time.sleep(1)
        pin.low()
        return True
    except:
        return False

# Simple Web Server
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print("Listening on", addr)

while True:
    cl, addr = s.accept()
    print('Client connected from', addr)
    req = cl.recv(1024)
    req = str(req)
    cue_index = None
    if '/?cue=' in req:
        cue_index = req.split('/?cue=')[1].split(' ')[0]
        fire_cue(cue_index)
    response = html % generate_buttons()
    cl.send(response)
    cl.close()
