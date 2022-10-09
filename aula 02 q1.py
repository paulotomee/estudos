#1aQuestao

#entradas
nota1 = float(input("Informe a Nota1:"))
nota2 = float(input("Informe a Nota2:"))
nota3 = float(input("Informe a Nota3:"))
nota4 = float(input("Informe a Nota4:"))

#processamento
media = float((nota1+nota2+nota3+nota4)/4)

#saida
print("Média:", media)

if media>=7:
    print("APROVADO")
else:
    print("REPROVADO")

