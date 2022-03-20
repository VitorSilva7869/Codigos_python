print('-='*20)
print('Analisar de triagolo')
print('-='*20)
r1 = float(input('Primeiro segimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Teceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMAR triangulo', end=' ')
    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISOSCALES')
else:
    print('Os segmento acima NAO PODEM FORMA triangulo')



