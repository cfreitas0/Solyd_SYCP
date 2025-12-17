# cSpell:disable
import socket

HOST = "127.0.0.1"
PORT = 7777
TIMEOUT = 20

# Cria o socket
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Define o timeout
cliente.settimeout(TIMEOUT)

print("Chat UDP iniciado. Digite 'sair' para encerrar.")

try:
    # Loop principal do chat
    while True:
        mensagem = input("Você: ")

        # Condição de saída
        if mensagem.lower() == 'sair':
            break

        # Envia a mensagem (codificada) para o servidor
        cliente.sendto(mensagem.encode(), (HOST, PORT))

        try:
            # Tenta receber uma resposta
            dados, servidor = cliente.recvfrom(1024)
            print(f"Resposta de {servidor}: {dados.decode()}")
        except socket.timeout:
            print(f"-> Nenhuma resposta do servidor em {TIMEOUT} segundos. Você pode enviar outra mensagem.")
        except Exception as e:
            print(f"-> Erro ao receber dados: {e}")

except Exception as e:
    print(f"-> Ocorreu um erro na conexão: {e}")
finally:
    # Garante que o socket será fechado no final
    print("Encerrando o chat...")
    cliente.close()