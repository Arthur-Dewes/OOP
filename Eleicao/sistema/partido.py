from excecoes import NotPythonNameError, CnpjError

class Partido:
    """Classe que representa um partido político"""
    def __init__(self, name: str, number: int, cnpj: str):
        if not name.isalpha() and len(name) >= 1:
            raise NotPythonNameError(name)
        if not (0 < number < 100):
            raise ValueError("Número do partido inválido")
        if not CnpjError(cnpj).cnpj[1]:
            raise CnpjError(cnpj)
        
        # se tiver raise, o objeto não é criado
        self.name = name
        self.number = number
        self.cnpj = cnpj

    def get_nome(self):
        return self._name

    def get_numero(self):
        return self._number

    def get_cnpj(self):
        return self._cnpj