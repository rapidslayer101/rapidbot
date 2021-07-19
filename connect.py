import socket
s = socket.socket()
port = 8079
s.connect(('172.18.136.166', port))
print(s.recv(1024).decode())
s.close()