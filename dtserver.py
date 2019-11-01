import socket
from datetime import datetime

server_sock = socket.socket()
server_sock.bind(("localhost",5000))

server_sock.listen(5)
conn , address = server_sock.accept()

data= conn.recv(1024).decode()
message = str(datetime.now())
conn.send(message.encode())

conn.close()
server_sock.close()
