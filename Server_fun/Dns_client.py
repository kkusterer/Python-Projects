import socket
import webbrowser
import os

def open_url_new_window(url):
    """Opens the given URL in a new Chrome window."""
    if os.name == 'posix':
        os.system(f"{url}")

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect(('0.0.0.0', 9999))

# Send messages
while True:
    message = input("You: ")
    if message == 'exit':
        client_socket.close()

    client_socket.send(message.encode())
    server = client_socket.recv(1023).decode()

    if server =='':
        message = input("You: ")
        client_socket.send(message.encode())
        server = client_socket.recv(1023).decode()

    else:
        print(f"Server: {server}")




# Close socket
client_socket.close()

