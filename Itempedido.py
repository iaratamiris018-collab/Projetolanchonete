class ItemPedido:
    def __init__(self,produto, obs, quantidade, desconto):
        self.produto = produto
        self.obs = obs
        self.quantidade = quantidade
        self.desconto = desconto

    def totalitem(self):
        return (self.quantidade*self.produto.preco)-self.desconto
      