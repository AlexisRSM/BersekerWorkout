# classe treino
from classes.exercicio import Exercicio

class Treino:
    def __init__(self, data=None, nivelDificuldade="Intermédio", nome="Treino Padrão", listaExercicios=None):
        self.data = data
        self.nivelDificuldade = nivelDificuldade
        self.nome = nome
        self.listaExercicios = listaExercicios if listaExercicios is not None else []
        self.iniciado = False
        self.finalizado = False
        self.caloriasQueimadas = 0

    def adicionarExercicio(self, exercicio):
        """adiciona um exercício ao treino."""
        self.listaExercicios.append(exercicio)

    def removerExercicio(self, indice):
        """remove um exercício do treino pelo índice."""
        if 0 <= indice < len(self.listaExercicios):
            return self.listaExercicios.pop(indice)
        else:
            print("índice inválido.")

    def editarNome(self, novoNome):
        """edita o nome do treino."""
        self.nome = novoNome

    def iniciarTreino(self):
        """marca o treino como iniciado."""
        self.iniciado = True
        print(f"treino '{self.nome}' iniciado.")

    def finalizarTreino(self):
        """marca o treino como finalizado."""
        if self.iniciado:
            self.finalizado = True
            print(f"treino '{self.nome}' finalizado.")
        else:
            print("o treino ainda não foi iniciado.")

    def calcularCaloriasQueimadas(self, peso, duracao_min):
        """calcula as calorias queimadas no treino (genérico)."""
        if not self.listaExercicios or duracao_min <= 0:
            return 0
        base = len(self.listaExercicios) * (peso * 0.05)
        return base * (duracao_min / 30.0)

# classe treinoForca
class TreinoForca(Treino):
    def calcularCaloriasQueimadas(self, peso, duracao_min):
        """calcula as calorias para um treino de força."""
        if not self.listaExercicios or duracao_min <= 0:
            return 0
        soma_total = sum(ex.carga * ex.series * ex.repeticoes for ex in self.listaExercicios)
        return soma_total * 0.005 * (duracao_min / 30.0) * (peso / 70.0)

# classe treinoCardio
class TreinoCardio(Treino):
    def __init__(self, data=None, nivelDificuldade="Fácil", nome="Treino Cardio", listaExercicios=None):
        super().__init__(data, nivelDificuldade, nome, listaExercicios)

    def calcularCaloriasQueimadas(self, peso, duracao_min):
        """calcula as calorias para um treino de cardio."""
        if duracao_min <= 0:
            return 0
        return duracao_min * peso * 0.1

# classe treinoSuperior
class TreinoSuperior(Treino):
    def gruposTrabalhados(self):
        """retorna os grupos musculares trabalhados no treino superior."""
        return ["Peito", "Costas", "Ombros", "Bíceps", "Tríceps"]

    def calcularCaloriasQueimadas(self, peso, duracao_min):
        """calcula as calorias para um treino superior."""
        if not self.listaExercicios or duracao_min <= 0:
            return 0
        return len(self.listaExercicios) * peso * 0.03 * (duracao_min / 20.0)

# classe treinoInferior
class TreinoInferior(Treino):
    def gruposTrabalhados(self):
        """retorna os grupos musculares trabalhados no treino inferior."""
        return ["Pernas", "Glúteos", "Panturrilhas"]

    def calcularCaloriasQueimadas(self, peso, duracao_min):
        """calcula as calorias para um treino inferior."""
        if duracao_min <= 0:
            return 0
        return duracao_min * (peso * 0.08)
