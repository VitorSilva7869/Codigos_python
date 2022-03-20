while True:
    print('-=' * 40)
    nu = int(input('Quer ver a tabuada de qual valor? '))
    print('-=' * 40)
    if nu < 0:
        break
    for c in range(1, 11):
        print(f'{nu} X {c:2} = {nu*c}')
print('A tabuada esta sendo encerrado por não ter numeros negativos ainda. Obrigado por te ussado')