class Votacao:
    total_votos = 0

    @classmethod
    def incrementar_total(cls):  # Total de pessoas que votaram
        cls.total_votos += 1

    def _init_(self, voto):
        self._voto = voto  # Voto por pessoa (talvez usar split-list?)
        # Fazer um dicionário com candidatos como chave e votos como valor
        Votacao.incrementar_total()

    def set_voto(self, voto):
        self._voto = voto

    voto = property(set_voto)
    
    
