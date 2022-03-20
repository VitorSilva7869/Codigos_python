nu = int(input('Digite um numero: '))
tot = 0
for c in range(1, nu + 1):
    if nu % c == 0:
        print('\033[1;32m', end='')
        tot += 1
    else:
        print('\033[m', end='')
    print('{} '.format(c), end='')
print('\n\033[m0 numero {} foi divisivel {} vezes'.format(nu, tot))
if tot == 2:
    print('Então ele é PRIMO!')
else:
    print('Então ele não é primo!')
