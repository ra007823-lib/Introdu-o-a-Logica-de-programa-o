Possibilidade = [True,False]

print('-------------------')
print('Formula: (M v N) ^ ¬(Q v P) ^ (¬M v Q) ^ (¬N v R)')
print('-------------------')
contador = 0
totalF = 0
totalV = 0
for M in Possibilidade:
    for N in Possibilidade:
        for O in Possibilidade:
            for P in Possibilidade:
                for Q in Possibilidade:
                    for R in Possibilidade:
                        if (M or N) and not(O or P) and (not M or Q) and (not N or R):
                            resultado = 'Verdadeiro'
                            totalV +=1 
                        else:
                            resultado = 'Falso'
                            totalF +=1
                        contador +=1
                        print('-'*120)
                        print(f'M = {M} \t N = {N} \t O = {O} \t Q = {Q} \t P = {P} \t R = {R} \t Formula = {resultado}')
print('-'*120)
print(f'foram rodadas {contador} vezes o codigo.')
print(f'o total de linhas com resulto True {totalV}')
print(f'o total de linhas com resulto False {totalF}')
print('-'*120)
if resultado == totalV:
    print('essa formula é taltologica')
elif resultado == totalF:
    print('essa formula é contraditoria')
else:
    print('essa formula é satisfatoria')