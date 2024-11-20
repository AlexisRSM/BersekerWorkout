class Treino:
    def __init__(self, data=None, nivelDificuldade="Fácil", nome="Treino Sem Nome"):
        self.data = data  # Data atribuída apenas ao iniciar o treino
        self.nivelDificuldade = nivelDificuldade
        self.nome = nome
        self.listaExercicios = []
        self.iniciado = False
        self.finalizado = False

    def adicionarExercicio(self, exercicio):
        """Adiciona um exercício ao treino."""
        self.listaExercicios.append(exercicio)

    def removerExercicio(self, indice):
        """Remove um exercício pelo índice."""
        if 0 <= indice < len(self.listaExercicios):
            return self.listaExercicios.pop(indice)
        else:
            raise IndexError("Índice inválido para remoção de exercício.")

    def editarNome(self, novoNome):
        """Edita o nome do treino."""
        self.nome = novoNome

    def iniciarTreino(self):
        """Inicia o treino."""
        if not self.iniciado:
            self.iniciado = True
            print(f"Treino '{self.nome}' iniciado.")
        else:
            print(f"Treino '{self.nome}' já está em andamento.")

    def finalizarTreino(self):
        """Finaliza o treino."""
        if self.iniciado and not self.finalizado:
            self.finalizado = True
            print(f"Treino '{self.nome}' finalizado. Total de exercícios: {len(self.listaExercicios)}")
        elif not self.iniciado:
            print(f"Treino '{self.nome}' ainda não foi iniciado.")
        else:
            print(f"Treino '{self.nome}' já foi finalizado.")
