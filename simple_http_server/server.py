import socket
import select

if __name__ == "__main__":
    listener_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    address_port = ("127.0.0.1", 8080)
    listener_socket.bind(address_port)
    listener_socket.listen(1)
    print("Server listening @ 127.0.0.1:8080")

    while True:
        client_socket, client_address = listener_socket.accept()

        client_msg = client_socket.recv(4096)
        print(f"Client said: {client_msg.decode('utf-8')}")

        with open("index.html") as f:
            answer = "HTTP/1.1 200 OK\nContent-Type: text/html\n<h1>hi</h1>"
            client_socket.sendall(answer.encode())
        try:
            client_socket.close()
        except OSError:
            pass