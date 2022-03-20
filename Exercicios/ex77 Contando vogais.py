palavras = ('Punheteiro', 'Padeiro', 'Prostituta', 'Xvideos',
            'Entragador', 'Encanador', 'Atriz', 'Nikeiro')
for p in palavras:
    print(f'\nNas palavras {p.upper()} temos', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
