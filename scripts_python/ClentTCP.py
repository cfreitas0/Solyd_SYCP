# cSpell:disable
import socket

# Boas práticas: Definir constantes para endereço e porta
HOST = "127.0.0.1"
PORT = 7878
TIMEOUT = 25  # Timeout em segundos

print("--- Iniciando Chat TCP ---")

# A variável do socket é declarada fora do try para estar acessível no finally
cliente_socket = None
try:
    # 1. Cria o socket TCP
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. Define um timeout para operações de bloqueio (connect, recv)
    cliente_socket.settimeout(TIMEOUT)

    # 3. Conecta-se ao servidor (operação pode falhar)
    print(f"Conectando ao servidor em {HOST}:{PORT}...")
    cliente_socket.connect((HOST, PORT))
    print("Conexão estabelecida! Digite 'sair' para encerrar o chat.")

    # 4. Loop principal do chat
    while True:
        mensagem_para_enviar = input("Você: ")

        if mensagem_para_enviar.lower() == 'sair':
            break

        # Envia a mensagem para o servidor conectado
        cliente_socket.sendall(mensagem_para_enviar.encode('utf-8'))

        # Aguarda a resposta do servidor
        # Em TCP, uma resposta de 0 bytes significa que o outro lado fechou a conexão
        resposta_servidor = cliente_socket.recv(1024)
        if not resposta_servidor:
            print("-> O servidor encerrou a conexão.")
            break
        
        print(f"Servidor: {resposta_servidor.decode('utf-8')}")

# Tratamento de erros específicos
except socket.timeout:
    print(f"Erro: Tempo de espera ({TIMEOUT}s) esgotado. O servidor não respondeu a tempo.")
except ConnectionRefusedError:
    print(f"Erro: Conexão recusada. Verifique se o servidor está rodando em {HOST}:{PORT}.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
finally:
    # 5. Garante que o socket seja fechado, se tiver sido criado
    if cliente_socket:
        print("--- Encerrando a conexão ---")
        cliente_socket.close()
