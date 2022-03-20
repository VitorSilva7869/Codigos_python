a = [2, 3, 4, 7]
b = a[:] # Esse comando copia a lista A mas sem interferir nela.
b[2] = 8 # Com esse comando eu mudei o numero que estava na posição 2 para 8 sem interferir na lista A
print(f'Lista A: {a}')
print(f'Lista B: {b}')