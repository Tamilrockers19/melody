import socket
client_sock = socket.socket()
client_sock.connect(("localhost",5000))

message = "current time and date"
client_sock.send(message.encode())
data= client_sock.recv(1024).decode()
print("The message from server is ",data)
client_sock.close()
