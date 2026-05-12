ingredientes = ['tomate','agriao','filé de frango','pão de queijo', 'mel']
contador = 0
for a in ingredientes:
    for b in ingredientes:
        for c in ingredientes:
            if (a != b) and (b !=c) and (a !=c):

                print('{} com {} e {}'.format(a,b,c))
                contador +=1
print('Forma um total de {} combinações.'.format(contador))