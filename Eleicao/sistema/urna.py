# import votacao

class Urna:

    @staticmethod
    def read_votos(file: str) -> list[list[str]]:
        with open(file, 'r') as f:
            linhas = [linha.strip().split(',') for i, linha in enumerate(f) if 1 <= i]
        return linhas

    def __init__(self, file: str):
        self.votos = Urna.read_votos(file)
    
    # def vencedor():
    #     pass

    def __add__(self, other) -> int:
        if isinstance(other, Urna):
            return len(self) + len(other)
        elif isinstance(other, int):
            return len(self) + other
        else:
            with open('Eleicao/IO/log.txt', 'a') as f:
                f.write(f'TypeError(f"Operação inválida entre {type(other)} e Urna.")\n')
            return 0
    
    def __radd__(self, other) -> int:
        if other == 0:
            return len(self)
        elif isinstance(other, int):
            return len(self) + other
        else:
            with open('Eleicao/IO/log.txt', 'a') as f:
                f.write(f'TypeError(f"Operação inválida entre {type(other)} e Urna.")\n')
            return 0
    
    def __len__(self):
        return len(self.votos)

