# Import socket module
import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 8079

# connect to the server on local computer
s.connect(('172.16.250.106', port))

# receive data from the server
print(s.recv(1024))
# close the connection
s.close()