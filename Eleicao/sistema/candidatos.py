from Eleicao.sistema.pessoa import pessoa
from abc import ABC, abstractmethod

class Candidatos(ABC, pessoa):
    @abstractmethod
    def verificar_numero_candidato(self):
        pass

    def _init_(self, nome: str, idade: int, cpf: str, numero_voto: int, proposta: str):
        pessoa._init_(self, nome, idade, cpf)
        self.numero_voto = numero_voto  # talvez privado, ver onde pegar o voto
        self.proposta = proposta

class DepFederal(Candidatos):
    def verificar_numero_candidato(self):
        if isinstance(self.numero_voto, int) and len(str(self.numero_voto)) == 4:
            return "válido"
        else:
            return "inválido"


class DepEstadual(Candidatos):
    def verificar_numero_candidato(self):
        if isinstance(self.numero_voto, int) and len(str(self.numero_voto)) == 5:
            return "válido"
        else:
            return "inválido"


class Senador(Candidatos):
    def verificar_numero_candidato(self):
        if isinstance(self.numero_voto, int) and len(str(self.numero_voto)) == 3:
            return "válido"
        else:
            return "inválido"


class Governador(Candidatos):
    def verificar_numero_candidato(self):
        if isinstance(self.numero_voto, int) and len(str(self.numero_voto)) == 2:
            return "válido"
        else:
            return "inválido"


class Presidente(Candidatos):
    def verificar_numero_candidato(self):
        if isinstance(self.numero_voto, int) and len(str(self.numero_voto)) == 2:
            return "válido"
        else:
            return "inválido"

