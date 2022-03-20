valo = []
mai = 0
men = 0
for cout in range(0, 5):
    valo.append(int(input(f'Digite um numero para a possição {cout} : ')))
    if cout == 0:
        mai = men = valo[cout]
    else:
        if valo[cout] > mai:
            mai = valo[cout]
        if valo[cout] < men:
            men = valo[cout]
print('=' * 40)
print(f'Voce digitou os valores: {valo}')
print(f'O maior valor digitado foi {mai} na posições', end= ' ')
for i, v in enumerate(valo):#enumerate enumera os valores
    if v == mai:
        print(f'{i}....', end='')
print()
print(f'O maior valor digitado foi {men} nas posições', end='')
for i, v in enumerate(valo):
    if v == men:
        print(f'{i}...', end= '')
