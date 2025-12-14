import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  server.bind(("0.0.0.0", 9999))
  server.listen(5)
  print("listen...")

  server.close()

except Exception as error:
  print("Erro: =>", error)
