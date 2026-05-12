f = []
b = []

for i in range(2):
    f.append(input(f'insuras a {i+1} frutas: '))
for i in range(2):
    b.append(input(f'insira a {i+1} bebidas: '))
for frutas in f:
    for bebidas in b:
        if not (frutas == 'manga' and bebidas =='leite'):
            print(f'combinção {frutas} e {bebidas}')
        else:
            print(f'erro! pois {frutas} e {bebidas} não é aceito!!!!!')