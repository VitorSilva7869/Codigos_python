co = so = 0
while True:
    nu = int(input('Digite um numero [999 ACABA]: '))
    if nu == 999:
        break
    so += nu
    co += 1
print(f'Voce digitou {co} numeros e a somas desses valores é {so}')
