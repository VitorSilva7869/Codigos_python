#Aula sobre lista
num = [2, 5, 9, 1]
num[2] = 3 #Trocar o numero da lista
num.append(7) #Esse comando adiciona mais um numero a lista
num.sort(reverse=True) #Esse comando organiza os numeros aocontrario
num.insert(2, 0) #Esse comando adicionou o numero 0 na posição 2
#num.pop(2) #Esse comando apaga o numero da posição "2"
if 4 in num: #Esse comando serve para remover um numero. Mas se não tiver esse numero eles mostra o "Else".
    num.remove(4)
else:
    print('Não achei o numero 4')
print(num)
print(len(num)) #Esse comando fala quantos elementos tem na lista
