import socket, threading

nickname = input("Choose username: ")
if nickname == "admin":
    password = input("Type password for admin: ")

HOST = (socket.gethostname(), 9022)


handle_thread = ""; write_thread = ""

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(HOST)
stop_thread = False

def handle():
    global stop_thread
    while True:
        if stop_thread:
            break
        try:
            message = client.recv(1024).decode('ascii')

            if message == "NICK":
                client.send(nickname.encode('ascii'))
                next_message = client.recv(1024).decode('ascii')
                if next_message == "PASS":
                    client.send(password.encode('ascii'))
                    if client.recv(1024).decode('ascii') == "REFUSE":
                        print("Password is not correct.")
                        print("Exiting.")
                        stop_thread = True
                elif next_message == "BAN":
                    print("You has been baned on this server!")
                    client.close()
                    stop_thread = True
            else:
                print(message)

        except:
            print("Exiting")
            client.close()
            stop_thread = True

def write():
    global stop_thread
    while True:
        if stop_thread:
            break
        message = f"{nickname}: {input()}"
        if stop_thread:
            break
        if message[len(nickname)+2:].startswith('/'):
            if nickname == "admin":
                if message[len(nickname)+2:].startswith("/kick"):
                    client.send(f"KICK {message[len(nickname)+2+6:]}".encode('ascii'))
                elif message[len(nickname)+2:].startswith("/ban"):
                    client.send(f"BAN {message[len(nickname)+2+5:]}".encode('ascii'))
            else:
                print("Command can be executed just by admin!")

        client.send(message.encode('ascii'))

handle_thread = threading.Thread(target=handle)
write_thread = threading.Thread(target=write)

handle_thread.start()
write_thread.start()
