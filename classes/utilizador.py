class Utilizador:
    def __init__(self, nome, idade, peso, altura, objetivo):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.objetivo = objetivo

    def calcularIMC(self):
        return self.peso / (self.altura ** 2)

    def atualizarPerfil(self, nome=None, idade=None, peso=None, altura=None, objetivo=None):
        if nome: self.nome = nome
        if idade: self.idade = idade
        if peso: self.peso = peso
        if altura: self.altura = altura
        if objetivo: self.objetivo = objetivo
