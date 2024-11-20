class Historico:
    def __init__(self):
        self.treinosRealizados = []

    def registrarTreino(self, treino):
        self.treinosRealizados.append(treino)

    def visualizarHistorico(self):
        for treino in self.treinosRealizados:
            print(f"Treino realizado em {treino.data} - Nível: {treino.nivelDificuldade}")
            print("Exercícios:")
            for exercicio in treino.listaExercicios:
                print(f"  - {exercicio.nomeExercicio}: {exercicio.series} séries, {exercicio.repeticoes} repetições, {exercicio.carga} kg")
