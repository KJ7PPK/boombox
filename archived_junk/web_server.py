import usocket as socket
import ujson as json
import machine
import time
import os

cue_file = "cue_data.json"
armed_file = "armed_state.json"

def load_cues():
    try:
        with open(cue_file) as f:
            return json.load(f)
    except:
        return [{"cue": i+1, "gpio": i+1, "desc": "", "runtime": 0.5, "fired": False} for i in range(20)]

def save_cues(cues):
    with open(cue_file, "w") as f:
        json.dump(cues, f)

def load_armed():
    try:
        with open(armed_file) as f:
            return json.load(f).get("armed", False)
    except:
        return False

def save_armed(state):
    with open(armed_file, "w") as f:
        json.dump({"armed": state}, f)

def start_server():
    cues = load_cues()
    armed = load_armed()

    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(5)
    print('[Boombox] Listening on', addr)

    while True:
        cl, addr = s.accept()
        try:
            request = cl.recv(1024).decode()
            print("[Boombox] Request:", request)

            if "/?arm=toggle" in request:
                armed = not armed
                save_armed(armed)

            elif "/?fire=" in request:
                try:
                    if armed:
                        num = int(request.split("fire=")[1].split()[0])
                        cues = load_cues()
                        for cue in cues:
                            if cue["cue"] == num and not cue.get("fired", False):
                                pin = machine.Pin(cue["gpio"], machine.Pin.OUT)
                                pin.value(1)
                                time.sleep(0.5)
                                pin.value(0)
                                cue["fired"] = True
                                save_cues(cues)
                                break
                except:
                    pass

            elif "/?reset=all" in request:
                for cue in cues:
                    cue["fired"] = False
                save_cues(cues)

            elif "/save_descs?data=" in request:
                try:
                    param = request.split("data=")[1].split(" HTTP")[0]
                    decoded = json.loads(param)
                    for i, desc in enumerate(decoded):
                        if i < len(cues):
                            cues[i]["desc"] = desc
                    save_cues(cues)
                except:
                    pass

            response = 'HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n<html><body><h1>OK</h1></body></html>'
            cl.send(response)
        except Exception as e:
            print("[Boombox] Error:", e)
        finally:
            cl.close()
