import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:

  while True:
      Servidor = input('Digite: ') + '\n'
      cliente.sendto(Servidor.encode(), ("127.0.0.1", 7777))
      data, sender = cliente.recvfrom(1024)
      print (sender[0] + " Resposta: " + data.decode())
      if data.decode() == "sair\n" or Servidor == "sair\n":
         break

  cliente.close()
except Exception as error:
    print("Erro =>  ", error)
    