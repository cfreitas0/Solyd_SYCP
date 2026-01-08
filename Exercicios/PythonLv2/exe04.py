''' 9)  Número positivo, negativo ou zero Peça um número e informe se ele é
    positivo, negativo ou zero. '''

numero = float(input('Digite um numero: '))

if numero == 0:
    print('O número é zero.')
elif numero > 0:
    print('O número é positivo.')
else:
    print('O número é negativo.')