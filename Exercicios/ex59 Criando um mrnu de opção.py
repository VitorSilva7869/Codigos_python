from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
op = 0
while op != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Mutiplicar
    [ 3 ] Maior 
    [ 4 ] Novos numeros
    [ 5 ] Sair do programa''')
    op = int(input('>>>> Qual é a sua opição?'))
    if op == 1:
        re = n1 + n2
        print('A soma de {} + {} = {}'.format(n1, n2, re))
    elif op == 2:
        re = n1 * n2
        print('A mutiplicação de {} X {} = {}'.format(n1, n2, re))
    elif op == 3:
        if n1 > n2:
            print('O maior numero é {}, o primeiro valor'.format(n1))
        if n2 > n1:
            print('O maior numero é {}, o segundo valor'.format(n2))
        if n1 == n2:
            print('O numero {} e {} são iguais e não tem maior.'.format(n1, n2))
    elif op == 4:
        print('Digite novamente!')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif op == 5:
        print('Finalizando')
    else:
        print('Opição invalida! Tente novamente')
    print('-=' * 20)
print('O programa esta sendo desligado',end= '')
for c in range(1, 5):
    print('.',end= '')
    sleep(1.50)
print('\nO programa foi finalizado, obrigado por ter ultilizado e volte sempre!')
