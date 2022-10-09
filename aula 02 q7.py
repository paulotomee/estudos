print("COTADOR DE PLANO DE SAÚDE")

#entradas
nomeCliente = input("Cliente, informe seu nome.")
idadeCliente = int(input("Agora informe a sua idade"))
valorPlano = float(0)

#processamento
if idadeCliente<=10:
    valorPlano = 30
elif idadeCliente > 10 and idadeCliente <= 29:
    valorPlano = 60
elif idadeCliente > 29 and idadeCliente <=45:
    valorPlano = 120
elif idadeCliente > 45 and idadeCliente <=59:
    valorPlano = 150
elif idadeCliente > 59 and idadeCliente <=65:
    valorPlano = 250
elif idadeCliente > 65:
    valorPlano = 400
    
#saidas
print("Nome do Cliente:", nomeCliente)
print("Valor do plano: R$", valorPlano)