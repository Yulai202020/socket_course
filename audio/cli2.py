from vidstream import AudioReceiver
from vidstream import AudioSender
import threading, socket

HOST = socket.gethostname()
HOST = "192.168.100.37"

sender = AudioSender(HOST, 9999)
sender_thread = threading.Thread(target=sender.start_stream)

receiver = AudioReceiver(HOST, 8888)
receiver_thread = threading.Thread(target=receiver.start_server)

sender_thread.start()
receiver_thread.start()

while input("") != 'quit':
    continue

sender.stop_stream()
receiver.stop_server()