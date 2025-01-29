from .excecoes import NotPythonNameError, AgeError, CpfError

class Pessoa:
    """Classe que armazena informações de uma pessoa"""

    def __init__(self, name: str, idade: int, cpf: str):
        self._name = name
        self._idade = idade
        self._cpf = cpf

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if type(value) != str or len(value) <= 1:
            raise NotPythonNameError(value)
        self._name = value

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, value: int):
        if not (18 < value < 120):
            raise AgeError(value)
        self._idade = value

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, value: str):
        if not CpfError(value).cpf[1]:
            raise CpfError(value)
        self._cpf = value
