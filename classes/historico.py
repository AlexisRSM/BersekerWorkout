from classes.treino import Treino
from classes.exercicio import Exercicio

class Historico:
    def __init__(self):
        self.treinosRealizados = []

    def registrarTreino(self, treino):
        self.treinosRealizados.append(treino)

    def visualizarHistorico(self):
        if not self.treinosRealizados:
            print("Nenhum treino no histórico.")
            return

        for treino in self.treinosRealizados:
            print(f"Treino: {treino.nome}, Data: {treino.data}, Dificuldade: {treino.nivelDificuldade}")
            for ex in treino.listaExercicios:
                print(f"   - {ex.nomeExercicio}: {ex.series}x{ex.repeticoes} @ {ex.carga}kg")

    def to_dict(self):
        return {
            "treinosRealizados": [
                {
                    "nome": treino.nome,
                    "data": treino.data,
                    "dificuldade": treino.nivelDificuldade,
                    "listaExercicios": [
                        {
                            "nomeExercicio": ex.nomeExercicio,
                            "series": ex.series,
                            "repeticoes": ex.repeticoes,
                            "carga": ex.carga
                        }
                        for ex in treino.listaExercicios
                    ]
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
                nivelDificuldade=treino_data["dificuldade"],
                listaExercicios=[
                    Exercicio(
                        nomeExercicio=ex["nomeExercicio"],
                        series=ex["series"],
                        repeticoes=ex["repeticoes"],
                        carga=ex["carga"]
                    )
                    for ex in treino_data["listaExercicios"]
                ]
            )
            historico.registrarTreino(treino)
        return historico
