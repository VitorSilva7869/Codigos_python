fra = str(input('\033[1;34mDigite uma frase: ')).strip().upper()
pa = fra.split()
ju = ''.join(pa)
inv = ''


for let in range(len(ju) -1, -1, -1):
    inv += ju[let]
print('\033[1;34mO inverso de \033[1;32m{}\033[m \033[1;34mé \033[1;31m{}\033[m\033[1;34m'.format(fra, inv),end=' ')
if inv == ju:
    print('e quer dizer que ele é um palidromo.')
else:
    print('e quer dizer que ele não é um palidromo.')
