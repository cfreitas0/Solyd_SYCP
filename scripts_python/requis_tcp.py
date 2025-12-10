import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#cliente.settimeout(1) => OPCIONAL 
try:
    cliente.connect(("127.0.0.1", 7878))
    cliente.send(b"salve salve\n")
    pacote_resposta = cliente.recv(999).decode()
    print(pacote_resposta)
except:
    print('erro!')
