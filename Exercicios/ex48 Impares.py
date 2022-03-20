so = 0
cot = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cot = cot + 1
        so = so + c
print('A soma de todos os {} valores solicitados é {}'.format(cot, so))
