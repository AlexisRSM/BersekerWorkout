# Aléxis Ralfe da Silva Mendes 25/11/24
from classes.utilizador import Utilizador
from classes.treino import Treino
from classes.exercicio import Exercicio
from classes.planoTreino import PlanoTreino
from classes.historico import Historico
from classes.sistema import Sistema
from datetime import datetime

# Lista de exercícios predefinidos
EXERCICIOS_PREDEFINIDOS = [
    {"nome": "Agachamento", "series": 3, "repeticoes": 12, "carga": 20},
    {"nome": "Supino", "series": 3, "repeticoes": 10, "carga": 30},
    {"nome": "Remada Curvada", "series": 3, "repeticoes": 12, "carga": 25},
    {"nome": "Leg Press", "series": 3, "repeticoes": 12, "carga": 50},
    {"nome": "Flexão de Braços", "series": 3, "repeticoes": 15, "carga": 0},
    {"nome": "Abdominal", "series": 3, "repeticoes": 20, "carga": 0},
    {"nome": "Bíceps com Halteres", "series": 3, "repeticoes": 12, "carga": 15},
    {"nome": "Tríceps no Banco", "series": 3, "repeticoes": 15, "carga": 10},
    {"nome": "Panturrilha no Leg Press", "series": 3, "repeticoes": 15, "carga": 40},
    {"nome": "Prancha", "series": 3, "repeticoes": 1, "carga": 0},
]

# Função para validar datas
def validarData(data):
    """Valida se a data é válida e no formato AAAA-MM-DD."""
    try:
        datetime.strptime(data, "%Y-%m-%d")
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    print("Bem-vindo à Berserker Workout!")
    sistema = Sistema()

    while True:
        print("\n=== Menu Principal ===")
        print("1. Criar Novo Utilizador")
        print("2. Login")
        print("3. Visualizar Utilizadores Existentes")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            sistema.criar_utilizador()

        elif opcao == "2":
            sistema.login_utilizador()
            while sistema.utilizador_atual:
                sistema.menu_utilizador()

        elif opcao == "3":
            sistema.visualizar_utilizadores()

        elif opcao == "4":
            print("Saindo... Obrigado por usar a Berserker Workout!")
            sistema.salvar_utilizadores()
            break

        else:
            print("Opção inválida. Tente novamente.")
