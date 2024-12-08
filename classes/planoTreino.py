from classes.treino import Treino

class PlanoTreino:
    def __init__(self, nomePlano="Plano Padrão", periodo="Indefinido"):
        self.nomePlano = nomePlano
        self.treinosProgramados = []
        self.periodo = periodo

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
