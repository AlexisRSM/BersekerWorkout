import unittest
from classes.historico import Historico
from classes.treino import Treino

class TestHistorico(unittest.TestCase):
    def setUp(self):
        self.historico = Historico()

    def test_registrarVisualizarHistorico(self):
        treino = Treino(nome="Treino A")
        self.historico.registrarTreino(treino)
        self.assertIn(treino, self.historico.treinosRealizados)

if __name__ == "__main__":
    unittest.main()
