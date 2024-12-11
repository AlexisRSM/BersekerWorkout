# planoTreino.py - Classe PlanoTreino
from classes.treino import Treino

class PlanoTreino:
    """planoTreino.py - Classe PlanoTreino"""
    def __init__(self, nomePlano="Plano Padrão", periodo="Indefinido", treinosProgramados=None):
        self.nomePlano = nomePlano
        self.periodo = periodo
        self.treinosProgramados = treinosProgramados if treinosProgramados is not None else []

    def criarPlano(self, treino):
        self.treinosProgramados.append(treino)

    def visualizarPlano(self):
        return [treino.nome for treino in self.treinosProgramados]

    def editarTreino(self, indice, novoNome):
        if 0 <= indice < len(self.treinosProgramados):
            self.treinosProgramados[indice].editarNome(novoNome)
            print(f"Treino atualizado para: {novoNome}")
        else:
            print("Índice inválido.")

    def excluirTreino(self, indice):
        if 0 <= indice < len(self.treinosProgramados):
            treinoRemovido = self.treinosProgramados.pop(indice)
            print(f"Treino '{treinoRemovido.nome}' excluído.")
        else:
            print("Índice inválido.")
