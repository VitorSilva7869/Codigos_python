from random import randint
com = randint(0, 10)
res = int(input('Sou seu computador...\nSerá que vc consegue adivinhar qual numero eu pensei de 0 a 10?\nQual é o seu palpite? '))
ten = 0
while com != res:
    ten += 1
    if com < res:
        res = print('Menos! ', end= ' ')
    elif com > res:
        res = print('Maior! ', end= ' ')
    res = int(input('Tente novamente: '))
print('Parabens vc acertou em {} tentativas, o numero é {}'.format(ten, com))