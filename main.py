#Aléxis Ralfe da Silva Mendes 25/11/24
from classes.utilizador import Utilizador
from classes.treino import Treino
from classes.exercicio import Exercicio
from classes.planoTreino import PlanoTreino
from classes.historico import Historico
from datetime import datetime

#lista de exercicios predefinidos
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

#função para validar datas
def validarData(data):
    """valida se a data é válida e no formato AAAA-MM-DD."""
    try:
        datetime.strptime(data, "%Y-%m-%d")
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    print("Bem-vindo à Berserker Workout!")

    #recolher dados do utilizador
    nome = input("Insira o seu nome: ")
    idade = int(input("Insira a sua idade: "))
    peso = float(input("Insira o seu peso (kg, ex.: 70.5): ").replace(",", "."))
    altura = float(input("Insira a sua altura (m, ex.: 1.75): ").replace(",", "."))
    objetivo = input("Qual é o seu objetivo? (ex.: Perder peso, Ganhar massa): ")

    utilizador = Utilizador(nome=nome, idade=idade, peso=peso, altura=altura, objetivo=objetivo)

    treinoAtual = None
    plano_selecionado = None

    while True:
        print("\nEscolha uma opção:")
        print("1. Calcular IMC")
        print("2. Mostrar/Editar Dados do Utilizador")
        print("3. Gerir Planos de Treino")
        print("4. Visualizar Histórico de Treinos")
        print("5. Sair")

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

                    utilizador.atualizarPerfil(nome, int(idade), float(peso), float(altura), objetivo)
                    print("Dados atualizados com sucesso!")
                elif escolha == "2":
                    break
                else:
                    print("Opção inválida.")

        elif opcao == "3":
            while True:
                print("\nGerir Planos de Treino:")
                print("1. Criar Novo Plano de Treino")
                print("2. Selecionar Plano Existente")
                print("3. Remover Plano de Treino")
                print("4. Voltar ao Menu Principal")
                escolha = input("Escolha uma opção: ")

                if escolha == "1":
                    nomePlano = input("Nome do novo plano: ")
                    periodo = input("Período do plano: ")
                    novo_plano = PlanoTreino(nomePlano=nomePlano, periodo=periodo)
                    utilizador.adicionarPlanoTreino(novo_plano)
                    print(f"Plano '{nomePlano}' criado e adicionado ao utilizador.")

                elif escolha == "2":
                    planos = utilizador.listarPlanosTreino()
                    if not planos:
                        print("Não há planos de treino disponíveis.")
                        continue

                    print("Planos de Treino:")
                    for idx, plano in enumerate(planos):
                        print(f"{idx + 1}. {plano.nomePlano} - {plano.periodo}")

                    escolha_plano = int(input("Escolha o número do plano de treino: ")) - 1
                    if 0 <= escolha_plano < len(planos):
                        plano_selecionado = planos[escolha_plano]
                        print(f"Plano '{plano_selecionado.nomePlano}' selecionado.")

                        while True:
                            print(f"\nGerir Plano '{plano_selecionado.nomePlano}':")
                            print("1. Adicionar Treino")
                            print("2. Iniciar Treino")
                            print("3. Editar Treino")
                            print("4. Excluir Treino")
                            print("5. Voltar ao Menu Anterior")
                            sub_escolha = input("Escolha uma opção: ")

                            if sub_escolha == "1":
                                #criar um novo treino
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

                                #perguntar se deseja adicionar exercicios
                                while True:
                                    adicionar = input("Deseja adicionar exercícios a este treino? (s/n): ").lower()
                                    if adicionar == "s":
                                        print("\nEscolha um exercício da lista ou adicione um personalizado:")
                                        for i, ex in enumerate(EXERCICIOS_PREDEFINIDOS):
                                            print(f"{i + 1}. {ex['nome']} - {ex['series']} séries, {ex['repeticoes']} repetições, {ex['carga']} kg")
                                        print("11. Adicionar Exercício Personalizado")

                                        escolha_ex = int(input("Escolha um número: "))
                                        if 1 <= escolha_ex <= 10:
                                            ex_escolhido = EXERCICIOS_PREDEFINIDOS[escolha_ex - 1]
                                            exercicio = Exercicio(
                                                nomeExercicio=ex_escolhido["nome"],
                                                series=ex_escolhido["series"],
                                                repeticoes=ex_escolhido["repeticoes"],
                                                carga=ex_escolhido["carga"],
                                            )
                                            treino.adicionarExercicio(exercicio)
                                            print(f"Exercício '{exercicio.nomeExercicio}' adicionado com sucesso!")
                                        elif escolha_ex == 11:
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

                                plano_selecionado.criarPlano(treino)
                                print(f"Treino '{nomeTreino}' adicionado ao plano '{plano_selecionado.nomePlano}'.")

                            elif sub_escolha == "2":
                                #iniciar um treino
                                if not plano_selecionado.treinosProgramados:
                                    print("Não há treinos programados neste plano.")
                                    continue

                                print("Treinos disponíveis:")
                                for i, treino in enumerate(plano_selecionado.treinosProgramados):
                                    print(f"{i + 1}. {treino.nome} - {treino.nivelDificuldade}")

                                escolha_treino = int(input("Escolha o treino para iniciar (número): ")) - 1
                                if 0 <= escolha_treino < len(plano_selecionado.treinosProgramados):
                                    treinoAtual = plano_selecionado.treinosProgramados.pop(escolha_treino)
                                    treinoAtual.iniciarTreino()

                                    while True:
                                        dataTreino = input("Insira a data do treino (AAAA-MM-DD): ")
                                        if validarData(dataTreino):
                                            treinoAtual.data = dataTreino
                                            break
                                        else:
                                            print("Data inválida. Tente novamente.")

                                    treinoAtual.finalizarTreino()
                                    utilizador.historico.registrarTreino(treinoAtual)
                                    treinoAtual = None
                                else:
                                    print("Opção inválida.")

                            elif sub_escolha == "3":
                                #Editar treino
                                if not plano_selecionado.treinosProgramados:
                                    print("Não há treinos para editar neste plano.")
                                    continue

                                print("Treinos disponíveis:")
                                for i, treino in enumerate(plano_selecionado.treinosProgramados):
                                    print(f"{i + 1}. {treino.nome} - {treino.nivelDificuldade}")

                                escolha_treino = int(input("Escolha o treino para editar (número): ")) - 1
                                if 0 <= escolha_treino < len(plano_selecionado.treinosProgramados):
                                    treinoEditar = plano_selecionado.treinosProgramados[escolha_treino]

                                    while True:
                                        print(f"\nEditar Treino '{treinoEditar.nome}':")
                                        print("1. Adicionar Exercício")
                                        print("2. Remover Exercício")
                                        print("3. Editar Nome do Treino")
                                        print("4. Voltar ao Menu Anterior")

                                        subEscolha = input("Escolha uma opção: ")

                                        if subEscolha == "1":
                                            #adicionar exercicio
                                            print("\nAdicionar Exercício:")
                                            for i, ex in enumerate(EXERCICIOS_PREDEFINIDOS):
                                                print(f"{i + 1}. {ex['nome']} - {ex['series']} séries, {ex['repeticoes']} repetições, {ex['carga']} kg")
                                            print("11. Adicionar Exercício Personalizado")

                                            escolha_ex = int(input("Escolha um número: "))
                                            if 1 <= escolha_ex <= 10:
                                                ex_escolhido = EXERCICIOS_PREDEFINIDOS[escolha_ex - 1]
                                                exercicio = Exercicio(
                                                    nomeExercicio=ex_escolhido["nome"],
                                                    series=ex_escolhido["series"],
                                                    repeticoes=ex_escolhido["repeticoes"],
                                                    carga=ex_escolhido["carga"],
                                                )
                                                treinoEditar.adicionarExercicio(exercicio)
                                                print(f"Exercício '{exercicio.nomeExercicio}' adicionado ao treino.")
                                            elif escolha_ex == 11:
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
                                            #remover exercicio
                                            if not treinoEditar.listaExercicios:
                                                print("Não há exercícios para remover.")
                                            else:
                                                for i, exercicio in enumerate(treinoEditar.listaExercicios):
                                                    print(f"{i + 1}. {exercicio.nomeExercicio}")
                                                removerIndice = int(input("Escolha o exercício para remover (número): ")) - 1
                                                if 0 <= removerIndice < len(treinoEditar.listaExercicios):
                                                    removido = treinoEditar.removerExercicio(removerIndice)
                                                    print(f"Exercício '{removido.nomeExercicio}' removido com sucesso.")
                                                else:
                                                    print("Opção inválida.")

                                        elif subEscolha == "3":
                                            #editar nome do treino
                                            novo_nome = input("Insira o novo nome do treino: ")
                                            treinoEditar.editarNome(novo_nome)
                                            print(f"Nome do treino atualizado para '{novo_nome}'.")
                                        elif subEscolha == "4":
                                            break
                                        else:
                                            print("Opção inválida.")
                                else:
                                    print("Opção inválida.")

                            elif sub_escolha == "4":
                                #excluir treino
                                if not plano_selecionado.treinosProgramados:
                                    print("Não há treinos para excluir neste plano.")
                                    continue

                                print("Treinos disponíveis:")
                                for i, treino in enumerate(plano_selecionado.treinosProgramados):
                                    print(f"{i + 1}. {treino.nome} - {treino.nivelDificuldade}")

                                escolha_treino = int(input("Escolha o treino para excluir (número): ")) - 1
                                if 0 <= escolha_treino < len(plano_selecionado.treinosProgramados):
                                    treinoExcluir = plano_selecionado.excluirTreino(escolha_treino)
                                else:
                                    print("Opção inválida.")

                            elif sub_escolha == "5":
                                break
                            else:
                                print("Opção inválida.")
                    else:
                        print("Opção inválida.")

                elif escolha == "3":
                    #remover plano de treino
                    planos = utilizador.listarPlanosTreino()
                    if not planos:
                        print("Não há planos para remover.")
                        continue

                    print("Planos de Treino:")
                    for idx, plano in enumerate(planos):
                        print(f"{idx + 1}. {plano.nomePlano} - {plano.periodo}")

                    escolha_plano = int(input("Escolha o plano para remover: ")) - 1
                    if 0 <= escolha_plano < len(planos):
                        plano_removido = utilizador.removerPlanoTreino(escolha_plano)
                        print(f"Plano '{plano_removido.nomePlano}' removido.")
                    else:
                        print("Opção inválida.")

                elif escolha == "4":
                    break
                else:
                    print("Opção inválida.")

        elif opcao == "4":
            #visualizar historico de treinos
            utilizador.historico.visualizarHistorico()

        elif opcao == "5":
            print("Saindo... Obrigado por usar a Berserker Workout!")
            break

        else:
            print("Opção inválida. Por favor, tente novamente.")
