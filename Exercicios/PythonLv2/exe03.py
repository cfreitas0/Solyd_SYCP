''' 8)  Média de notas Peça duas notas. Se a média for maior ou igual a 7,
    mostre “Aprovado”. Caso contrário, mostre “Reprovado”.'''

nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))

if (nota1 + nota2) /2 >= 7:
  print('Aprovado!')
else:
  print('Reprovado!')