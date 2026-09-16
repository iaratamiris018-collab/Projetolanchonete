class Pedido:
    #não defini os atributos
    status="Recebido"
        #metodo construtor - instanciar recebe o valor do objeto
    def __init__(self, numero, data, hora, cliente, items, pagamento):
        #selft é chamar os atributos;
        self .numero=numero#private - não pode ser acessado nem alterado fora daqui
        self .data=data#publico - pode acessado e alterado por outras classes
        self .hora=hora
        self .cliente=cliente
        self .items=items
        self .pagamento=pagamento
       #metodo - Ação
    def atualizar_Pedido(self, status):
        self .items=status

    def imprimir(self):
        print(f"\n-------- Pedido nº {self.numero} ------"
              f"\n|Data: {self.data} - Horarios: {self.hora} |"
              f"\n|cliente: {self.cliente} "
              f"\n|Item: {self.items} |"
              f"\n|Pagamento: {self.pagamento} ")

        #encapsulamento
        def setNum(self, numero):#setando-alterando indiretamente pois num e private
            self.__numero=numero

        def getNum(self): #acessar a informação variavel private
            return self.__numero

        def setItem(self, items): #controla as informações
            self.__itens.append(items)


                      
    
        



