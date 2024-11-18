# Classe Utilizador
class Utilizador:
    def __init__(self, nome, idade, peso, altura, objetivo):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.objetivo = objetivo

    def calcular_IMC(self):
        return self.peso / (self.altura ** 2)

    def atualizar_perfil(self, nome=None, idade=None, peso=None, altura=None, objetivo=None):
        if nome: self.nome = nome
        if idade: self.idade = idade
        if peso: self.peso = peso
        if altura: self.altura = altura
        if objetivo: self.objetivo = objetivo

    def visualizar_historico(self, historico):
        return historico.treinos_realizados


# Classe Treino
class Treino:
    def __init__(self, data, nivel_dificuldade):
        self.data = data
        self.lista_exercicios = []
        self.duracao = 0
        self.nivel_dificuldade = nivel_dificuldade

    def adicionar_exercicio(self, exercicio):
        self.lista_exercicios.append(exercicio)

    def iniciar_treino(self):
        print(f"Treino de {self.data} iniciado.")

    def finalizar_treino(self):
        print(f"Treino de {self.data} finalizado. Total de exercícios: {len(self.lista_exercicios)}")


# Classe Exercício
class Exercicio:
    def __init__(self, nome_exercicio, series, repeticoes, carga):
        self.nome_exercicio = nome_exercicio
        self.series = series
        self.repeticoes = repeticoes
        self.carga = carga


# Classe PlanoDeTreino
class PlanoDeTreino:
    def __init__(self, nome_plano, periodo):
        self.nome_plano = nome_plano
        self.treinos_programados = []
        self.periodo = periodo

    def criar_plano(self, treino):
        self.treinos_programados.append(treino)

    def visualizar_plano(self):
        return [treino.data for treino in self.treinos_programados]


# Classe Histórico
class Historico:
    def __init__(self):
        self.treinos_realizados = []

    def registrar_treino(self, treino):
        self.treinos_realizados.append(treino)

#################################-- Main--######################
# Testar o código
if __name__ == "__main__":
    # Criar um utilizador
    utilizador = Utilizador(nome="João", idade=25, peso=75, altura=1.80, objetivo="Ganho de Massa")

    # Calcular o IMC
    print(f"IMC do {utilizador.nome}: {utilizador.calcular_IMC():.2f}")

    # Atualizar perfil do utilizador
    utilizador.atualizar_perfil(nome="João Silva", peso=78)
    print(f"Nome atualizado: {utilizador.nome}, Peso atualizado: {utilizador.peso} kg")

    # Criar exercícios
    exercicio1 = Exercicio(nome_exercicio="Supino", series=3, repeticoes=10, carga=50)
    exercicio2 = Exercicio(nome_exercicio="Agachamento", series=4, repeticoes=12, carga=60)

    # Criar um treino
    treino = Treino(data="2024-11-20", nivel_dificuldade="Intermédio")
    treino.adicionar_exercicio(exercicio1)
    treino.adicionar_exercicio(exercicio2)

    # Iniciar e finalizar treino
    treino.iniciar_treino()
    treino.finalizar_treino()

    # Criar um plano de treino
    plano = PlanoDeTreino(nome_plano="Plano de Hipertrofia", periodo="1 mês")
    plano.criar_plano(treino)
    print(f"Treinos no plano: {plano.visualizar_plano()}")

    # Criar um histórico e registrar treino
    historico = Historico()
    historico.registrar_treino(treino)
    print(f"Histórico de treinos realizados: {[t.data for t in historico.treinos_realizados]}")

    # Visualizar histórico através do utilizador
    print(f"Histórico visualizado pelo utilizador: {[t.data for t in utilizador.visualizar_historico(historico)]}")
