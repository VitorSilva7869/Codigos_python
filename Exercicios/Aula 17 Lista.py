# num = [2, 5, 9, 1]
# num [2] = 3 #Muda um intem da lista
# num.append(7) #Adiciona um intem no final da lista
# num.sort(reverse=True) #Deixa os intem na ordem aocontraria
# num.insert(2, 5) #Adiciona um intem na posição que vc escolher
# print(f'Essa lista tem {len(num)} elementos') #"len" mostra quantos intem tem na lista
a = [2, 3, 4, 7]
b = a[:]#[:] Esse comando copia uma lista sem conectalas.
b[2] = 8
print(f'lista A: {a}')
print(f'Lista B: {b}')