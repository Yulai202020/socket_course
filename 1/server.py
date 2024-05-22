import socket, threading

HOST = (socket.gethostname(), 9022)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(HOST)
s.listen()

clients = []
nicknames = []

def boardcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)

            if message.decode('ascii').startswith("KICK"):
                name_to_kick = message.decode('ascii')[5:]
                kick_user(name_to_kick)
                break

            elif message.decode('ascii').startswith("BAN"):
                name_to_kick = message.decode('ascii')[4:]
                kick_user(name_to_kick)
                with open("ban.txt", "a") as f:
                    f.write(name_to_kick+'\n')
                break

            boardcast(message)

        except:
            try:
                index = clients.index(client)
                nickname = nicknames[index]

                clients.remove(index)
                nickname.remove(nickname)

                boardcast(f"{nickname} has been leaved.".encode('ascii'))
                client.close()
            except:
                break
            finally:
                break

def accept():
    while True:
        client, addr = s.accept()
        print("Connected to ", addr)

        client.send(b"NICK")
        nickname = client.recv(1024).decode()

        with open('ban.txt') as f:
            baned = f.readlines()
        
        if nickname+'\n' in baned:
            client.send("BAN".encode('ascii'))
            client.close()
            continue

        nicknames.append(nickname)
        clients.append(client)

        if nickname == "admin":
            client.send("PASS".encode("ascii"))
            password = client.recv(1024).decode("ascii")
            if password != "abc":
                client.send("REFUSE".encode("ascii"))
                client.close()
                continue

        boardcast(f"{nickname} has been joined.".encode("ascii"))

        user_thread = threading.Thread(target=handle, args=(client,))
        user_thread.start()

def kick_user(name):
    if name in nicknames:
        name_index = nicknames.index(name)
        client_to_kick = clients[name_index]

        clients.remove(client_to_kick)
        nicknames.remove(name)

        client_to_kick.send("You was kicked by an admin!".encode('ascii'))
        client_to_kick.close()

if __name__ == "__main__":
    print("Server is listening")
    accept()