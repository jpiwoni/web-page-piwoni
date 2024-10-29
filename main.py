import socket
import json

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    host = '127.0.0.1'
    port = 8080

    server_socket.bind((host, port))

    server_socket.listen(5)
    print(f"Server listening on port {port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Got a connection from {addr}")

        data = client_socket.recv(1024).decode('utf-8')

        json_data = json.loads(data)

        print(json_data["firstName"])
        client_socket.close()


if __name__ == "__main__":
    start_server()