pe = float(input('Qual o seu peso? (KG) '))
al = float(input('Qual é sua altura? (M)'))
imc = pe / (al ** 2)
print('O IMC dessa pessoa é de {:.2f}'.format(imc))
if imc <= 18.5:
    print('Cuidado vc ja pode limpar uma mangueira por dentro.')
elif imc <= 25:
    print('Vc esta de boa fique tranquilo.')
elif imc <= 30:
    print('Faça um exercicio para tirar essa pochete ai.')
elif imc <= 40:
    print('Meu irmão vc ja virou uma BALEIA.')
elif imc > 40:
    print('Brother vai procurar uma ajuda porque sua especie de BALEIA é rara. ')