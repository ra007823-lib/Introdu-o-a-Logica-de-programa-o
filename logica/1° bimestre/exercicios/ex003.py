camisas = ['social','verde','regata']
calcas = ['jeans','azul','bermuda']
calcados = ['tenis','sapato']
contador = 0
for a in camisas:
    for b in calcas:
        for c in calcados:
            regra1 = not(a == 'verde' and b =='azul')
            regra2 = (c =='tenis') or (c !='social')


            if regra1 and regra2:
                print(f' sugestoes: {a}, {b} e {c}')


