valor = float(input('digite o valor da compra: '))
fidelidade = input('é fidelidade(s/n): ').lower() == 's'
cupom = input('possui cupom(s/n): ').lower() == 's'

if valor > 100: 
    print(f'o valor da compra é de R${valor:.2f}')
    if not(not((not fidelidade or True) and (not True or fidelidade)) or not((not cupom or True) and (not True or cupom))):
        desc = (valor * 0.2)
        pagar = valor - desc
        print(f'você obteve um desconto de 20%, valor do desconto sera de: R${desc:.2f}')
        print(f'o valor com o desconto aplicado sera de: R${pagar:.2f}')
    else:
        desc = (valor *0.05)
        pagar = valor - desc
        print(f'você obteve um desconto de 5%, valor do desconto sera de: R${desc:.2f}')
        print(f'o valor com o desconto aplicado sera de: R${pagar:.2f}')
else:
    print(f'o valor sera de: R${valor:.2f}, pois sua compra foi abaixo de R$100,00')