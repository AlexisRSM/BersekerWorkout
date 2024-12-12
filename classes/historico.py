# classe historico
from classes.treino import Treino, TreinoForca, TreinoCardio, TreinoSuperior, TreinoInferior
from classes.exercicio import Exercicio

class Historico:
    def __init__(self):
        self.treinosRealizados = []

    def registrarTreino(self, treino):
        """regista um treino no histórico."""
        self.treinosRealizados.append(treino)

    def visualizarHistorico(self):
        """exibe o histórico de treinos."""
        if not self.treinosRealizados:
            print("nenhum treino no histórico.")
            return

        for treino in self.treinosRealizados:
            print(f"treino: {treino.nome}, data: {treino.data}, dificuldade: {treino.nivelDificuldade}")
            if treino.caloriasQueimadas > 0:
                print(f"  calorias queimadas: {treino.caloriasQueimadas:.2f} kcal")
            for ex in treino.listaExercicios:
                print(f"   - {ex.nomeExercicio}: {ex.series}x{ex.repeticoes} @ {ex.carga}kg")

    def to_dict(self):
        """retorna um dicionário com o histórico."""
        return {
            "treinosRealizados": [
                {
                    "nome": treino.nome,
                    "data": treino.data,
                    "dificuldade": treino.nivelDificuldade,
                    "tipo": (
                        "forca" if isinstance(treino, TreinoForca) else
                        "cardio" if isinstance(treino, TreinoCardio) else
                        "superior" if isinstance(treino, TreinoSuperior) else
                        "inferior" if isinstance(treino, TreinoInferior) else
                        "generico"
                    ),
                    "caloriasQueimadas": treino.caloriasQueimadas,
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
        """cria um histórico a partir de um dicionário."""
        historico = Historico()
        for treino_data in dados.get("treinosRealizados", []):
            tipo = treino_data.get("tipo", "generico")
            listaEx = [
                Exercicio(
                    nomeExercicio=ex["nomeExercicio"],
                    series=ex["series"],
                    repeticoes=ex["repeticoes"],
                    carga=ex["carga"]
                )
                for ex in treino_data["listaExercicios"]
            ]

            if tipo == "forca":
                t = TreinoForca(nome=treino_data["nome"], nivelDificuldade=treino_data["dificuldade"], listaExercicios=listaEx)
            elif tipo == "cardio":
                t = TreinoCardio(nome=treino_data["nome"], nivelDificuldade=treino_data["dificuldade"], listaExercicios=listaEx)
            elif tipo == "superior":
                t = TreinoSuperior(nome=treino_data["nome"], nivelDificuldade=treino_data["dificuldade"], listaExercicios=listaEx)
            elif tipo == "inferior":
                t = TreinoInferior(nome=treino_data["nome"], nivelDificuldade=treino_data["dificuldade"], listaExercicios=listaEx)
            else:
                t = Treino(nome=treino_data["nome"], nivelDificuldade=treino_data["dificuldade"], listaExercicios=listaEx)

            t.data = treino_data["data"]
            t.caloriasQueimadas = treino_data.get("caloriasQueimadas", 0)
            historico.registrarTreino(t)
        return historico
