sa = float(input('Qual é o salario do funcionarios'))
if sa <= 1250:
    no = sa + (sa * 15 / 100)
else:
    no = sa + (sa * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(sa, no))
