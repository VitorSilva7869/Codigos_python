di = float(input('Qual é a distancia da sua viagem? '))
print('Voce esta preste a percorrer uma viggem de {}KM'.format(di))
pr = di * 0.50 if di <=200 else di * 0.45
print('E o preçoo da sua viagem é de R${:.2f}'.format(pr))

