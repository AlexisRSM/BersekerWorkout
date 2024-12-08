import unittest
from classes.planoTreino import PlanoTreino
from classes.treino import Treino

class TestPlanoTreino(unittest.TestCase):
    def setUp(self):
        self.plano = PlanoTreino(nomePlano="Plano A")

    def test_criarVisualizarPlano(self):
        treino = Treino(nome="Treino 1")
        self.plano.criarPlano(treino)
        self.assertIn("Treino 1", self.plano.visualizarPlano())

    def test_excluirTreino(self):
        treino = Treino(nome="Treino 1")
        self.plano.criarPlano(treino)
        self.plano.excluirTreino(0)
        self.assertEqual(len(self.plano.treinosProgramados), 0)

if __name__ == "__main__":
    unittest.main()
