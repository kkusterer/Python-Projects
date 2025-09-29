import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('0.0.0.0', 9999))

while True:
    message = input("You: ")
    if message == 'exit':
        break
    client_socket.send(message.encode())
    response = client_socket.recv(1023).decode()
    print(f"Server: {response}")

    if message =='exit':
        break

client_socket.close()

