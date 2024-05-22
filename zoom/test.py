from vidstream import *
import threading
server = StreamingServer("192.168.100.37", 7777)
t = threading.Thread(target=server.start_server)
t.start()

while True:
    input()
    continue