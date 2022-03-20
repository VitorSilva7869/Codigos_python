ti = ('1°Fortaleza', '2°Atletico-PR', '3°Atletico-GO', '4°Bragantino', '5°Bahia'
         , '6°Fluminense', '7°Palmeiras', '8°Flamengo', '9°Atletico-MG', '10°Corintias'
      , '11°Ceará SC', '12°Santos', '13°Cuiabá', '14°Sport Recife', '15°São Paulo', '16°Juventude',
      '17°internacional', '18°Gremio', '19°America-MG', '20°Chapecoense')
print('-=' * 50)
print('Clasificação do Brasileirão 2022')
for t in ti:
    print(f'{t}')
print('-=' * 50)
print(f'Os 5 primeiros são {ti[0:5]}')
print(f'Os 4 ultimos são {ti[16:20]}')
print(f'Times em ordem alfabetica: {sorted(ti)}')
print(f'O Bahia est ana posoção {ti.index("5°Bahia")+1}°')