#classe historico

class Historico:
    def __init__(self):
        self.treinosRealizados = []

    def registrarTreino(self, treino):
        """Regista um treino no histórico."""
        if treino.finalizado:
            self.treinosRealizados.append(treino)
            print(f"Treino '{treino.nome}' registrado no histórico.")
        else:
            print(f"Erro: O treino '{treino.nome}' ainda não foi finalizado.")

    def visualizarHistorico(self):
        """Exibe o histórico de treinos."""
        if not self.treinosRealizados:
            print("Ainda não existem treinos registrados no histórico.")
            return

        for treino in self.treinosRealizados:
            print(f"Treino: {treino.nome}")
            print(f"  Data: {treino.data}")
            print(f"  Nível: {treino.nivelDificuldade}")
            print(f"  Exercícios:")
            for exercicio in treino.listaExercicios:
                print(f"    - {exercicio.nomeExercicio}: {exercicio.series} séries, {exercicio.repeticoes} repetições, {exercicio.carga} kg")
