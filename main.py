import os
from Pedido import Pedido
from Cliente import cliente 
from Produto import Produto
from Itempedido import ItemPedido
from Itempedido import ItemPedido

os.system("cls")

#Cdastrar cliente
novoCli = cliente(nome="João Paulo",cpf="123.456.789-00",
                  email="joao@gmail.com", endereco="Rua das Flores, 123", tel="(11) 99999-9999", nascimento="15/06/1990")

#Cadastrar produto
siri = Produto(cod=1, desc="Siri", categoria="Lanche", preco=25.00)
refri = Produto(cod=2, desc="Tubaina", categoria="Bebida", preco=6.00)

novoCli.imprimeFicha()
siri.imprimeProduto()
refri.imprimeProduto()

#Pedidos
item1 = ItemPedido(produto=siri, obs="Sem picles", quantidade=2, desconto=5.00)
item2= ItemPedido(produto=refri, obs="Gelo", quantidade=3, desconto=0.00)

itens = [item1, item2]

pedido=Pedido(num=1, data="01/01/2024", hora="12:00", cliente=novoCli, itens=itens, pag="Cartão")
pedido.imprimePedido()