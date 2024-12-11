# treino.py - Classes Treino e Subclasses
from classes.exercicio import Exercicio

class Treino:
    """treino.py - Classe Treino"""
    def __init__(self, data=None, nivelDificuldade="Intermédio", nome="Treino Padrão", listaExercicios=None):
        self.data = data
        self.nivelDificuldade = nivelDificuldade
        self.nome = nome
        self.listaExercicios = listaExercicios if listaExercicios is not None else []
        self.iniciado = False
        self.finalizado = False
        self.caloriasQueimadas = 0

    def adicionarExercicio(self, exercicio):
        self.listaExercicios.append(exercicio)

    def removerExercicio(self, indice):
        if 0 <= indice < len(self.listaExercicios):
            return self.listaExercicios.pop(indice)
        else:
            print("Índice inválido.")

    def editarNome(self, novoNome):
        self.nome = novoNome

    def iniciarTreino(self):
        self.iniciado = True
        print(f"Treino '{self.nome}' iniciado.")

    def finalizarTreino(self):
        if self.iniciado:
            self.finalizado = True
            print(f"Treino '{self.nome}' finalizado.")
        else:
            print("O treino ainda não foi iniciado.")

    def calcularCaloriasQueimadas(self, peso, duracao_min):
        # Cálculo genérico
        if not self.listaExercicios or duracao_min <= 0:
            return 0
        base = len(self.listaExercicios) * (peso * 0.05)
        return base * (duracao_min / 30.0)

class TreinoForca(Treino):
    """treino.py - Classe TreinoForca"""
    def calcularCaloriasQueimadas(self, peso, duracao_min):
        if not self.listaExercicios or duracao_min <= 0:
            return 0
        soma_total = sum(ex.carga * ex.series * ex.repeticoes for ex in self.listaExercicios)
        return soma_total * 0.005 * (duracao_min / 30.0) * (peso / 70.0)

class TreinoCardio(Treino):
    """treino.py - Classe TreinoCardio"""
    def __init__(self, data=None, nivelDificuldade="Fácil", nome="Treino Cardio", listaExercicios=None):
        super().__init__(data, nivelDificuldade, nome, listaExercicios)

    def calcularCaloriasQueimadas(self, peso, duracao_min):
        if duracao_min <= 0:
            return 0
        return duracao_min * peso * 0.1

class TreinoSuperior(Treino):
    """treino.py - Classe TreinoSuperior"""
    def gruposTrabalhados(self):
        return ["Peito", "Costas", "Ombros", "Bíceps", "Tríceps"]

    def calcularCaloriasQueimadas(self, peso, duracao_min):
        if not self.listaExercicios or duracao_min <= 0:
            return 0
        return len(self.listaExercicios) * peso * 0.03 * (duracao_min / 20.0)

class TreinoInferior(Treino):
    """treino.py - Classe TreinoInferior"""
    def gruposTrabalhados(self):
        return ["Pernas", "Glúteos", "Panturrilhas"]

    def calcularCaloriasQueimadas(self, peso, duracao_min):
        if duracao_min <= 0:
            return 0
        return duracao_min * (peso * 0.08)
