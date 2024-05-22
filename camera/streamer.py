from vidstream import *
import threading
import socket

HOST = "192.168.100.37"

screen_client = CameraClient(HOST, 9999)

screen_client_thread = threading.Thread(target=screen_client.start_stream)
screen_client_thread.start()

while input("") != "quit":
    continue

screen_client.stop_stream()