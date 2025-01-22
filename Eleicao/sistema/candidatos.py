from .pessoa import Pessoa
from abc import ABC, abstractmethod
from excecoes import ProposalError

class Candidatos(ABC, Pessoa):
    """Classe que representa um candidato"""
    
    @abstractmethod
    def verificar_numero_candidato(self):
        pass

    def _init_(self, nome: str, idade: int, cpf: str, numero_voto: int, proposta: str):
        if not isinstance(numero_voto, int) or numero_voto < 10:
            raise ValueError("Número de voto inválido")
        if not isinstance(proposta, str) :
            raise ProposalError(proposta)
        
        # se tiver raise, o objeto não é criado
        Pessoa._init_(self, nome, idade, cpf)
        self.numero_voto = numero_voto
        self.proposta = proposta


class DepFederal(Candidatos):
    def verificar_numero_candidato(self):
        if isinstance(self.numero_voto, int) and len(str(self.numero_voto)) == 4:
            return True # voto válido
        else:
            return False # voto inválido

class DepEstadual(Candidatos):
    def verificar_numero_candidato(self):
        if isinstance(self.numero_voto, int) and len(str(self.numero_voto)) == 5:
            return True # voto válido
        else:
            return False # voto inválido

class Senador(Candidatos):
    def verificar_numero_candidato(self):
        if isinstance(self.numero_voto, int) and len(str(self.numero_voto)) == 3:
            return True # voto válido
        else:
            return False # voto inválido

class Governador(Candidatos):
    def verificar_numero_candidato(self):
        if isinstance(self.numero_voto, int) and len(str(self.numero_voto)) == 2:
            return True # voto válido
        else:
            return False # voto inválido

class Presidente(Candidatos):
    def verificar_numero_candidato(self):
        if isinstance(self.numero_voto, int) and len(str(self.numero_voto)) == 2:
            return True # voto válido
        else:
            return False # voto inválido

__all__ = ['Candidatos', 'DepFederal', 'DepEstadual', 'Senador', 'Governador', 'Presidente']