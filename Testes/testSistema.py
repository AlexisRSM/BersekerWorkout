import unittest
from classes.sistema import Sistema
from classes.utilizador import Utilizador

class TestSistema(unittest.TestCase):
    def setUp(self):
        self.sistema = Sistema()
        self.sistema.utilizadores = {}

    def test_criarUtilizador(self):
        self.sistema.utilizadores = {}
        nome = "Teste"
        idade = 25
        peso = 70.0
        altura = 1.75
        objetivo = "Ganhar Massa"
        novo_utilizador = Utilizador(nome, idade, peso, altura, objetivo)
        self.sistema.utilizadores[novo_utilizador.id] = novo_utilizador
        self.assertEqual(len(self.sistema.utilizadores), 1)

    def test_visualizarUtilizadores(self):
        self.sistema.utilizadores["1"] = Utilizador("João", 25, 70.0, 1.75, "Ganhar Massa")
        self.sistema.utilizadores["2"] = Utilizador("Maria", 30, 60.0, 1.65, "Perder Peso")
        self.assertEqual(len(self.sistema.utilizadores), 2)

if __name__ == "__main__":
    unittest.main()
