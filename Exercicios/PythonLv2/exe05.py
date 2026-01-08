''' 10) Login simples Usuário correto: admin Senha correta: 1234 Mostre
    “Acesso permitido” ou “Acesso negado”. '''


print('Admin')
senha = int(input('Digite a senha: '))

if senha == 1234:
  print('Acesso Permitido')
else:
  print('Acesso Negado')
