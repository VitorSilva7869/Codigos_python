qu = str(input('Qual é o seu sexo? [M/F]: ')).strip().upper()[0]
while qu not in 'MF':
    qu = str(input('Esse sexo não existe seu jumento, digite novamente: ')).strip().upper()[0]
print('O sexo {} foi salvo no banco de dados da JUMELANDIA, pode entrar!!'.format(qu))
