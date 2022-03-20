n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Segunda nota: '))
n4 = (n1 + n2 + n3) / 3
print('Sua media foi {:.1f}'.format(n4))
if n4 >= 5 and n4 < 8:
    print('Parabens vc passou arrastado, estude mais na proxima.')
elif n4 >= 8:
    print('Otima nota, vc esta passado.')
elif n4 < 4:
    print('Vc foi reprovado, estude mais na proxima')


