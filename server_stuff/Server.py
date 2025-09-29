import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('0.0.0.0', 9999))
server_socket.listen(1)
print("Server is listening on port 9999...")

client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

while True:
    data = client_socket.recv(1023).decode()
    if  data == 'exit':
        break
    print(f"Client says: {data}")
