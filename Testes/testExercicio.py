import unittest
from classes.exercicio import Exercicio

class TestExercicio(unittest.TestCase):
    def setUp(self):
        self.exercicio = Exercicio("Supino", 3, 10, 30)

    def test_atributosExercicio(self):
        self.assertEqual(self.exercicio.nomeExercicio, "Supino")
        self.assertEqual(self.exercicio.series, 3)
        self.assertEqual(self.exercicio.repeticoes, 10)
        self.assertEqual(self.exercicio.carga, 30)

if __name__ == "__main__":
    unittest.main()
