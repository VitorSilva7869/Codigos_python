co = ho = mu = 0
while True:
    print('-' * 30)
    print('   Cadastre uma pessoa')
    print('-' * 30)
    ida = int(input('Idade: '))
    fm = ' '
    while fm not in 'MF':
        fm = str(input('Sexo: [M/F] ')).strip().upper()[0]
        print('-' * 30)

    sn = ' '
    if fm == 'M':
        ho += 1
    elif fm == 'F' and ida <= 20:
        mu += 1
    while sn not in 'SN':
        sn = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if sn == 'N':
        break
    elif ida >= 18:
        co += 1
print('-' * 30)
print(f'Total de pessoas com mais de 18 anos: {co + 1}')
print(f'Ao todo temos {ho} homens cadastrados.')
print(f'E temos {mu} mulheres com menos de 20 anos')