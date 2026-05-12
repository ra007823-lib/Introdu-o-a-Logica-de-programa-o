print('combinações')
tintas = ['oleo','latex','acrilica']
pinceis = ['rolo','cerda','esponja']
solventes = ['agua','aguarras','thinner']

contador = 0
for x in tintas:
    for y in pinceis:
        for z in solventes:
            if not (x == 'oleo' and z == 'agua'):
                if (y =='rolo' or not x =='latex'):
                    print(f'{x},{y},{z}')
                    contador +=1
print(f'foram geradas um total de {contador} combinações')
