Possibilidade = [True,False]

print('-------------------')
qual_formula = input(f'Digite a fórmula (use P, Q e R como variaves:):').lower()
print('-------------------')

contador = 0
totalF = 0
totalV = 0

for p in Possibilidade:
    for q in Possibilidade:
        for r in Possibilidade:
            if eval(qual_formula):
                resultado_f = 'verdadeiro'
                totalV +=1 
            else:
                resultado_f = 'falso'
                totalF +=1
            contador +=1
            print('-'*120)
            print(f'P = {p} \t Q = {q} \t R = {r} \tformula = {resultado_f}')

print('-'*120)
print(f'o total de linhas foi de {contador}')
print(f'o total de linhas com resulto True {totalV}')
print(f'o total de linhas com resulto False {totalF}')
print('-'*120)
if contador == totalV:
    propriedade = 'essa formula é taltologica'
elif contador == totalF:
    propriedade = 'essa formula é contraditoria'
else:
    propriedade = 'essa formula é satisfatoria'
print(f'Esta formula é: \033[1m{propriedade}\033[0m')
print('-'*120)