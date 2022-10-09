#entradas
num1 = int(input("Informe o primeiro valor:"))
num2 = int(input("Informe o segundo valor:"))

#processamento
soma = (num1+num2)

#saidas
if soma>20:
    soma = (soma+8)
    print("O total somado a 8 é:", soma)
if soma<=20:
    soma= (soma-5)
    print("O total subtraido 5 é:", soma)
