comidas = ['pizzas','churrasco','sorvetes','bacon','hotdog','alface']
print(comidas)

len(comidas)#conta o tamnanho da lista
print(len(comidas))#imprime o resultado do comando que conta o tamnho da lista

tamanho_da_lista=len(comidas)# jogou o tamanho para uma vairavel
print(tamanho_da_lista)#imprime a varial com o tamanho

print(comidas[0])#imprime o primeiro elemeto da lista
print(comidas[2])#imprime o 3° elemeto da 

print(f'o ultimo elemento é "{comidas[-1]}"')
print(f"o ultimo elemento é '{comidas[-1]}'")

texto = "okokokok"
print(f'O tamanho de {texto} é {len(texto)}')

#gerando uma lista

range(10)#cria um objeto referente a esta "faixa" de dados
list(range(10))# gera uma lista com base na "faixa" definida
print(list(range(10)))#imprime o range com uma lista

print(list(range(2,10))) #gerou lista de '2' até valor antes de '10'

print(list(range(20,30)))
print(list(range(20,30,2)))

print(f'cmoida = {comidas}')
comidas.reverse() #inverte a lista
print(f'comidas = {comidas}')

# adiciona elementos na lista

comidas.append('lasanha') #add ao final da lista
print(f'comidas = {comidas}')

comidas.insert(0,'feijoada')#add ao inicio da lista
print(f'comidas = {comidas}')