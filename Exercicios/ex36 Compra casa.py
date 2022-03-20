ca = float(input('valor da casa: R$'))
sa = float(input('Salario do comprador: R$'))
an = float(input('Quantos anos de financiamento: R$'))
pr = ca / (an * 12)
mi =sa * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação sera de R${:.2f}'.format(ca, an, pr))
if pr <= mi :
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')
