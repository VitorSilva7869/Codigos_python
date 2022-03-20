from time import sleep
from random import randint
it = ('Pedra', 'Papel', 'Tesoura')
com = randint(1, 2)
print('''Escolha sua opção:
 { 0 } PEDRA
 { 1 } PAPEL
 { 2 } TESOURA''')
op = int(input('Qual sua jogada de mestre? '))
print('JO')
sleep(1)
print('Ken')
sleep(1)
print('PO!!')
print('-=-' * 50)
print('O computador jogou {}'.format(it[com]))
print('Vc jogou {}'.format(it[op]))
print('-=-' * 50)
if com == 0:
    if op == 0:
        print('EMPATE')
    elif op == 1:
        print('Vc VENCEU')
    elif op == 2:
        print('Vc PERDEU')
elif com == 1:
    if op == 0:
        print('Vc PERDEU')
    elif op == 1:
        print('EMPATE')
    elif op == 2:
        print('Vc VENCEU')
elif com == 2:
    if op == 0:
        print('Vc VENCEU')
    elif op == 1:
        print('Vc PERDEU')
    elif op == 2:
        print('EMPATE')