from vidstream import *
from multiprocessing import Process
import threading
import socket

HOST = "192.168.100.37"

screen_client = ScreenShareClient(HOST, 9997)
server = StreamingServer(HOST, 8887)

t = Process(target=server.start_server)
t.start()


screen_client_thread = Process(target=screen_client.start_stream)
screen_client_thread.start()

i = input("")

screen_client.stop_stream()
server.stop_server()