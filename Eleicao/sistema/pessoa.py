from excecoes import NameError, AgeError, CpfError

class Pessoa:
    """Classe que armeza informações de uma pessoa"""
    
    def __init__(self, name: str, idade: int, cpf: str):
        if not name.isalpha() and len(name) >= 1:
            raise NameError(name)
        if not (18 < idade < 120):
            raise AgeError(idade)
        if not CpfError(cpf).cpf[1]:
            raise CpfError(cpf)
        
        # se tiver raise, o objeto não é criado
        self.name = name
        self.idade = idade
        self.__cpf = cpf
        
    def get_name(self):
        return self.name
    
    def set_name(self, name: str):
        self.name = name

    def get_idade(self):
        return self.idade
    
    def set_idade(self, idade: int):
        self.idade = idade

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf

    @cpf.deleter
    def cpf(self):
        del self.__cpf
