a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
me = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    me = c

ma = a
if b > a and b > c:
    ma = b
if c > a and c > b:
    ma = c
print('O maior valor digitado foi {}'.format(ma))
print('O menor valor digitado foi {}'.format(me))
