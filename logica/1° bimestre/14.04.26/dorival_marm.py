proteinas = ['ovo','peixe','frango']
carboidratos = ['arroz','macarrão','batata doce']
saladas = ['espinafre','alface','brocolis']

for i in proteinas:
    for x in carboidratos:
        for y in saladas:
            if (not(i == 'peixe' and x == 'batata doce')) and ((y == 'espinafre')==(i =='ovo')) and ((i != x and x != y and y != i)):
                print(f'{i} + {x} + {y}')
            else:
                print(f'dont have idea, this option not true in this code')