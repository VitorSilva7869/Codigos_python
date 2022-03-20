n = int(input('Quantos termos vc quer mostrar: '))
t1 = 0
t2 = 1
print('~' * 30)
print('{} -> {}'.format(t1, t2), end='')
co = 3
while co <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    co += 1
print(' -> FIM')
