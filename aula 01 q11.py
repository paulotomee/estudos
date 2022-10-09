#var
peso = float(input("Informe o peso do Peixe"))
excesso = (peso-50)
multa = (excesso*4)

print("Peso informado: ", peso, "kg")
print("Peso excendente: ", excesso, "kg")
print("Valor da multa ser paga: R$", round(multa,2))