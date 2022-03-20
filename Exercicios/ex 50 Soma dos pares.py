so = 0
co = 0
for c in range(1, 7):
    nu = int(input('Digite o {} valor: '.format(c)))
    if nu % 2 == 0:
        so += nu
        co += 1
print('Voce informou {} numeros PARES e a soma foi {}'.format(co, so))
