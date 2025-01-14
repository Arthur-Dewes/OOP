class Votacao:
    total_votos = 0

    @classmethod
    def incrementar_total(cls):
        cls.total_votos += 1
    
    def __init__(self, voto: list):
        self.voto = voto[1:]
        Votacao.incrementar_total()

    def __str__(self):
        return f'{self.voto}'
