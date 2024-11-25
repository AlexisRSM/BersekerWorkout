# classes/utilizador.py

class Utilizador:
    def __init__(self, nome, idade, peso, altura, objetivo):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.objetivo = objetivo
        self.planosTreino = []  # Novo atributo para armazenar planos de treino
        self.historico = Historico()  # Associando o histórico ao utilizador

    def calcularIMC(self):
        """calcula o Índice de massa corporal (IMC)."""
        return self.peso / (self.altura ** 2)

    def atualizarPerfil(self, nome, idade, peso, altura, objetivo):
        """atualiza os dados do perfil do utilizador."""
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.objetivo = objetivo

    def adicionarPlanoTreino(self, planoTreino):
        """adiciona um plano de treino ao utilizador."""
        self.planosTreino.append(planoTreino)

    def removerPlanoTreino(self, indice):
        """remove um plano de treino do utilizador pelo índice."""
        if 0 <= indice < len(self.planosTreino):
            return self.planosTreino.pop(indice)
        else:
            print("Índice inválido.")

    def listarPlanosTreino(self):
        """retorna a lista de planos de treino do utilizador."""
        return self.planosTreino
