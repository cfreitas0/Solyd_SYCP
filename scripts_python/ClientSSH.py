import paramiko

host = "127.0.0.1"
user = "dom"
passwd = "nvme"


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=user, password=passwd)

while True:
    stdin, stduot, stderr = client.exec_command(input('Digite um Comando: '))
    for line in stduot.readlines():
        print(line.strip())

    erro = stderr.readlines()
    if erro:
        print(erro)


    
    