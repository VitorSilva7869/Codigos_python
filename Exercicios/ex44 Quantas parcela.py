print('{:=^80}'.format('lojas STORVITOR'))
pr = float(input('Preço do produto: '))
print('''[ 1 ] A vista dinheiro/cheque:
10% de desconto.
[ 2 ] A vista no cartão:
5% de desconto.
[ 3 ] Em até 2x no cartão:
Preço normal.
[ 4 ] 3x ou mais no cartão:
20% de juros.''')
op = int(input('Qual opição? '))
if op == 1:
    to = pr - (pr * 10 / 100)
elif op == 2:
    to = pr - (pr * 5 / 100)
elif op == 3:
    to = pr
    pa = to / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f} SEM JUROS'.format(pa))
elif op == 4:
    to = pr + (pr * 20 / 100)
    tp = int(input('Quantas parcela? '))
    par = to / tp
    print('Sua compra será parcelada em 3x vai custar R${:.2f} no final COM JUROS'.format(tp, par))
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(pr, to))