from votacao import Votacao

class Urna:

    @staticmethod
    def ler_urna(file) -> list[list[str]]:
        """Lê o arquivo urna e retorna uma lista com listas de cada linha do arquivo"""
        with open(file, 'r') as f:
            linhas = [linha.strip().split(',') for i, linha in enumerate(f) if 1 <= i]
        return linhas
    
    @staticmethod
    def ler_votos(filepath) -> list[Votacao]:
        """Retorna uma lista de objetos Votacao a partir de um arquivo de votos"""
        votos = Urna.ler_urna(filepath)
        return [Votacao(voto) for voto in votos]
    
    def __init__(self, filepath: str):
        self.votos = Urna.ler_votos(filepath)

    def __add__(self, other) -> int:
        if isinstance(other, Urna):
            return len(self) + len(other)
        elif isinstance(other, int):
            return len(self) + other
        else:
            with open('Eleicao/IO/log.txt', 'a') as f:
                f.write(f'TypeError(f"Operação inválida entre {type(other)} e Urna ao __add__.")\n')
            return 0
    
    def __radd__(self, other) -> int:
        if isinstance(other, int):
            return len(self) + other
        else:
            with open('Eleicao/IO/log.txt', 'a') as f:
                f.write(f'TypeError(f"Operação inválida entre {type(other)} e Urna ao __radd__.")\n')
            return 0
    
    def __len__(self):
        return len(self.votos)
