from classes.utilizador import Utilizador
from classes.treino import Treino
from classes.exercicio import Exercicio
from classes.planoTreino import PlanoTreino
from classes.historico import Historico

if __name__ == "__main__":
    print("Bem-vindo à Berserker Workout!")

    # Dados do utilizador
    nome = input("Insira o seu nome: ")
    idade = int(input("Insira a sua idade: "))
    peso = float(input("Insira o seu peso (kg): "))
    altura = float(input("Insira a sua altura (m): "))
    objetivo = input("Qual é o seu objetivo? (ex.: Perder peso, Ganhar massa): ")

    utilizador = Utilizador(nome=nome, idade=idade, peso=peso, altura=altura, objetivo=objetivo)
    plano = PlanoTreino(nomePlano="Plano Inicial", periodo="1 mês")
    historico = Historico()

    while True:
        print("\nEscolha uma opção:")
        print("1. Calcular IMC")
        print("2. Adicionar exercício a um treino")
        print("3. Criar treino e adicionar ao plano")
        print("4. Finalizar treino e registrar no histórico")
        print("5. Visualizar histórico de treinos")
        print("6. Sair")

        opcao = input("Insira a sua opção: ")

        if opcao == "1":
            imc = utilizador.calcularIMC()
            print(f"O seu IMC é: {imc:.2f}")

        elif opcao == "2":
            nomeExercicio = input("Nome do exercício: ")
            series = int(input("Número de séries: "))
            repeticoes = int(input("Número de repetições: "))
            carga = float(input("Carga utilizada (kg): "))

            exercicio = Exercicio(nomeExercicio, series, repeticoes, carga)
            print(f"Exercício {nomeExercicio} criado com sucesso!")

        elif opcao == "3":
            data = input("Data do treino (AAAA-MM-DD): ")
            nivelDificuldade = input("Nível de dificuldade (Fácil, Intermédio, Difícil): ")
            treino = Treino(data, nivelDificuldade)

            while True:
                adicionar = input("Deseja adicionar um exercício? (s/n): ").lower()
                if adicionar == "s":
                    nomeExercicio = input("Nome do exercício: ")
                    series = int(input("Número de séries: "))
                    repeticoes = int(input("Número de repetições: "))
                    carga = float(input("Carga utilizada (kg): "))
                    treino.adicionarExercicio(Exercicio(nomeExercicio, series, repeticoes, carga))
                elif adicionar == "n":
                    break

            plano.criarPlano(treino)
            print(f"Treino para {data} adicionado ao plano.")

        elif opcao == "4":
            if plano.treinosProgramados:
                treinoFinalizado = plano.treinosProgramados.pop(0)
                treinoFinalizado.finalizarTreino()
                historico.registrarTreino(treinoFinalizado)
            else:
                print("Nenhum treino programado.")

        elif opcao == "5":
            historico.visualizarHistorico()

        elif opcao == "6":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")
