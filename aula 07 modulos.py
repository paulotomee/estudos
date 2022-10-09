from dataclasses import dataclass
from turtle import clear

estoque = 0
def loop_inicial():
    opcao = 0
    while opcao != 5:
        print(f'=========== Sistema de Estoque ===========')
        print(f'1) Listar estoque \n2) Cadastrar estoque \n3) Realizar Saída Estoque \n4) Realizar Entrada de Estoque \n5) Sair do sistema')
        print(f'Selecione a opção desejada: \n')
        opcao = int(input())
        if opcao == 1:
            print(f'========= Listar Estoque =========')
            listar_estoque()
        elif opcao == 2:
            print(f'========= Cadastrar Estoque =========')
            cadastro_estoque()
        elif opcao == 3:
            print(f'========= Realizar Saída =========')
            saida_estoque()            
        elif opcao == 4:
            print(f'========= Realizar Entrada =========')
            entrada_estoque()
        elif opcao == 5:
            print(f'Saindo do sistema')
        else:
            print('Opção invalida')
        # print(f'Deseja retornar ao Menu? \n1 - Sim 2 - Não')
        # retornar_menu = int(input())
        # if retornar_menu == 1:
        #     loop_inicial()
        # elif retornar_menu == 2:
        #     print(f'Saindo do sistema')
        # else:
        #     print(f'Opção invalida')
def saida_estoque():
    global estoque
    quantidade_venda = int(input('Informe a quantidade a ser retirada: \n'))
    if quantidade_venda <= estoque: 
        estoque = estoque - quantidade_venda
        print(f'Saída realizada com sucesso. \n Novo Estoque: {estoque} \n')
    else:
        print(f'Saída indisponível. Estoque insuficiente.\n')
def cadastro_estoque():
    global estoque
    print(f'Informe a nova quantidade de estoque')
    estoque=int(input('Quantidade de Estoque: \n'))
    print(f'Cadastro realizado com sucesso. \n Novo Estoque: {estoque} \n')
def listar_estoque():
    print(f'Temos em estoque {estoque} item(s)\n \n')
def entrada_estoque():
    global estoque
    quantidade_entrada = int(input(f'Informe a quantidade a ser adicionada ao estoque: \n'))
    estoque = estoque + quantidade_entrada    
    print(f'Entrada realizada com sucesso. \n Novo Estoque: {estoque}\n')

loop_inicial()