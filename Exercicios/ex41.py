from datetime import date
an = int(input('Qual ano vc nasceu: '))
at = date.today().year
mm = at - an
print('Vc nasceu em {} e tem {} anos, e pela CNN (Confederação Nacional de Natação)'.format(an, mm))
if mm <= 9:
    print('Vc é MIRIM.')
elif mm <= 14:
    print('Vc é INFANTIL.')
elif mm <= 19:
    print('Vc é JUNIOR')
elif mm <= 25:
    print('Vc é SENIOR')
elif mm >= 26:
    print('VC é MASTER')
