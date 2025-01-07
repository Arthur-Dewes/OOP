class Pessoa:
    """Classe que armeza informações de uma pessoa"""
    def _init_(self, nome: str, idade: int, cpf: str):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf
        
    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        self.nome = nome

    def get_idade(self):
        return self.idade
    
    def set_idade(self, idade):
        self.idade = idade

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @cpf.deleter
    def cpf(self):
        del self.__cpf

