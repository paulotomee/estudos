#dados_aluno = {
#    'nome': 'Teles',
#    'endereco': 'Rua abc',
#    'telefone': '71 9899999',
#    'idade': '18'}, {
#    'nome': 'Icaro',
#    'endereco': 'Rua cba',
#    'telefone': '71 9998281',
#    'idade': '25' 
#    }

#dados_aluno ={}

# dados_aluno['nome'] = input('Informe o nome: ')
# dados_aluno['endereco'] = input('Informe o endereço: ')
# dados_aluno['telefone'] = input('Informe o telefone: ')
# dados_aluno['idade'] = input('Informe o idade: ')

#print(dados_aluno)

vogais = {
    'a': 0,
    'e': 0,
    'i': 0,
    'o': 0,
    'u': 0
}

texto = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Dignissim cras tincidunt lobortis feugiat vivamus at augue eget arcu. 
Euismod nisi porta lorem mollis aliquam ut. Eget lorem dolor sed viverra ipsum. 
Duis at consectetur lorem donec massa sapien faucibus et. 
Sit amet nisl purus in mollis nunc sed id. Cras semper auctor neque vitae tempus quam. 
Praesent elementum facilisis leo vel fringilla est ullamcorper eget nulla. 
Tellus id interdum velit laoreet id donec ultrices tincidunt arcu. 
Auctor augue mauris augue neque gravida in fermentum et sollicitudin.
 Tellus cras adipiscing enim eu turpis egestas.'''


for lista in texto.lower():
    if lista in vogais.keys():
        vogais[lista] += 1


# for lista in texto:
#     if lista == 'a':
#         vogais["a"] += 1
#     elif lista == 'e':
#         vogais["e"] += 1
#     elif lista == 'i':
#         vogais["i"] += 1
#     elif lista == 'o':
#         vogais["o"] += 1
#     elif lista == 'u':
#         vogais["u"] += 1   

print(vogais)
