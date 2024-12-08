import uuid
from classes.historico import Historico
from classes.planoTreino import PlanoTreino

class Utilizador:
    def __init__(self, nome, idade, peso, altura, objetivo, username, password):
        self.id = str(uuid.uuid4())
        self.nome = nome
        self.username = username
        self.password = password
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.objetivo = objetivo
        self.historico = Historico()
        self.planosTreino = []

    def calcularIMC(self):
        return self.peso / (self.altura ** 2)

    def atualizarPerfil(self, idade=None, peso=None, altura=None, objetivo=None):
        if idade is not None: self.idade = idade
        if peso is not None: self.peso = peso
        if altura is not None: self.altura = altura
        if objetivo is not None: self.objetivo = objetivo

    def calcularCaloriasDiarias(self):
        # Cálculo simplificado usando Mifflin-St Jeor (assumindo sexo masculino)
        # BMR = 10*peso + 6.25*(altura*100) - 5*idade + 5
        altura_cm = self.altura * 100
        BMR = 10 * self.peso + 6.25 * altura_cm - 5 * self.idade + 5

        if self.objetivo == "Perder Peso":
            calorias = BMR * 1.2
        elif self.objetivo == "Manter Peso e Tonificar":
            calorias = BMR * 1.5
        elif self.objetivo == "Ganhar Massa Muscular":
            calorias = BMR * 1.8
        else:
            # Caso não tenha objetivo definido corretamente
            calorias = BMR * 1.4

        return calorias
