from datetime import date
at = date.today().year
con = 0
conm = 0
for c in range(1, 8):
    ida = int(input('Em que ano a \033[1;34m{}°\033[m pessoa nasceu: '.format(c)))
    ano = at - ida
    if ano >= 18:
       con += 1
    elif ano < 18:
        conm += 1
print('Ao todo tivemos \033[1;34m{}\033[m pessoas maiores de idade'.format(con))
print('Ao todo tivemos \033[1;34m{}\033[m pessoas menor de idade'.format(conm))
