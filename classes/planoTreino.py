# classe planoTreino

class PlanoTreino:
    def __init__(self, nomePlano="Plano Padrão", periodo="Indefinido"):
        self.nomePlano = nomePlano
        self.treinosProgramados = []
        self.periodo = periodo

    def criarPlano(self, treino):
        """adiciona um treino ao plano."""
        self.treinosProgramados.append(treino)

    def visualizarPlano(self):
        """retorna os nomes dos treinos programados."""
        return [treino.nome for treino in self.treinosProgramados]

    def editarTreino(self, indice, novoNome):
        """edita o nome de um treino no plano."""
        if 0 <= indice < len(self.treinosProgramados):
            self.treinosProgramados[indice].editarNome(novoNome)
            print(f"Treino atualizado para: {novoNome}")
        else:
            print("Erro: Índice do treino inválido.")

    def excluirTreino(self, indice):
        """exclui um treino do plano."""
        if 0 <= indice < len(self.treinosProgramados):
            treinoRemovido = self.treinosProgramados.pop(indice)
            print(f"Treino '{treinoRemovido.nome}' excluído com sucesso.")
        else:
            print("Erro: Índice do treino inválido.")
