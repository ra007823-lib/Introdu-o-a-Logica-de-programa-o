1)
# TAREFA 1: Substitua a conjunção (AND)
# Regra: E ^ R
if possui_token and ip_conhecido:
print("Acesso Nível 1 Liberado")

R: if not(not possui_token or not ip_conhecido):

# TAREFA 3: Substitua a conjunção complexa
# Regra: E ^ ¬R ≡ ¬(¬E v R)
if sistema_atualizado and not tentativas_excedidas:
print("Acesso Nível 3: Verificação de Integridade")

R:if not (not sistema_atualizado or tentativas_excedidas):

2)
# Status do sistema de vendas
estoque_disponivel = True
cliente_premium = True
frete_gratis = True
if estoque_disponivel and (cliente_premium == frete_gratis):
print("Pedido validado: Prosseguir para pagamento.")
else:
print("Pedido retido: Verifique as condições de frete e estoque.")

R:if not (not estoque_disponivel or (not(not cliente_premium or frete_gratis) or not (not frete_gratis or cliente_premium))):




if (fidelidade == 'sim') and (cupom == 'sim')
if not(not((not fidelidade or True) and (not True or fidelidade)) or not((not cupom or True) and (not True or cupom))
