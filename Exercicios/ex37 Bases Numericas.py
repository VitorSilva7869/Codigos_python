nu = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases da conversão: 
[ 1 ] converter para Binario? 
[ 2 ] converter para Octal? 
[ 3 ] converter para Hexadecimal?''')
ope = int(input('Sua opção: '))
if ope == 1:
    print('{} convertido para BINARIO é igual a {}'.format(nu, bin(nu)[2:]))
elif ope == 2:
    print('{} convertido para OCTAL é igual a {}'.format(nu, oct(nu)[2:]))
elif ope == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(nu, hex(nu)[2:]))
else:
    print('Opição invalida')
