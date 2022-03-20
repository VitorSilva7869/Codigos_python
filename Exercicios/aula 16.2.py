valores = []
for cout in range(0,5):
    valores.append(int(input('Digite um valor: '))) #Esse codigo serve para perguntar e colocar o numero na lista.
#valores.append(5)
#valores.append(9)
#valores.append(4)

for c, v in enumerate(valores): #O codigo vai  enumereit pega a chave quanto o valor para mostrar onde estar os valores
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')