Possibilidade = [True,False]

print('-------------------')
print('Formula: (P v Q) ^ ¬R')
print('-------------------')

for P in Possibilidade:
    for Q in Possibilidade:
        for R in Possibilidade:
            if (P or Q) and not R:
                resultado_f = 'verdadeiro'
            else:
                resultado_f = 'falso'
            print(f'P = {P} \t Q = {Q} \t R = {R} \tformula = {resultado_f}')