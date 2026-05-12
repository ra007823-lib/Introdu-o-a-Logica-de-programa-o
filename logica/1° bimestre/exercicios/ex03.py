camisas = ['social','verde','regata']
calcas = ['jeans','azul','bermuda']
calcados = ['tenis','sapato']
contador = 0
for a in camisas:
    for b in calcas:
        for c in calcados:
            if (not (a == 'verde' and b == 'azul'))  and (c =='tenis' or a != 'social'):
                print(a,b,c)
                

