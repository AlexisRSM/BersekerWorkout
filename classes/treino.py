class Treino:
    def __init__(self, data=None, nivelDificuldade="Intermédio", nome="Treino Padrão"):
        self.data = data
        self.nivelDificuldade = nivelDificuldade
        self.nome = nome
        self.listaExercicios = []
        self.iniciado = False
        self.finalizado = False

    def adicionarExercicio(self, exercicio):
        self.listaExercicios.append(exercicio)

    def removerExercicio(self, indice):
        if 0 <= indice < len(self.listaExercicios):
            return self.listaExercicios.pop(indice)
        else:
            print("Índice inválido.")

    def editarNome(self, novoNome):
        self.nome = novoNome

    def iniciarTreino(self):
        self.iniciado = True
        print(f"Treino '{self.nome}' iniciado.")

    def finalizarTreino(self):
        if self.iniciado:
            self.finalizado = True
            print(f"Treino '{self.nome}' finalizado.")
        else:
            print("O treino ainda não foi iniciado.")
