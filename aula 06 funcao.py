# print('Ola Mundo!')
# print('Bom dia!')
# print('Ola Mundo!')
# print('Boa tarde!')
# print('Ola Mundo!')


# def ola_mundo():
#     print('Ola mundos!')


# ola_mundo()

# print('Ola Mundo!')
# print('Bom dia!')
# print('Ola Mundo!')
# print('Boa tarde!')

#recebe numero n e imprime se é positivo ou negativo

# def verificarNumero(numero):
#     if numero > 0:
#         print("Positivo")
#     elif numero == 0:
#         pass
#     else:
#         print("Negativo")

# verificarNumero(int(input('Informe o numero: ')))

# se o parametro da funcao for divisel por 3, retorne fizz. 
# se o parametro for divisivel por 5, retorne buzz
# se for divisivel por 3 e 5, retorne fizz buzz,
# caso nao, retorne Numero enviado

# def fizzBuzz(n):
#     if (n%3 == 0) and (n%5 == 0):
#         print(f'FizzBuzz')
#     elif (n%5 == 0):
#         print(f'Buzz')
#     elif (n%3 == 0):
#         print(f'Fizz')
#     else:
#         print(n)


# for numeros in range(1,31):
#     fizzBuzz(numeros)

# fizzBuzz(int(input('Informe o numero: ')))

# n1 recebe 0
# n2 recebe 1
# 1,1,2,3,5,8,13,21,34

# def fibonacci(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fibonacci(n-2) + fibonacci(n-1)

# print(fibonacci(8))

# def piramide(n):
#     for i in range(n+1)
#         for j in range(n+1)
#             print(n)
#         print()



def somaImposto(taxaImposto,custo):
    print(f'{taxaImposto}%')
    print(custo)

somaImposto(float(input('Informe a Taxa de Imposto: ')),float(input(('Informe o Valor do Produto: '))))    

