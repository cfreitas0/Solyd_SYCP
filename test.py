import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cliente.connect(b'127.0.0.1', 777)
print (cliente.recvfrom)