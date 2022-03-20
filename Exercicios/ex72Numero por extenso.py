co = 'Zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'deis', 'onze', 'doze', 'treze', 'cartoze', 'quinze', 'desseseis', 'dessesete', 'desoito', 'desenove', 'vinte'

while True:
    nu = int(input('Digite um numero: '))
    if 0 <= nu <= 20:
        break
    print('Tente novamente.', end=' ')
print(f'Vc digitou o numero {co[nu]}')