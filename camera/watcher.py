from vidstream import *
import threading

HOST = "192.168.100.37"

server = StreamingServer(HOST, 9999)
t = threading.Thread(target=server.start_server)
t.start()

while input("") != "quit":
    continue

server.stop_server()