from classes.treino import Treino

class Historico:
    def __init__(self):
        self.treinosRealizados = []  # Lista de treinos realizados

    def registrarTreino(self, treino):
        self.treinosRealizados.append(treino)

    def visualizarHistorico(self):
        if not self.treinosRealizados:
            print("Nenhum treino no histórico.")
        for treino in self.treinosRealizados:
            print(f"Treino: {treino.nome}, Data: {treino.data}, Dificuldade: {treino.nivelDificuldade}")

    def to_dict(self):
        return {
            "treinosRealizados": [
                {
                    "nome": treino.nome,
                    "data": treino.data,
                    "dificuldade": treino.nivelDificuldade
                }
                for treino in self.treinosRealizados
            ]
        }

    @staticmethod
    def from_dict(dados):
        historico = Historico()
        for treino_data in dados.get("treinosRealizados", []):
            treino = Treino(
                nome=treino_data["nome"],
                data=treino_data["data"],
                nivelDificuldade=treino_data["dificuldade"]
            )
            historico.registrarTreino(treino)
        return historico
