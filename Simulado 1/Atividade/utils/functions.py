
from Cliente import Cliente
from Pedido import Pedido
from os import system
import platform

def listar_clientes(clientes):
    for i in clientes:
        print(f"\n Nome: {i.nome}")
        print(f"\n Cel: {i.telefone}")
        print(f"\n Endereço: {i.endereco}")
        print(f"\n\n")

def cadastrar_cliente(cliente, cadastrados):
    
    #Se a lista estiver vazia:
    if len(cadastros) == 0:
        cadastros.append(cliente)
        print("\n\n")
        print(f"\t {cliente.nome} foi cadastrado(a) com sucesso! \(°u°)/ ")
        print("\n\n")
    
    #Se a lista não estiver vazia:
    else:
        for i in cadastros:
            if (cliente.nome == i.nome) and (cliente.telefone == i.telefone) and (cliente.endereco == i.endereco):
                print(f"{cliente.nome} já foi cadastrado(a) ←~(°>°)~")
            else:
                cadastros.append(cliente)
                print(f"O Cadastro de {cliente.nome} foi efetuado com sucesso! \(°u°)/")


def verificar_telefone_em_clientes(telefone, clientes):
    for i in clientes:
        if i.telefone == telefone:
            return True
        else:
            return False

def cadastrar_pedido_em_cliente(pedido, clientes, telefone):
    for cliente in clientes:
        if telefone == cliente.telefone:
            cliente.pedidos.append(pedido)
            print(f"{cliente.nome} Seu pedido foi cadastrado \ (•◡•) /")



def Menu():
    print('\033[33m'+"đ°đ°đ°đ°đ°đ°đ°đ°"+'\033[0;0m'+'\033'+"[31m"+"LANCHONETE"+'\033[0;0m'+'\033[33m'+"°ħ°ħ°ħ°ħ°ħ°ħ°ħ"+'\033[0;0m')
    print("Pressione um número seguido da tecla (Enter ←) para solicitar um comando ao sistema:")
    print("1 - Cadastrar um cliente")
    print("2 - Cadastrar um pedido")
    print("3 - Listar Pedidos de um cliente dado seu número de telefone")
    print("4 - Listar todos os clientes cadastrados")
    print("5 - Mostrar todos os pedidos mostrando seus detalhes")
    print("6 - Mostrar todos os pedidos mostrando seus detalhes")
    print("\033[31m"+"Qualquer outro número - Sair"+'\033[0;0m')

    resposta = int(input("Digite aqui: "))

    return resposta




def processar_escolha(escolha=0, clientes=[], pedidos=[]):
    if escolha == 1:    
        #Cadastrar cliente

        print("Cadastrando um Cliente:")
        nome = input("\n Por favor digite o Nome:")
        endereco = input("Digite o Endereço:")
        telefone = input("Digite o Telefone:")

        cadastrar_cliente(Cliente(nome, endereco, telefone), clientes)
        return 1
        

    elif escolha == 2:    
        if len(clientes) != 0:
            print("Cadastrando um Pedido:")
            telefone = input("\n Qual telefone do clientes que está realizando o pedido? ")
        
            #Verificando se cliente existe:
            if verificar_telefone_em_clientes(telefone, clientes):        
                #Adicionando cliente na lista:
                numero = input("\n digite o numero: ")
                descricao = input("Digite a descrição: ")
                total = input("Digite o total: ")

                pedidos.append(Pedido(numero, descricao, total))
                cadastrar_pedido_em_cliente(Pedido(numero, descricao, total), clientes, telefone)
            else:
                print("Desculpe o telefone inserido não existe! ¯\_(ツ)_/¯")
        
        else:
            print("Não podemos cadastrar pedidos por que nenhum cliente foi cadastrado ainda")
                
        return 2
        

    elif escolha == 3:
        tel = input("Insira aqui um número de telefone:")
        print(f"Mostrando pedidos pelo número do telefone {tel}:")
        mostrar_pedidos_do_telefone(telefone, clientes)
        return 3
        
    elif escolha == 4:
        print("Mostrando todos os clientes:")
        listar_clientes(clientes)
        return 4
        
    elif escolha == 5:
        print("Mostrando todos os pedidos:")
        return 5
        
    elif escolha == 6:
        print("Mostrando todos os pedidos:")    
        return 6
    
    else:
        exit()