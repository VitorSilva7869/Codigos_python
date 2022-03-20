from datetime import date
at = date.today().year
ge = str(input('Qual é seu genero MASCULINO ou FEMININO? '))
na = int(input('Ano de nascimento: '))
id = at - na
print('Quem nasceu em {} tem {} anos em {}.'. format(na, id, at))
if ge == ('Masculino'):
    id == 18
    print('VC tem que se alistar ao exercito IMEDIATAMENTE')
elif ge == ('Masculino'):
    id > 18
    print('VC ja passou da idade vagabundo, corre logo para se alistar se não vai pagar uma muta de 1000R$')
elif ge == ('Masculino'):
    id < 18
    sal = 18 - id
    ano = at + sal
    print('Vc so vai poder se alistar em {} quando tiver 18 anos'.format(ano))
elif ge == ('Feminino'):
    print('Por vc ser do genero Feminino não é obrigatorio se alistar ao exercito')