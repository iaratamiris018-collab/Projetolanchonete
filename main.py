from Pedido import Pedido 

#criar um objeto - representar um elemento - dar valores
novoPedido = Pedido(1, "14/09/2025", "21:10", "Iara", ["X-Salada", "X-Bacon"], "pix")

### O que eu posso fazer com o objeto?###
#acessar um atributo
print(novoPedido.numero)
print(novoPedido.status)
#alterar dados de um atributo
novoPedido.cliente="Iara Tamires Mendoza"
print(novoPedido.cliente)

novoPedido.imprimir()
novoPedido.atualizar_Pedido("Em preparação")

#acessar o id - private
#novoPedido:__num2
#print(novoPedido:__num)#acessar
#novoPedido.imprimir()
print(novoPedido.getNum())
novoPedido.setNum(2)
print(novoPedido.getNum())

novoPedido.setItem("X-Calabresa")
novoPedido.imprimir()