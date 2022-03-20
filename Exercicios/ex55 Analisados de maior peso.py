maior = 0
menor = 0
for c in range(1, 6):
    pe = int(input('Qual o peso da {}° pessoa: '.format(c)))
    if c == 1:
       maior = pe
       menor = pe
    else:
        if pe > maior:
            maior = pe
        if pe < menor:
            menor = pe
print('O maior peso lido foi de \033[1;32m{}Kg\033[m'.format(maior))
print('o menor peso lido foi de \033[1;32m{}Kg'.format(menor))