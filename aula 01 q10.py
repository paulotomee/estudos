#var

dolar = float(input("Qual a cotação atual do Dolar?"))
real = float(input("Que valor em Real você deseja converter?"))
conversao = real/dolar

print("R$", real, "convertido em dolares é igual a:")
print("$", round(conversao, 2))