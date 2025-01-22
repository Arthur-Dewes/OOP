from excecoes import NotPythonNameError, AgeError, CpfError

class Pessoa:
    """Classe que armeza informações de uma pessoa"""
    
    def __init__(self, name: str, idade: int, cpf: str):
        if not name.isalpha() and len(name) >= 1:
            raise NotPythonNameError(name)
        if not (18 < idade < 120):
            raise AgeError(idade)
        if not CpfError(cpf).cpf[1]:
            raise CpfError(cpf)
        
        # se tiver raise, o objeto não é criado
        self.name = name
        self.idade = idade
        self.cpf = cpf
        
    @property
    def name(self):
        return self._name

    @property
    def idade(self):
        return self._idade

    @property
    def cpf(self):
        return self._cpf
