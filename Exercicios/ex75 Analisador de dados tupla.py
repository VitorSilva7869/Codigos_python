n1 = (int(input('Digite um numero: ')),
     int(input('Digite outro numero: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite o ultimo numero: ')))
va = f'{n1}'
co = 1
print(f'Vc digitou os valores {va}')
print(f'O valor 9 apareceu {n1.count(9)} vezes.')
if 3 in n1:
    print(f'O valor 3 apareceu na {n1.index(3)+1}° posição')
else:
    print('Infelizmente o valor 3 não foi digitado')
print(f'Os valores pares digitados foram', end=' ')
for n in n1:
    if n %2 == 0:
        print(n, end=' ')