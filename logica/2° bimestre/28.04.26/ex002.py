Possibilidade = [True,False]

print('-------------------')
print('Formula: (P v Q) ^ ¬R')
print('-------------------')

contador = 0
totalF = 0
totalV = 0

for P in Possibilidade:
    for Q in Possibilidade:
        for R in Possibilidade:
            if (P or Q) and not R:
                resultado_f = 'verdadeiro'
                totalV +=1 
            else:
                resultado_f = 'falso'
                totalF +=1
            contador +=1
            print('-'*120)
            print(f'P = {P} \t Q = {Q} \t R = {R} \tformula = {resultado_f}')

print('-'*120)
print(f'foram rodadas {contador} vezes o codigo.')
print(f'o total de linhas com resulto True {totalV}')
print(f'o total de linhas com resulto False {totalF}')
print('-'*120)
if contador == totalV:
    print('essa formula é taltologica')
elif contador == totalF:
    print('essa formula é contraditoria')
else:
    print('essa formula é satisfatoria')