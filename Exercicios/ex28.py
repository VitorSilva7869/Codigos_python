from random import randint
cpm = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. tente adivinhar...')
print('-=-' * 20)
jog = int(input('Em que numero eu pensei?'))
if jog == cpm:
    print('Parabens! Voce conseguiu me vencer!')
else:
    print('Eu ganhei seu otario! Pensei no {} e nao no {}'.format(cpm, jog))
