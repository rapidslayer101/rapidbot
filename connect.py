import socket
s = socket.socket()
port = 8079
s.connect(('172.16.226.190', port))
print(s.recv(1024).decode())
s.close()