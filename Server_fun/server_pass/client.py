import socket
port = 9998
i = 0

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('0.0.0.0', port))


while True:
    user_user = input("enter username: ")
    client_socket.send(user_user.encode())
    response = client_socket.recv(1024).decode()
    if response == '1':
        i += 1
        break
    else:
        print("enter correct username")

while True:
    user_pass = input("enter password: ")
    client_socket.send(user_pass.encode())
    response = client_socket.recv(1024).decode()
    if response == '1':
        i += 1
        break
    else:
        print("enter correct password")

if i == 2:
    print("Welcome!")
else:
    print("Wrong username and/or password")
