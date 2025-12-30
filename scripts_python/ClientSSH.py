import paramiko

host = "127.0.0.1"
user = "dom"
passwd = "nvme"

try:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=user, password=passwd)
except Exception as e:
    print('Erro =>', e) 
    