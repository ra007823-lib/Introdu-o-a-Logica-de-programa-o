proteinas = ['ovo','peixe','frango']
carboidratos = ['arroz','macarrão','batata doce']
saladas = ['espinafre','alface','brocolis']

for i in proteinas:
    for x in carboidratos:
        for y in saladas:
            if (not(i == 'peixe' and x == 'batata doce')):
                if(not(i != 'ovo' and y =='espinafre')):
                    print(i,'+',x,'+',y)
                else:
                    print(f'{i} + {x} + {y}, prato indisponivel!')