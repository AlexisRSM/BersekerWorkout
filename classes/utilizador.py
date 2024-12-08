import uuid
from classes.historico import Historico

class Utilizador:
    def __init__(self, nome, idade, peso, altura, objetivo, username, password):
        self.id = str(uuid.uuid4())  # ID único
        self.nome = nome
        self.username = username  # Novo atributo para login
        self.password = password  # Novo atributo para autenticação
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.objetivo = objetivo
        self.historico = Historico()  # Histórico associado ao utilizador

    def calcularIMC(self):
        return self.peso / (self.altura ** 2)

    def atualizarPerfil(self, nome=None, idade=None, peso=None, altura=None, objetivo=None):
        if nome: self.nome = nome
        if idade: self.idade = idade
        if peso: self.peso = peso
        if altura: self.altura = altura
        if objetivo: self.objetivo = objetivo
