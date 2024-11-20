class Treino:
    def __init__(self, data, nivelDificuldade):
        self.data = data
        self.listaExercicios = []
        self.nivelDificuldade = nivelDificuldade

    def adicionarExercicio(self, exercicio):
        self.listaExercicios.append(exercicio)

    def iniciarTreino(self):
        print(f"Treino de {self.data} iniciado.")

    def finalizarTreino(self):
        print(f"Treino de {self.data} finalizado. Total de exercícios: {len(self.listaExercicios)}")
