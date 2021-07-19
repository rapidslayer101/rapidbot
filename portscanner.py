import socket
import _thread

print("Please enter an IP Address to scan.")
target = input("> ")

print("*" * 40)
print("* Scanning: " + target + " *")
print("*" * 40)

for port in range(1, 65535):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def scan(port, x):
        result = s.connect_ex((target, port))
        if result == 0:
            print("Port: " + str(port) + " Open")
        s.close()

    x = 0
    _thread.start_new_thread(scan, (port, x))