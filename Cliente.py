##Construir + atributos
class cliente:
    def __init__(self, nome, cpf, email, nascimento, endereco,tel):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.nascimento = nascimento
        self.endereco = endereco
        self.tel = tel

  ##Encapsulamento (analisar se precisa)
    def getTelefone(self):
        return self.__telefone

    def setTelefone(self, tel):
        self.__telefone=tel

    def imprimeFicha(self):
        print("--------- Ficha do Cliente ---------"
              f"\n|Nome Completo: {self.nome}"
              f"\n|cpf: {self.cpf}"
              f"\n|email: {self.email}"
              f"\n|Data de nascimento: {self.nascimento}"
              f"\n|Endereço: {self.endereco}"
              f"\n|Telefone: {self.tel}"
              f"\n------------------------------------")