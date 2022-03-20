print('\033[1;33mGerenciador de PA')
print('-=' * 20)
p1 = int(input('Primeiro termo: '))
pa = int(input('Razão de PA: '))
ter = p1
co = 1
to = 0
ma = 10
while ma != 0:
    to = to + ma
    while co <= to:
        print('{} -> '.format(ter), end='')
        ter += pa
        co += 1
    print('Pausa')
    ma = int(input('Quanto termo vc quer mostrar a mais: '))
print('Prosseso terminado com {} termos'.format(to))