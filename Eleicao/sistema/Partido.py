class Partido:
    def _init_(self, nome: str, numero: int, cnpj: str):
        self.nome = nome
        self.numero = numero
        self.__cnpj = cnpj
