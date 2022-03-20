print('=' * 50)
print('               10 TERMOS DE UM PA')
print('=' * 50)
t1 = int(input('Primeiro termo: '))
ra = int(input('Primeiro termo: '))
de = t1 + (10 - 1) * ra
for c in range(t1, de + ra, ra):
    print('{} ->'.format(c), end=' ')
print('Acabou')