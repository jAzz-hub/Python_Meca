class Cliente:
    def __init__(self, nome="", endereco="", telefone=""):
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone
        self.pedidos = list()
        
    def ver_pedidos(self):
        print(f"{len(self.pedidos)} foram realizados, sendo eles:")
        for v,i in enumerate(self.pedidos):
            print("Número: ",v.numero)
            print("Descrição: ",v.descricao)
            print("Total: R$",v.total)
            