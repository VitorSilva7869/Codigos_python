re = 0
co = 0
n1 = 0
while n1 != 999:
    n1 = int(input('Digite um numero [999 para parar]: '))
    co += 1
    r1 = co - 1
    if n1 != 999:
        re += n1
print('Voce digitou {} numeros e a soma é {}'.format(r1, re))
