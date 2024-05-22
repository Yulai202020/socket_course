from vidstream import AudioReceiver
from vidstream import AudioSender
import threading, socket

HOST = socket.gethostname()
HOST = "192.168.100.37"

receiver = AudioReceiver(HOST, 9999)
receiver_thread = threading.Thread(target=receiver.start_server)

sender = AudioSender(HOST, 8888)
sender_thread = threading.Thread(target=sender.start_stream)

receiver_thread.start()
sender_thread.start()

while input("") != 'quit':
    continue

receiver.stop_server()
sender.stop_stream()