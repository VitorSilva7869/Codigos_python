lis = ('Lapis', 1.25,
       'borracha', 2,
       'caderno', 15.90,
       'estojo', 25,
       'tranferidor', 4.20)
print('-' * 30)

for it in range(0, len(lis)):
    if it % 2 == 0:
        print(f'{lis[it]:.<30}', and = '')
    else:
        print(f'R${lis[it]:>7.2f}')
