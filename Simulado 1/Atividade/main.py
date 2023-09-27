from utils.functions import Menu, processar_escolha

Clientes = list()
Pedidos = list()
escolha = 1

while(escolha<7 and escolha>0):
    escolha = Menu()
    escolha = processar_escolha(escolha, Clientes, Pedidos)