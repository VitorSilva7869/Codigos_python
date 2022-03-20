from math import factorial
n = int(input('Digite um numero para calcular o fatorial: '))
f = factorial(n)
print('O fatorial de {} ='.format(n, f), end= ' ')
for c in range( n, +1, -1):
    print('{} X '.format(c),end= '')
print('1 = {}'.format(f))
