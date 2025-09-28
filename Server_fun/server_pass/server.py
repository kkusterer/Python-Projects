import socket
port = 9998
password = '1234'
username = "kaleb"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind(('0.0.0.0', port))
server_socket.listen(1)
print(f"Server is listening on port {port}...")

client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

try:
        while True:

            user_user = client_socket.recv(1023).decode()
            
            if  user_user == username:
                response = '1'
                client_socket.send(response.encode())
                print(f"client username: {user_user}")
                break

            if user_user != username:
                response = '2'
                client_socket.send(response.encode())
            

        while True:

            user_pass = client_socket.recv(1023).decode()
            if user_pass == password:
                response = '1'
                client_socket.send(response.encode())
                print(f"client password: {user_pass}")
                break

            if user_pass != password:
                response = '2'
                client_socket.send(response.encode())

except BrokenPipeError:
    client_socket.close()
    print("client disconnected")
                