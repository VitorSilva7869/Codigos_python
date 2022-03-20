n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
if n1 > n2:
    print('O numero {} é maior que {}.'.format(n1, n2))
elif n2 > n1:
    print('O nemero {} é maior que {}.'.format(n2, n1))
else:
    print('Os numeros são iguais.')
