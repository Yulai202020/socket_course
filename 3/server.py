from vidstream import CameraClient
from vidstream import StreamingServer
import threading, time

receiving = StreamingServer('ip', 9999)
sending = CameraClient('ip', 9999)
th = threading.Thread(target=receiving.start_server)
th.start()

time.sleep(2)

th2 = threading.Thread(target=sending.start_server)
th2.start()

while input("") != "STOP":
    continue

receiving.stop_server()
sending.stop_server(a)