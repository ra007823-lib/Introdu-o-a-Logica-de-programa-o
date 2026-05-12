f = []
b = []

for i in range(2):
    f.append(input(f'insuras {i+1} frutas: '))
for i in range(2):
    b.append(input(f'insira {i+1} bebidas: '))
for y in f:
    for z in b:
        if not (y == 'manga' and z =='leite'):
            print(f'combinção {z} e {y}')
        else:
            print(f'erro! pois {z} e {y}')