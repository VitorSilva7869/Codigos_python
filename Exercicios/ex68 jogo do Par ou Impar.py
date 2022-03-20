from random import randint

print('>-<' * 50)
print('Vamos jogar IMPAR ou PAR ?')
print('>-<' * 50)
co = 0
while True:
    com = randint(0, 50)
    va = int(input('Digite um valor: '))

    op = ' '
    som = com + va
    re = som % 2
    while op not in 'PI':
        op = str(input('IMPA ou PAR? [I/P] ')).strip().upper()[0]
        print('-' * 100)
        print(f'Voce jogou {va} e o computador {com}. O total de {som} é', end=' ')
    if re == 0:
        print('par.')
        print('-' * 100)
        if op == 'P':
            if som % 2 == 0:
                print('Parabens voce ganhou.')
                print('Vamos recomeçar....')
                print('-' * 100)
                co += 1
            else:
                print('Voce PERDEU.')
                print('-=' * 50)
                break
    else:
        print('impar')
        print('-' * 100)
        if op == 'I':
            if som % 2 == 0:
                print('Voce PERDEU.')
                break
            else:
                print('Parabens voce ganhou.')
                print('Vamos recomeçar....')
                print('-=' * 50)
                co += 1
    print('VAmos recomeçar...')
print('GAMER OVER, voce ganhou {} vezes.')
