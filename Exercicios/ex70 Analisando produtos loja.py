print('==-' * 20)
print('                Loja do pika das galixias')
print('==-' * 20)
som = co = men = com = 0
bara = ''
while True:
    no = str(input('Nome do produto: '))
    pr = int(input('Preço: R$'))
    com += 1
    som += pr
    if pr >= 1000:
        co += 1
    if com == 1 or pr < men:
        men = pr
        bara = no
    sn = ' '
    while sn not in 'NS':
        sn = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    if sn == 'N':
        break
print('{:-^40}'.format(' Fim do programa '))
print(f'O total da compra foi R${som:.2f}')
print(f'Temos {co} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {bara} que custa R${men:.2f}')