class PlanoTreino:
    def __init__(self, nomePlano, periodo):
        self.nomePlano = nomePlano
        self.treinosProgramados = []
        self.periodo = periodo

    def criarPlano(self, treino):
        self.treinosProgramados.append(treino)

    def visualizarPlano(self):
        return [treino.data for treino in self.treinosProgramados]
