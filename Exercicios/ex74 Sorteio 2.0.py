from random import randint
n = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10), )
print(f'Eu sortieei os valores: ',end='')
for m in n:
    print(f'{m} ', end='')
print(f'\nO numero maior sortiado foi {max(n)}')

print(f'O nnumero menor sortiado foi {min(n)}')