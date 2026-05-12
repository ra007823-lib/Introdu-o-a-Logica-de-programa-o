Possibilidade = [True,False]

print('-------------------')
print('Formula: (M v N) ^ ¬(Q v P) ^ (¬M v Q) ^ (¬N v R)')
print('-------------------')
contador = 0
for M in Possibilidade:
    for N in Possibilidade:
        for O in Possibilidade:
            for P in Possibilidade:
                for Q in Possibilidade:
                    for R in Possibilidade:
                        if (M or N) and not(O or P) and (not M or Q) and (not N or R):
                            resultado = 'Verdadeiro'
                        else:
                            resultado = 'Falso'
                        contador +=1
                        print('-'*120)
                        print(f'M = {M} \t N = {N} \t O = {O} \t Q = {Q} \t P = {P} \t R = {R} \t Formula = {resultado}')
print(f'foram rodadas {contador} vezes o codigo.')