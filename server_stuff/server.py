import socket

PORT = 9999
HOST = "0.0.0.0"

CREDENTIALS = [
    {"username": "kaleb", "password": "1234", "id": "1"},
    {"username": "admin", "password": "4321", "id": "2"},
    {"username": "guest", "password": "0000", "id": "3"},
]

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"Server listening on port {PORT}...")

while True:
    client_socket, client_address = server_socket.accept()
    print("------------------------------------------------------------")
    print(f"Connected to {client_address}")

    try:

        while True:
            data = client_socket.recv(1024)
            if not data:
                raise ConnectionResetError
            user_user = data.decode()

            match = next((u for u in CREDENTIALS if u["username"] == user_user), None)

            if match:
                client_socket.send(b'1')
                print(f"Client username: {user_user}, ID: {match['id']}")
                break
            else:
                client_socket.send(b'2')

        while True:
            data = client_socket.recv(1024)
            if not data:
                raise ConnectionResetError
            user_pass = data.decode()

            if match and match["password"] == user_pass:
                client_socket.send(b'1')
                print(f"Client password: {user_pass}, ID: {match['id']}")
                break
            else:
                client_socket.send(b'2')

        print(f"{client_address} logged in successfully.\n"
              f"Username > {user_user}\nPassword > {user_pass}\nUser ID > {match['id']}")

        while True:
            data = client_socket.recv(1024)
            if not data:
                raise ConnectionResetError
            print(f"Received from {user_user}: {data.decode()}")

    except (BrokenPipeError, ConnectionResetError):
        print(f"Client {client_address} disconnected")
    finally:
        client_socket.close()
