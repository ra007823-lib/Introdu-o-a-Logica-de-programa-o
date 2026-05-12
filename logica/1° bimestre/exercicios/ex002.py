grupo1 =[]
grupo2 =[]
grupo3 =[]

qtd1 = int(input('quantos produtos no grupo eletrodomesticos? '))
for i in range(qtd1):
    item = input(f'Digie o nome do {i+1}° item: ')
    grupo1.append(item)

qtd2 = int(input('quantos produtos no grupo comidas? '))
for i in range(qtd2):
    item = input(f'Digie o nome do {i+1}° item: ')
    grupo2.append(item)

qtd3 = int(input('quantos produtos no grupo utilidades? '))
for i in range(qtd3):
    item = input(f'Digie o nome do {i+1}° item: ')
    grupo3.append(item)

print('---Combinações geradas---')
contador = 0


for a in grupo1:
    for b in grupo2:
        for c in grupo3:
            if (a != b) and (b != c) and (a != c):
                print(f' {a} + {b} + {c}')
                contador +=1
print(f'foram um total de {contador} combinações!')
