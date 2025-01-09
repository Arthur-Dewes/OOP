class Eleicao:
    """Classe responsável por ler o arquivo eleitores.txt"""
    
    @staticmethod
    def diff(value: int) -> tuple[int, int, int]:
        total_pessoas = value + 1
        total_candidatos = value + 1 + 209
        total_partidos = value + 1 + 209 + 32
        return total_pessoas, total_candidatos, total_partidos
    
    def __init__(self, qtd_pessoas):
        self.qtd_pessoas, self.qtd_candidatos, self.qtd_partidos = Eleicao.diff(qtd_pessoas)
        
    def __read_indexes(self, filepath, start: int, stop: int) -> list[list[str]]:
        with open(filepath, 'r') as file:
            linhas = [linha.strip().split(',') for i, linha in enumerate(file) if start <= i < stop]
        return linhas
    
    def read_pessoas(self, file) -> list[list[str]]:
        linhas = self.__read_indexes(file, 1, self.qtd_pessoas)
        return linhas

    def read_candidatos(self, file) -> list[list[str]]:
        linhas = self.__read_indexes(file, self.qtd_pessoas + 1, self.qtd_candidatos + 1)
        return linhas

    def read_partidos(self, file) -> list[list[str]]:
        linhas = self.__read_indexes(file, self.qtd_candidatos + 2, self.qtd_partidos + 2)
        return linhas

