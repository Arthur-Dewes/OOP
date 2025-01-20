class Partido:
    """Classe que representa um partido político"""
    def _init_(self, nome: str, numero: int, cnpj: str):
        self.nome = nome
        self.numero = numero
        self.__cnpj = cnpj

    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome: str):
        self.nome = nome

    def get_numero(self):
        return self.numero
    
    def set_numero(self, numero: int):
        self.numero = numero

    @property
    def cnpj(self):
        return self.__cnpj
    
    @cnpj.setter
    def cnpj(self, cnpj: str):
        self.__cnpj = cnpj
    
    @cnpj.deleter
    def cnpj(self):
        del self.__cnpj
    