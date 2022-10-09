#entradas
num1 = int(input("Informe o númnero:"))

#process
d3 = (num1 % 3)
d7 = (num1 % 7)

#saida

if d3==0 and d7==0:
    print("O número",num1,"é divisível por 3.")
    print("O número",num1,"é divisível por 7.")
    