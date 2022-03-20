print('\033[1;33mGerenciador de PA')
print('-=' * 20)
p1 = int(input('Primeiro termo: '))
pa = int(input('Razão de PA: '))
ter = p1
co = 1
while co <= 10:
    print('{} -> '.format(ter), end='')
    ter += pa
    co += 1
print('Pausa')
qu = int(input('Quanto termo vc quer mostrar a mais: '))

