from vidstream import *
from multiprocessing import Process
import threading
import socket

HOST = "192.168.100.37"

screen_client = ScreenShareClient(HOST, 8887)
server = StreamingServer(HOST, 9997)

t = Process(target=server.start_server)
t.start()

screen_client_thread = None

i = input("")

while i != "reset":
    if i == "start stream":
        screen_client.stop_stream()

        try:
            screen_client_thread.terminate()
        except:
            pass

        screen_client_thread = Process(target=screen_client.start_stream)
        screen_client_thread.start()

    elif i == "stop stream":
        screen_client.stop_stream()
        screen_client_thread.terminate()

    elif i == "stop watch":
        server.stop_server()
        t.terminate()

    elif i == "start watch":
        t = Process(target=server.start_server)
        t.start()

    i = input("")
    continue

screen_client.stop_stream()
server.stop_server()