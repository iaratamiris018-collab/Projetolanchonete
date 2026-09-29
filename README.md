# 🍔 Projeto Lanchonete

Este projeto é um conteúdo trabalhado no curso de **Técnico em Desenvolvimento de Software**, realizado no **SENAC**.

* **Início do curso:** 2026
* **Finalização do curso:** 2027

---

## ▶️ Como Rodar este Projeto

### 1. Instale o Python

Instale a versão mais recente do **Python** em seu computador.

### 2. Faça o Git Clone

No terminal, execute:

```bash
git clone https://github.com/iaratamiris018-collab/Projetolanchonete.git
```

### 3. Abra o projeto no VS Code

Abra a pasta do projeto no **Explorador de Arquivos do Windows**.

Na barra de endereço:

1. Digite `CMD`
2. Pressione **Enter**
3. No terminal, digite:

```bash
code .
```

4. Pressione **Enter**.

O projeto será aberto no **Visual Studio Code**.

### 4. Execute o projeto

Abra o arquivo:

```text
main.py
```

Depois, clique em **Executar** no VS Code.

---

# 🧩 Entendendo as Classes

Neste projeto, utilizamos **classes e objetos** para representar elementos do sistema da lanchonete.

## Criando um objeto

Um objeto pode representar um elemento do sistema e receber valores para seus atributos.

Exemplo:

```python
novoPedido = Pedido(
    1,
    "14/09/2025",
    "21:10",
    "Iara",
    ["X-Salada", "X-Bacon"],
    "pix")
```

Nesse exemplo, estamos criando um objeto chamado `novoPedido` a partir da classe `Pedido`.

---

## 🔎 Acessando um atributo

Podemos acessar os dados armazenados nos atributos do objeto.

```python
print(novoPedido.numero)

print(novoPedido.status)
```

---

## ✏️ Alterando dados de um atributo

Também podemos alterar o valor de um atributo.

```python
novoPedido.cliente = "Iara Tamires Mendoza"

print(novoPedido.cliente)
```

---

## 🖨️ Imprimindo os dados do pedido

Podemos utilizar um método da classe para mostrar as informações do pedido:

```python
novoPedido.imprimir()
```

---

## 🔄 Atualizando o pedido

Podemos alterar o status do pedido utilizando um método:

```python
novoPedido.atualizar_Pedido("Em preparação")
```

---

# 🔐 Acessando um atributo privado

Quando um atributo é definido como privado, ele não deve ser acessado diretamente de fora da classe.

Por exemplo:

```python
self.__num
```

Nesse caso, o atributo `__num` é privado.

Para acessar esse valor, podemos utilizar um método `get`.

### Método GET

```python
print(novoPedido.getNum())
```

O método `getNum()` permite consultar o valor do atributo privado.

---

# ✏️ Alterando um atributo privado

Para alterar o valor de um atributo privado, podemos utilizar um método `set`.

```python
novoPedido.setNum(2)

print(novoPedido.getNum())
```

Nesse exemplo, o número do pedido é alterado para `2`.

---

# 🍔 Adicionando um item ao pedido

Também podemos utilizar um método para adicionar um novo item:

```python
novoPedido.setItem("X-Calabresa")
```

Depois, podemos utilizar o método `imprimir()` para visualizar as informações atualizadas:

```python
novoPedido.imprimir()
```

---

## 📌 Resumo

Neste projeto foram trabalhados conceitos importantes de **Programação Orientada a Objetos (POO)**, como:

* **Classes**
* **Objetos**
* **Atributos**
* **Métodos**
* **Encapsulamento**
* **Atributos privados**
* **Getters (`get`)**
* **Setters (`set`)**
* **Alteração de dados**
* **Criação e atualização de pedidos**