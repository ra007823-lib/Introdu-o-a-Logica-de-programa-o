#estrutura de repetição

#for i in '1','2',8,2+2,'abobrinha',True,'subi no ônibus',len('obabão'):
#    print(i)
#for i in [1,2,3,4]:
#    print(i)
#a = ['agrião','rúcula','berinjela','abobrinha','couve-flor',3,19,2457]
#for x in a:
#    print(x)
#for y in range(0,6):
#    print(y)
#x = 1
#while x < 10: #enquanto x for menor que 10, faça
#    x = float(input('digite um valor para x: '))
#    print(f'foi digitado {x}. vou continuar rodando')

#senha = 0
#while senha != 1590: 
#    senha = float(input('digite a senha: '))
#    print(f'senha incorreta, tente novamente!')

#password = "tijolinho"
#while input('digite a senha: ') != password:
#    print('senha incorreta!')

#nota = float(input('digite uma nota (0-100): '))
#while nota < 0 or nota > 100:
#    nota = float(input('Nota invalida. Tente novamente: '))
#print(f'A nota válida digitada foi {nota}')

#while True:
#    n = int(input('digite um numero: '))
#    print(f'voce digitou o numero: {n}')
#    if n == 9:
#        print('parabens, agora podemos sair do loop.')
#        break

#x = [] 
#for x in range(1,6):
#    item = input(f'digite o item{x}:')
#    x.append(item)
#x.sort()
#print(x)

#x.invertido=sorted(x, reverse=True)
#print(x.invertido)

#print()
#print('exibição da lista em ordem alfabetica')
#for y in range(len(x)):
#    print(f'item {x+1}: {x[y]}')

comida = ['bacon','lasanha','churrasco']
frutas = ['pera','uva','morango','abacaxi','melão']

for x in comida:
    print(x)
for y in frutas:
    print(y)
for x in sorted(comida):
    for y in sorted(frutas):
        print(x,y)
        contador+=1
print(f'foram indentificados \033[1m{contador}\033[0m combinações.')