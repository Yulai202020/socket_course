from vidstream import *
import threading, time
import tkinter as tk
import socket

local_ip_address = socket.gethostbyname(socket.gethostname())
local_ip_address = "192.168.100.37"

server = StreamingServer(local_ip_address, 5555)
receiver = AudioReceiver(local_ip_address, 6666)

def start_listen():
    t1 = threading.Thread(target=server.start_server)
    t2 = threading.Thread(target=receiver.start_server)

    t1.start()
    t2.start()

def start_camera_stream():
    camera_client = CameraClient(text_target_ip.get(1.0, "end-1c"), 7777)
    t3 = threading.Thread(target=camera_client.start_stream)
    t3.start()

def start_screen_sharing():
    screen_client = ScreenShareClient(text_target_ip.get(1.0, "end-1c"), 7777)
    t4 = threading.Thread(target=screen_client.start_stream)
    t4.start()

def start_audio_sharing():
    audio_client = AudioSender(text_target_ip.get(1.0, "end-1c"), 4444)
    t5 = threading.Thread(target=audio_client.start_stream)
    t5.start()

# Gui
window = tk.Tk()
window.title("ZOOM")
window.geometry("300x200")

label_target_ip = tk.Label(window, text="target IP:")
label_target_ip.pack()

text_target_ip = tk.Text(window, height=1)
text_target_ip.pack()

btn_listen = tk.Button(window, text="Start listening", width=50, command=start_listen)
btn_listen.pack(anchor=tk.CENTER, expand=True)

btn_camera = tk.Button(window, text="Start Camera Stream", width=50, command=start_camera_stream)
btn_camera.pack(anchor=tk.CENTER, expand=True)

btn_screen = tk.Button(window, text="Start Screen Sharing", width=50, command=start_screen_sharing)
btn_screen.pack(anchor=tk.CENTER, expand=True)

btn_audio = tk.Button(window, text="Start Audio Sharing", width=50, command=start_audio_sharing)
btn_audio.pack(anchor=tk.CENTER, expand=True)

window.mainloop()