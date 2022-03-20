so = 0
me = 0
maiorho = 0
nove = ''
totmu = 0
for c in range(1, 5):
    print('-' * 5, end= ' ')
    print('{}° PESSOA '.format(c), end= '')
    print('-' * 5)
    no = str(input('Nome: '))
    ida = int(input('Idade: '))
    se = str(input('Sexo [M/F]: '))
    so += ida
    if c == 1 and se in 'Mm':
        maiorho = ida
        nove = no
    if se in 'Mm' and ida > maiorho:
        maiorho = ida
        nove = no
    if se in 'Ff' and ida < 20:
        totmu += 1
me = so / 4
print('A media da idade do grupo é de {:.2f} anos'.format(me))
print('O nome do mais velho é {} e tem {} anos.'.format(nove, maiorho))
print('Ao todo sao {} mulheres com menos de 20 anos'.format(totmu))

