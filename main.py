from classes.utilizador import Utilizador
from classes.treino import Treino
from classes.exercicio import Exercicio
from classes.planoTreino import PlanoTreino
from classes.historico import Historico
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

    # Recolher dados do utilizador
    nome = input("Insira o seu nome: ")
    idade = int(input("Insira a sua idade: "))
    peso = float(input("Insira o seu peso (kg, ex.: 70.5): ").replace(",", "."))
    altura = float(input("Insira a sua altura (m, ex.: 1.75): ").replace(",", "."))
    objetivo = input("Qual é o seu objetivo? (ex.: Perder peso, Ganhar massa): ")

    utilizador = Utilizador(nome=nome, idade=idade, peso=peso, altura=altura, objetivo=objetivo)
    plano = PlanoTreino(nomePlano="Plano Inicial", periodo="1 mês")
    historico = Historico()

    treinoAtual = None

    while True:
        print("\nEscolha uma opção:")
        print("1. Calcular IMC")
        print("2. Mostrar/Editar Dados do Utilizador")
        print("3. Criar Treino")
        if plano.treinosProgramados:
            print("4. Iniciar Treino")
        if treinoAtual:
            print("5. Finalizar Treino Atual")
        print("6. Visualizar Histórico de Treinos")
        print("7. Visualizar/Editar Planos de Treino")
        print("8. Sair")

        opcao = input("Insira a sua opção: ")

        if opcao == "1":
            imc = utilizador.calcularIMC()
            print(f"O seu IMC é: {imc:.2f}")

        elif opcao == "2":
            while True:
                print("\nDados do Utilizador:")
                print(f"Nome: {utilizador.nome}")
                print(f"Idade: {utilizador.idade}")
                print(f"Peso: {utilizador.peso} kg")
                print(f"Altura: {utilizador.altura} m")
                print(f"Objetivo: {utilizador.objetivo}")
                print("\n1. Editar Dados")
                print("2. Voltar ao Menu Principal")

                escolha = input("Escolha uma opção: ")

                if escolha == "1":
                    nome = input("Novo nome (ou Enter para manter): ") or utilizador.nome
                    idade = input("Nova idade (ou Enter para manter): ") or utilizador.idade
                    peso = input("Novo peso (ou Enter para manter): ") or utilizador.peso
                    altura = input("Nova altura (ou Enter para manter): ") or utilizador.altura
                    objetivo = input("Novo objetivo (ou Enter para manter): ") or utilizador.objetivo

                    utilizador.atualizarPerfil(nome, idade, float(peso), float(altura), objetivo)
                    print("Dados atualizados com sucesso!")
                elif escolha == "2":
                    break
                else:
                    print("Opção inválida.")

        elif opcao == "3":
            nomeTreino = input("Nome do treino: ")
            print("\nEscolha a dificuldade:")
            print("1. Fácil")
            print("2. Intermédio")
            print("3. Difícil")

            nivelDificuldade = input("Insira a dificuldade (1, 2 ou 3): ")
            while nivelDificuldade not in ["1", "2", "3"]:
                print("Opção inválida. Escolha 1, 2 ou 3.")
                nivelDificuldade = input("Insira a dificuldade (1, 2 ou 3): ")

            dificuldadeTexto = {"1": "Fácil", "2": "Intermédio", "3": "Difícil"}[nivelDificuldade]

            treino = Treino(data=None, nivelDificuldade=dificuldadeTexto, nome=nomeTreino)

            # Perguntar se deseja adicionar exercícios
            while True:
                adicionar = input("Deseja adicionar exercícios a este treino? (s/n): ").lower()
                if adicionar == "s":
                    print("\nEscolha um exercício da lista ou adicione um personalizado:")
                    for i, ex in enumerate(EXERCICIOS_PREDEFINIDOS):
                        print(f"{i + 1}. {ex['nome']} - {ex['series']} séries, {ex['repeticoes']} repetições, {ex['carga']} kg")
                    print("11. Adicionar Exercício Personalizado")

                    escolha = int(input("Escolha um número: "))
                    if 1 <= escolha <= 10:
                        exercicioEscolhido = EXERCICIOS_PREDEFINIDOS[escolha - 1]
                        exercicio = Exercicio(
                            nomeExercicio=exercicioEscolhido["nome"],
                            series=exercicioEscolhido["series"],
                            repeticoes=exercicioEscolhido["repeticoes"],
                            carga=exercicioEscolhido["carga"],
                        )
                        treino.adicionarExercicio(exercicio)
                        print(f"Exercício '{exercicio.nomeExercicio}' adicionado com sucesso!")
                    elif escolha == 11:
                        nomeExercicio = input("Nome do exercício: ")
                        series = int(input("Número de séries: "))
                        repeticoes = int(input("Número de repetições: "))
                        carga = float(input("Carga utilizada (kg): "))
                        exercicio = Exercicio(nomeExercicio, series, repeticoes, carga)
                        treino.adicionarExercicio(exercicio)
                        print(f"Exercício '{nomeExercicio}' adicionado com sucesso!")
                    else:
                        print("Opção inválida.")
                elif adicionar == "n":
                    break
                else:
                    print("Resposta inválida. Insira 's' ou 'n'.")

            plano.criarPlano(treino)
            print(f"Treino '{nomeTreino}' com dificuldade '{dificuldadeTexto}' criado com sucesso!")

        elif opcao == "4" and plano.treinosProgramados:
            print("Treinos disponíveis:")
            for i, treino in enumerate(plano.treinosProgramados):
                print(f"{i + 1}. {treino.nome} - {treino.nivelDificuldade}")

            escolha = int(input("Escolha o treino para iniciar (número): "))
            treinoAtual = plano.treinosProgramados.pop(escolha - 1)
            treinoAtual.iniciarTreino()

        elif opcao == "5" and treinoAtual:
            while True:
                dataTreino = input("Insira a data do treino (AAAA-MM-DD): ")
                if validarData(dataTreino):
                    treinoAtual.data = dataTreino
                    break
                else:
                    print("Data inválida. Tente novamente.")

            treinoAtual.finalizarTreino()
            historico.registrarTreino(treinoAtual)
            treinoAtual = None

        elif opcao == "6":
            historico.visualizarHistorico()

        elif opcao == "7":
            if not plano.treinosProgramados:
                print("Não há treinos programados.")
            else:
                print("Planos de Treino:")
                for i, treino in enumerate(plano.treinosProgramados):
                    print(f"{i + 1}. {treino.nome} - {treino.nivelDificuldade}")
                    if treino.listaExercicios:
                        print("  Exercícios:")
                        for exercicio in treino.listaExercicios:
                            print(f"    - {exercicio.nomeExercicio}: {exercicio.series} séries, {exercicio.repeticoes} repetições, {exercicio.carga} kg")
                    else:
                        print("  Sem exercícios.")

                print("\n1. Editar Treino")
                print("2. Excluir Treino")
                print("3. Voltar ao Menu Principal")
                escolha = input("Escolha uma opção: ")

                if escolha == "1":
                    numero = int(input("Escolha o treino para editar (número): "))
                    treinoEditar = plano.treinosProgramados[numero - 1]

                    while True:
                        print(f"\nEditar Treino '{treinoEditar.nome}':")
                        print("1. Adicionar Exercício")
                        print("2. Remover Exercício")
                        print("3. Voltar ao Menu Principal")

                        subEscolha = input("Escolha uma opção: ")

                        if subEscolha == "1":
                            print("\nAdicionar Exercício:")
                            for i, ex in enumerate(EXERCICIOS_PREDEFINIDOS):
                                print(f"{i + 1}. {ex['nome']} - {ex['series']} séries, {ex['repeticoes']} repetições, {ex['carga']} kg")
                            print("11. Adicionar Exercício Personalizado")

                            escolhaExercicio = int(input("Escolha um número: "))
                            if 1 <= escolhaExercicio <= 10:
                                exercicioEscolhido = EXERCICIOS_PREDEFINIDOS[escolhaExercicio - 1]
                                exercicio = Exercicio(
                                    nomeExercicio=exercicioEscolhido["nome"],
                                    series=exercicioEscolhido["series"],
                                    repeticoes=exercicioEscolhido["repeticoes"],
                                    carga=exercicioEscolhido["carga"],
                                )
                                treinoEditar.adicionarExercicio(exercicio)
                                print(f"Exercício '{exercicio.nomeExercicio}' adicionado ao treino.")
                            elif escolhaExercicio == 11:
                                nomeExercicio = input("Nome do exercício: ")
                                series = int(input("Número de séries: "))
                                repeticoes = int(input("Número de repetições: "))
                                carga = float(input("Carga utilizada (kg): "))
                                exercicio = Exercicio(nomeExercicio, series, repeticoes, carga)
                                treinoEditar.adicionarExercicio(exercicio)
                                print(f"Exercício '{nomeExercicio}' adicionado ao treino.")
                            else:
                                print("Opção inválida.")
                        elif subEscolha == "2":
                            if not treinoEditar.listaExercicios:
                                print("Não há exercícios para remover.")
                            else:
                                for i, exercicio in enumerate(treinoEditar.listaExercicios):
                                    print(f"{i + 1}. {exercicio.nomeExercicio}")
                                removerIndice = int(input("Escolha o exercício para remover (número): ")) - 1
                                if 0 <= removerIndice < len(treinoEditar.listaExercicios):
                                    removido = treinoEditar.listaExercicios.pop(removerIndice)
                                    print(f"Exercício '{removido.nomeExercicio}' removido com sucesso.")
                                else:
                                    print("Opção inválida.")
                        elif subEscolha == "3":
                            break
                        else:
                            print("Opção inválida.")
                elif escolha == "2":
                    numero = int(input("Escolha o treino para excluir (número): "))
                    treinoExcluir = plano.treinosProgramados.pop(numero - 1)
                    print(f"Treino '{treinoExcluir.nome}' excluído com sucesso!")
                elif escolha == "3":
                    continue
                else:
                    print("Opção inválida.")

        elif opcao == "8":
            print("Saindo... Obrigado por usar a Berserker Workout!")
            break

        else:
            print("Opção inválida. Por favor, tente novamente.")
