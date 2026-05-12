num_v = int(input(' digite se deseja utilizar 2 ou 3 variaveis na formula: '))

Possibilidade = [True,False]

if num_v == 3:
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
    print(f'o total de linhas foi de \033[32m{contador}\033[m')
    print(f'o total de linhas com resulto True \033[32m{totalV}\033[m')
    print(f'o total de linhas com resulto False \033[32m{totalF}\033[m')
    print('-'*120)
    if contador == totalV:
        propriedade = 'essa formula é taltologica'
    elif contador == totalF:
        propriedade = 'essa formula é contraditoria'
    else:
        propriedade = 'essa formula é satisfatoria'
    print(f'Esta formula é: \033[31m{propriedade}\033[m')
    print('-'*120)

elif num_v == 2:

    print('-------------------')
    qual_formula = input(f'Digite a fórmula (use Q e R como variaves:):').lower()
    print('-------------------')

    contador = 0
    totalF = 0
    totalV = 0


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
            print(f'Q = {q} \t R = {r} \tformula = {resultado_f}')

    print('-'*120)
    print(f'o total de linhas foi de \033[33m{contador}\033[m')
    print(f'o total de linhas com resulto True \033[33m{totalV}\033[m')
    print(f'o total de linhas com resulto False \033[33m{totalF}\033[m')
    print('-'*120)
    if contador == totalV:
        propriedade = 'essa formula é taltologica'
    elif contador == totalF:
        propriedade = 'essa formula é contraditoria'
    else:
        propriedade = 'essa formula é satisfatoria'
    print(f'Esta formula é: \032[31m{propriedade}\033[m')
    print('-'*120)

else:
    print('\033[31mvalor não aceito!\033[m')