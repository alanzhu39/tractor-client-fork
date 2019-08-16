import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

# client socket initialized
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # connects to server and sends data (byte)
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', repr(data))
