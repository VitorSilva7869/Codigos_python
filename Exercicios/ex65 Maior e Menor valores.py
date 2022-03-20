maior = menor = som = com = co = 0
sn = 'S'
while sn in 'Ss':
    co = int(input('Digite um numero: '))
    com += 1
    sn = str(input('Quer continuar? [S/N] '))
    som += co
    re = som / com
    if com == 1:
        maior = menor = co
    else:
        if co > maior:
            maior = co
        if co < menor:
            menor = co
print(f'Voce digitou {com} numeros, e a media foi {re}')
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
