comparacao = []
for i in range(2):

    Possibilidade = [True,False]

    
    print('-'*120)
    qual_formula = input(f'Digite a fórmula (use A, B e C como variaves:):').lower()
    print('-'*120)

    contador = 0
    totalF = 0
    totalV = 0
    compara = []

    for a in Possibilidade:
        for b in Possibilidade:
            for c in Possibilidade:
                if eval(qual_formula):
                    resultado_f = 'verdadeiro'
                    totalV +=1 
                else:
                    resultado_f = 'falso'
                    totalF +=1
                    contador +=1
                compara.append(resultado_f)
    comparacao.append(compara)

    print('-'*120)
    print(f'A = {a} \t B = {b} \t C = {c} \tformula = {resultado_f}')
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

    
    print(comparacao)
