import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to localhost and a port
server_socket.bind(('0.0.0.0', 9999))
server_socket.listen(1)
print("Server is listening on port 9999...")

# Accept a connection
client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

# Receive and respond
while True:
    data = client_socket.recv(1023).decode()
    if  data == 'exit':
        break
    print(f"Client says: {data}")
    response = input("Enter reply: ")
    client_socket.send(response.encode())
    if response =='exit':
        client_socket.close()
        server_socket.close()
