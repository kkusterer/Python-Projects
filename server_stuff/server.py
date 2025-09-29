import socket

PORT = 65535
USERNAME = "kaleb"
PASSWORD = "1234"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('0.0.0.0', PORT))
server_socket.listen(1)
print(f"Server listening on port {PORT}...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connected to {client_address}")

    try:
        # Handle username
        while True:
            data = client_socket.recv(1024)
            if not data:  # client closed connection
                raise ConnectionResetError
            user_user = data.decode()
            if user_user == USERNAME:
                client_socket.send(b'1')
                print(f"Client username: {user_user}")
                break
            else:
                client_socket.send(b'2')

        # Handle password
        while True:
            data = client_socket.recv(1024)
            if not data:  # client closed connection
                raise ConnectionResetError
            user_pass = data.decode()
            if user_pass == PASSWORD:
                client_socket.send(b'1')
                print(f"Client password: {user_pass}")
                break
            else:
                client_socket.send(b'2')

        print(f"{client_address} logged in successfully")

        
        while True:
            data = client_socket.recv(1024)
            if not data:  
                raise ConnectionResetError
            
            print(f"Received from client: {data.decode()}")

    except (BrokenPipeError, ConnectionResetError):
        print(f"Client {client_address} disconnected")
    finally:
        client_socket.close()
