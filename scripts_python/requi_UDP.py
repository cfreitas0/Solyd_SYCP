import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    cliente.sendto(b"SALVE", ("127.0.0.1", 777))
    print (cliente.recvfrom(1024))
except:
    print ('Algum erro ocorreu..')