print(1.5+2.5)

st = "sistemas de informação"
print(st)
print(st[3:8])
print(st[9:11])
print(st[14:22])
print(st[:6])
print(st[:3],st[19:])
print(st[::-1])#inventer a string
print(st[::-1].upper())#imprime invertido maiusculo
print(st[::-1].isupper())#testa se objeto é maiusculo
print(st.upper())
st2 = st[::-1].upper()#criou a variavel st2 com string maiuscula invertida
print(st2)
st3 = st.upper()#criou a variavel st3 com string maiuscula 
print(st3)

valor = 33
print(f'o valor da variavel é {valor}')
print("o valor da variavel é", valor)

print('vamos definir a cor dos times')
cor1 = input('digite a primeira cor: ')
cor2 = input('digite a segunda cor: ')
cor3 = input('digite a terceira cor: ')

if cor1 == cor2:
    print("otima escolha")
elif cor3 == cor1:
    print("otima escolha")
elif cor1 != cor2:
    print("pessima escolha")
elif cor1 != cor3:
    print("pessima escolha")

if(cor1 == cor2 and cor3 == cor1 or cor1 != cor2 and cor1 != cor3):
    print("otima escolha")
else:
    print("pessima escolha")