import unittest
from classes.treino import Treino
from classes.exercicio import Exercicio

class TestTreino(unittest.TestCase):
    def setUp(self):
        self.treino = Treino(nome="Treino A")

    def test_adicionarExercicio(self):
        exercicio = Exercicio("Agachamento", 3, 12, 20)
        self.treino.adicionarExercicio(exercicio)
        self.assertEqual(len(self.treino.listaExercicios), 1)

    def test_removerExercicio(self):
        exercicio = Exercicio("Supino", 3, 10, 30)
        self.treino.adicionarExercicio(exercicio)
        self.treino.removerExercicio(0)
        self.assertEqual(len(self.treino.listaExercicios), 0)

    def test_iniciarFinalizarTreino(self):
        self.treino.iniciarTreino()
        self.assertTrue(self.treino.iniciado)

        self.treino.finalizarTreino()
        self.assertTrue(self.treino.finalizado)

if __name__ == "__main__":
    unittest.main()
