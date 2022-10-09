#var
anoNasc = int(input("Informe o ano de Nascimento"))
anoAtual = int(input("Informe o ano atual"))

#processamento
idade = (anoAtual - anoNasc)

#saida
if (anoNasc>0) and (anoAtual>anoNasc):
    print("O usuário tem",idade,"anos de idade.")
else:
    print("Ano de nascimento invalido.")