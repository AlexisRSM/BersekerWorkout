# classe planoTreino
from classes.treino import Treino

class PlanoTreino:
    def __init__(self, nomePlano="Plano Padrão", periodo="Indefinido", treinosProgramados=None):
        self.nomePlano = nomePlano
        self.periodo = periodo
        self.treinosProgramados = treinosProgramados if treinosProgramados is not None else []

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
            print(f"treino atualizado para: {novoNome}")
        else:
            print("erro: índice do treino inválido.")

    def excluirTreino(self, indice):
        """exclui um treino do plano."""
        if 0 <= indice < len(self.treinosProgramados):
            treinoRemovido = self.treinosProgramados.pop(indice)
            print(f"treino '{treinoRemovido.nome}' excluído com sucesso.")
        else:
            print("erro: índice do treino inválido.")
