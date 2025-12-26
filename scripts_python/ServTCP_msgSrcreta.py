import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

file = open("mensagem.txt", "w")

try:
  server.bind(("0.0.0.0", 7878))
  server.listen(5)
  print("Conectado ...")
  
  client_socket, address = server.accept()
  print("Conexão estabelecida:", address[0])

  while True:
      data = client_socket.recv(1024).decode("utf-8")
      if data == "senhasecreta\n":
          client_socket.send(b"Acesso Permitido")
      

except Exception as error:
    print("Erro: =>", error)
    server.close()