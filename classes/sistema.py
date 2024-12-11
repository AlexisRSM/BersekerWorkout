# sistema.py - Classe Sistema
import json
import re
from datetime import datetime

from classes.utilizador import Utilizador
from classes.planoTreino import PlanoTreino
from classes.historico import Historico
from classes.treino import Treino, TreinoForca, TreinoCardio, TreinoSuperior, TreinoInferior
from classes.exercicio import Exercicio

def validarData(data):
    """Valida se a data é válida e no formato AAAA-MM-DD."""
    try:
        datetime.strptime(data, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validar_username(username):
    pattern = r'^[A-Za-z0-9_]+$'
    return re.match(pattern, username) is not None

# Exercícios pré-definidos por tipo de treino
EXERCICIOS_FORCA = [
    {"nome": "Levantamento Terra", "series": 4, "repeticoes": 6, "carga": 60},
    {"nome": "Supino Plano", "series": 4, "repeticoes": 8, "carga": 40},
    {"nome": "Agachamento Barra", "series": 4, "repeticoes": 6, "carga": 50}
]

EXERCICIOS_CARDIO = [
    {"nome": "Correr na Passadeira", "series": 1, "repeticoes": 1, "carga": 0},
    {"nome": "Elíptica", "series": 1, "repeticoes": 1, "carga": 0},
    {"nome": "Bicicleta Estacionária", "series": 1, "repeticoes": 1, "carga": 0}
]

EXERCICIOS_SUPERIOR = [
    {"nome": "Supino Inclinado", "series": 3, "repeticoes": 10, "carga": 30},
    {"nome": "Remada Sentada", "series": 3, "repeticoes": 12, "carga": 25},
    {"nome": "Desenvolvimento de Ombros", "series": 3, "repeticoes": 8, "carga": 20}
]

EXERCICIOS_INFERIOR = [
    {"nome": "Leg Press", "series": 3, "repeticoes": 12, "carga": 50},
    {"nome": "Extensora de Pernas", "series": 3, "repeticoes": 12, "carga": 30},
    {"nome": "Flexora de Pernas", "series": 3, "repeticoes": 12, "carga": 25}
]

class Sistema:
    """sistema.py - Classe Sistema"""
    def __init__(self):
        self.utilizadores = {}
        self.utilizador_atual = None
        self.carregar_utilizadores()

    def criar_utilizador(self):
        print("Dica: O nome de utilizador deve conter apenas letras, números ou underscore, sem espaços ou acentos.")
        while True:
            username = input("Nome de utilizador: ")
            if validar_username(username):
                if username in self.utilizadores:
                    print("Nome de utilizador já existe. Tente outro.")
                else:
                    break
            else:
                print("Username inválido. Utilize apenas letras, números ou underscore.")

        password = input("Defina uma senha: ")
        nome = input("Nome completo: ")
        try:
            idade = int(input("Idade: "))
            peso = float(input("Peso (kg): ").replace(",", "." ))
            altura = float(input("Altura (m): ").replace(",", "."))
        except ValueError:
            print("Valores inválidos inseridos. Tente novamente.")
            return

        print("Escolha o seu objetivo:")
        print("1. Perder Peso")
        print("2. Manter Peso e Tonificar")
        print("3. Ganhar Massa Muscular")
        while True:
            obj_choice = input("Insira o número do objetivo: ")
            if obj_choice == '1':
                objetivo = "Perder Peso"
                break
            elif obj_choice == '2':
                objetivo = "Manter Peso e Tonificar"
                break
            elif obj_choice == '3':
                objetivo = "Ganhar Massa Muscular"
                break
            else:
                print("Opção inválida. Escolha entre 1, 2 ou 3.")

        novo_utilizador = Utilizador(nome, idade, peso, altura, objetivo, username, password)
        self.utilizadores[username] = novo_utilizador
        self.salvar_utilizadores()
        print(f"Utilizador '{username}' criado com sucesso!")

    def login_utilizador(self):
        username = input("Nome de utilizador: ")
        password = input("Senha: ")

        if username in self.utilizadores:
            utilizador = self.utilizadores[username]
            if utilizador.password == password:
                self.utilizador_atual = utilizador
                print(f"Bem-vindo(a), {utilizador.nome}!")
            else:
                print("Senha incorreta.")
        else:
            print("Utilizador não encontrado.")

    def visualizar_utilizadores(self):
        if not self.utilizadores:
            print("Nenhum utilizador registrado.")
        else:
            print("\n=== Lista de Utilizadores ===")
            for username, utilizador in self.utilizadores.items():
                print(f"Username: {username} | Nome: {utilizador.nome} | Objetivo: {utilizador.objetivo}")

    def salvar_utilizadores(self, arquivo='utilizadores.json'):
        try:
            dados = {
                username: {
                    "nome": utilizador.nome,
                    "username": utilizador.username,
                    "password": utilizador.password,
                    "idade": utilizador.idade,
                    "peso": utilizador.peso,
                    "altura": utilizador.altura,
                    "objetivo": utilizador.objetivo,
                    "historico": utilizador.historico.to_dict(),
                    "planosTreino": [
                        {
                            "nomePlano": plano.nomePlano,
                            "periodo": plano.periodo,
                            "treinosProgramados": [
                                {
                                    "nome": treino.nome,
                                    "nivelDificuldade": treino.nivelDificuldade,
                                    "tipo": (
                                        "forca" if isinstance(treino, TreinoForca) else
                                        "cardio" if isinstance(treino, TreinoCardio) else
                                        "superior" if isinstance(treino, TreinoSuperior) else
                                        "inferior" if isinstance(treino, TreinoInferior) else
                                        "generico"
                                    ),
                                    "caloriasQueimadas": treino.caloriasQueimadas,
                                    "data": treino.data,
                                    "listaExercicios": [
                                        {
                                            "nomeExercicio": ex.nomeExercicio,
                                            "series": ex.series,
                                            "repeticoes": ex.repeticoes,
                                            "carga": ex.carga
                                        }
                                        for ex in treino.listaExercicios
                                    ]
                                }
                                for treino in plano.treinosProgramados
                            ]
                        }
                        for plano in utilizador.planosTreino
                    ]
                }
                for username, utilizador in self.utilizadores.items()
            }
            with open(arquivo, 'w', encoding='utf-8') as f:
                json.dump(dados, f, indent=4)
        except Exception as e:
            print(f"Erro ao salvar utilizadores: {e}")

    def carregar_utilizadores(self, arquivo='utilizadores.json'):
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                for username, info in dados.items():
                    historico = Historico.from_dict(info["historico"])
                    planosTreino = []
                    for plano in info["planosTreino"]:
                        treinos = []
                        for treino_data in plano["treinosProgramados"]:
                            tipo = treino_data.get("tipo", "generico")
                            listaEx = [
                                Exercicio(
                                    nomeExercicio=ex["nomeExercicio"],
                                    series=ex["series"],
                                    repeticoes=ex["repeticoes"],
                                    carga=ex["carga"]
                                )
                                for ex in treino_data["listaExercicios"]
                            ]
                            if tipo == "forca":
                                t = TreinoForca(nome=treino_data["nome"], nivelDificuldade=treino_data["nivelDificuldade"], listaExercicios=listaEx)
                            elif tipo == "cardio":
                                t = TreinoCardio(nome=treino_data["nome"], nivelDificuldade=treino_data["nivelDificuldade"], listaExercicios=listaEx)
                            elif tipo == "superior":
                                t = TreinoSuperior(nome=treino_data["nome"], nivelDificuldade=treino_data["nivelDificuldade"], listaExercicios=listaEx)
                            elif tipo == "inferior":
                                t = TreinoInferior(nome=treino_data["nome"], nivelDificuldade=treino_data["nivelDificuldade"], listaExercicios=listaEx)
                            else:
                                t = Treino(nome=treino_data["nome"], nivelDificuldade=treino_data["nivelDificuldade"], listaExercicios=listaEx)

                            t.data = treino_data.get("data", None)
                            t.caloriasQueimadas = treino_data.get("caloriasQueimadas", 0)
                            treinos.append(t)

                        planosTreino.append(
                            PlanoTreino(
                                nomePlano=plano["nomePlano"],
                                periodo=plano["periodo"],
                                treinosProgramados=treinos
                            )
                        )

                    utilizador = Utilizador(
                        nome=info["nome"],
                        idade=info["idade"],
                        peso=info["peso"],
                        altura=info["altura"],
                        objetivo=info["objetivo"],
                        username=info["username"],
                        password=info["password"]
                    )
                    utilizador.historico = historico
                    utilizador.planosTreino = planosTreino
                    self.utilizadores[username] = utilizador
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Erro ao carregar utilizadores: {e}")

    def menu_utilizador(self):
        if not self.utilizador_atual:
            print("Nenhum utilizador logado.")
            return

        while self.utilizador_atual:
            print(f"\n=== Menu de {self.utilizador_atual.nome} ===")
            print("1. Calcular IMC e Calorias Recom.")
            print("2. Gerir Planos")
            print("3. Visualizar Histórico")
            print("4. Editar Perfil")
            print("5. Calcular Calorias Diárias (Objetivo Atual)")
            print("6. Logout")

            escolha = input("Escolha: ")
            if escolha == "1":
                imc = self.utilizador_atual.calcularIMC()
                print(f"IMC de {self.utilizador_atual.nome}: {imc:.2f}")
                # Ajustar ingestão calórica
                print("Deseja ajustar ingestão calórica?")
                print("1. Perda Rápida (-300 kcal)")
                print("2. Perda Lenta (-150 kcal)")
                print("3. Manter (0 kcal)")
                print("4. Ganhar Massa (+200 kcal)")
                print("Enter para não calcular agora")
                sub = input("Opção: ")
                calorias_base = self.utilizador_atual.calcularCaloriasDiarias()
                if sub == '1':
                    calorias_base -= 300
                elif sub == '2':
                    calorias_base -= 150
                elif sub == '3':
                    calorias_base = calorias_base
                elif sub == '4':
                    calorias_base += 200
                elif sub == '':
                    pass
                else:
                    print("Opção inválida. Mantendo valor base.")

                if sub in ['1','2','3','4']:
                    print(f"Ingestão Calórica Recomendada: {calorias_base:.0f} kcal/dia")

            elif escolha == "2":
                self.menu_planos()
            elif escolha == "3":
                self.utilizador_atual.historico.visualizarHistorico()
            elif escolha == "4":
                self.editar_perfil()
            elif escolha == "5":
                calorias = self.utilizador_atual.calcularCaloriasDiarias()
                print(f"Baseado no seu objetivo, recomendamos aproximadamente {calorias:.0f} calorias/dia.")
            elif escolha == "6":
                print(f"Logout do utilizador '{self.utilizador_atual.nome}'.")
                self.utilizador_atual = None
            else:
                print("Opção inválida. Tente novamente.")

    def editar_perfil(self):
        if not self.utilizador_atual:
            return
        print("\n=== Editar Perfil ===")
        idade = input(f"Nova idade (Enter para manter {self.utilizador_atual.idade}): ")
        peso = input(f"Novo peso (Enter para manter {self.utilizador_atual.peso}): ")
        altura = input(f"Nova altura (Enter para manter {self.utilizador_atual.altura}): ")

        print("Selecione um novo objetivo (ou Enter para manter o atual):")
        print("Objetivo atual:", self.utilizador_atual.objetivo)
        print("1. Perder Peso")
        print("2. Manter Peso e Tonificar")
        print("3. Ganhar Massa Muscular")
        print("Enter para manter o objetivo atual.")
        obj_choice = input("Insira o número do objetivo: ")

        objetivo = self.utilizador_atual.objetivo
        if obj_choice == '1':
            objetivo = "Perder Peso"
        elif obj_choice == '2':
            objetivo = "Manter Peso e Tonificar"
        elif obj_choice == '3':
            objetivo = "Ganhar Massa Muscular"
        elif obj_choice == '':
            pass
        else:
            print("Opção inválida. Mantendo objetivo atual.")

        nova_idade = int(idade) if idade else self.utilizador_atual.idade
        novo_peso = float(peso) if peso else self.utilizador_atual.peso
        nova_altura = float(altura) if altura else self.utilizador_atual.altura

        self.utilizador_atual.atualizarPerfil(
            idade=nova_idade,
            peso=novo_peso,
            altura=nova_altura,
            objetivo=objetivo
        )
        self.salvar_utilizadores()
        print("Perfil atualizado com sucesso!")

    def menu_planos(self):
        while True:
            print("\n=== Gestão de Planos ===")
            print("1. Criar Novo Plano")
            print("2. Visualizar Planos Existentes")
            print("3. Gerir/Editar um Plano")
            print("4. Remover Plano")
            print("5. Voltar ao Menu Anterior")

            escolha = input("Escolha: ")

            if escolha == "1":
                nomePlano = input("Nome do plano: ")
                periodo = input("Período do plano (ex.: 1 mês): ")
                novo_plano = PlanoTreino(nomePlano, periodo)
                self.utilizador_atual.planosTreino.append(novo_plano)
                self.salvar_utilizadores()
                print(f"Plano '{nomePlano}' criado com sucesso.")
                add_now = input("Deseja adicionar um treino agora? (s/n): ").lower()
                if add_now == 's':
                    self.menu_editar_plano(novo_plano)

            elif escolha == "2":
                if not self.utilizador_atual.planosTreino:
                    print("Nenhum plano disponível.")
                else:
                    print("\n=== Planos de Treino ===")
                    for idx, plano in enumerate(self.utilizador_atual.planosTreino):
                        print(f"{idx + 1}. {plano.nomePlano} ({plano.periodo})")

            elif escolha == "3":
                if not self.utilizador_atual.planosTreino:
                    print("Nenhum plano disponível para editar.")
                    continue

                print("\n=== Editar/Gerir Planos ===")
                for idx, plano in enumerate(self.utilizador_atual.planosTreino):
                    print(f"{idx + 1}. {plano.nomePlano} ({plano.periodo})")

                try:
                    escolha_plano = int(input("Escolha o plano para gerir: ")) - 1
                except ValueError:
                    print("Opção inválida.")
                    continue

                if 0 <= escolha_plano < len(self.utilizador_atual.planosTreino):
                    plano = self.utilizador_atual.planosTreino[escolha_plano]
                    self.menu_editar_plano(plano)
                else:
                    print("Opção inválida.")

            elif escolha == "4":
                if not self.utilizador_atual.planosTreino:
                    print("Nenhum plano disponível para remover.")
                    continue

                print("\n=== Remover Planos ===")
                for idx, plano in enumerate(self.utilizador_atual.planosTreino):
                    print(f"{idx + 1}. {plano.nomePlano} ({plano.periodo})")

                try:
                    escolha_plano = int(input("Escolha o plano para remover: ")) - 1
                except ValueError:
                    print("Opção inválida.")
                    continue

                if 0 <= escolha_plano < len(self.utilizador_atual.planosTreino):
                    plano_removido = self.utilizador_atual.planosTreino.pop(escolha_plano)
                    self.salvar_utilizadores()
                    print(f"Plano '{plano_removido.nomePlano}' removido com sucesso.")
                else:
                    print("Opção inválida.")

            elif escolha == "5":
                break
            else:
                print("Opção inválida. Tente novamente.")

    def menu_editar_plano(self, plano):
        while True:
            print(f"\n=== Gerir Plano: {plano.nomePlano} ({plano.periodo}) ===")
            print("1. Editar Nome e Período do Plano")
            print("2. Adicionar Treino")
            print("3. Gerir Treinos (Visualizar/Editar/Remover)")
            print("4. Voltar")

            escolha = input("Escolha: ")

            if escolha == '1':
                novo_nome = input(f"Novo nome (Enter para manter {plano.nomePlano}): ") or plano.nomePlano
                novo_periodo = input(f"Novo período (Enter para manter {plano.periodo}): ") or plano.periodo
                plano.nomePlano = novo_nome
                plano.periodo = novo_periodo
                self.salvar_utilizadores()
                print("Plano atualizado com sucesso.")

            elif escolha == '2':
                nomeTreino = input("Nome do treino: ")
                print("\nEscolha a dificuldade:")
                print("1. Fácil")
                print("2. Intermédio")
                print("3. Difícil")

                nivel = input("Insira a dificuldade (1, 2 ou 3): ")
                dificuldades = {"1": "Fácil", "2": "Intermédio", "3": "Difícil"}
                while nivel not in dificuldades:
                    print("Opção inválida. Escolha 1, 2 ou 3.")
                    nivel = input("Insira a dificuldade (1, 2 ou 3): ")

                print("\nEscolha o tipo de treino:")
                print("1. Força")
                print("2. Cardio")
                print("3. Superior")
                print("4. Inferior")

                tipo = input("Insira o tipo (1, 2, 3 ou 4): ")
                while tipo not in ["1", "2", "3", "4"]:
                    print("Opção inválida. Escolha 1, 2, 3 ou 4.")
                    tipo = input("Insira o tipo (1, 2, 3 ou 4): ")

                if tipo == "1":
                    treino = TreinoForca(nivelDificuldade=dificuldades[nivel], nome=nomeTreino)
                    exercicios_tipo = EXERCICIOS_FORCA
                elif tipo == "2":
                    treino = TreinoCardio(nivelDificuldade=dificuldades[nivel], nome=nomeTreino)
                    exercicios_tipo = EXERCICIOS_CARDIO
                elif tipo == "3":
                    treino = TreinoSuperior(nivelDificuldade=dificuldades[nivel], nome=nomeTreino)
                    exercicios_tipo = EXERCICIOS_SUPERIOR
                else:
                    treino = TreinoInferior(nivelDificuldade=dificuldades[nivel], nome=nomeTreino)
                    exercicios_tipo = EXERCICIOS_INFERIOR

                plano.criarPlano(treino)
                self.salvar_utilizadores()
                print(f"Treino '{nomeTreino}' adicionado ao plano '{plano.nomePlano}'.")

                # Perguntar se quer adicionar exercícios agora
                add_ex = input("Deseja adicionar exercícios a este treino agora? (s/n): ").lower()
                if add_ex == 's':
                    self.menu_gerir_exercicios_treino(treino, exercicios_tipo)
                    self.salvar_utilizadores()

            elif escolha == '3':
                if not plano.treinosProgramados:
                    print("Não há treinos neste plano.")
                    continue
                for i, tr in enumerate(plano.treinosProgramados):
                    print(f"{i + 1}. {tr.nome} - {tr.nivelDificuldade}")

                try:
                    es_treino = int(input("Escolha um treino para gerir: ")) - 1
                except ValueError:
                    print("Opção inválida.")
                    continue

                if 0 <= es_treino < len(plano.treinosProgramados):
                    self.menu_editar_treino(plano, es_treino)
                else:
                    print("Opção inválida.")

            elif escolha == '4':
                break
            else:
                print("Opção inválida.")

    def menu_editar_treino(self, plano, indice_treino):
        treino = plano.treinosProgramados[indice_treino]
        while True:
            print(f"\n=== Gerir Treino: {treino.nome} ({treino.nivelDificuldade}) ===")
            print("1. Adicionar Exercício")
            print("2. Remover Exercício")
            print("3. Editar Nome do Treino")
            print("4. Finalizar Treino (definir data, duração e registar histórico)")
            print("5. Voltar")

            escolha = input("Escolha: ")

            if escolha == '1':
                # Determinar o tipo de exercicios default
                if isinstance(treino, TreinoForca):
                    exercicios_tipo = EXERCICIOS_FORCA
                elif isinstance(treino, TreinoCardio):
                    exercicios_tipo = EXERCICIOS_CARDIO
                elif isinstance(treino, TreinoSuperior):
                    exercicios_tipo = EXERCICIOS_SUPERIOR
                elif isinstance(treino, TreinoInferior):
                    exercicios_tipo = EXERCICIOS_INFERIOR
                else:
                    exercicios_tipo = []  # Caso genérico
                self.menu_gerir_exercicios_treino(treino, exercicios_tipo)
                self.salvar_utilizadores()

            elif escolha == '2':
                if not treino.listaExercicios:
                    print("Não há exercícios para remover.")
                else:
                    for i, ex in enumerate(treino.listaExercicios):
                        print(f"{i + 1}. {ex.nomeExercicio} - {ex.series}x{ex.repeticoes}@{ex.carga}kg")
                    try:
                        ex_rmv = int(input("Escolha o exercício para remover: ")) - 1
                    except ValueError:
                        print("Opção inválida.")
                        continue
                    if 0 <= ex_rmv < len(treino.listaExercicios):
                        removido = treino.removerExercicio(ex_rmv)
                        print(f"Exercício '{removido.nomeExercicio}' removido.")
                        self.salvar_utilizadores()
                    else:
                        print("Índice inválido.")

            elif escolha == '3':
                novo_nome = input("Novo nome do treino: ")
                treino.editarNome(novo_nome)
                self.salvar_utilizadores()
                print("Nome do treino atualizado.")

            elif escolha == '4':
                if not treino.iniciado:
                    treino.iniciarTreino()

                while True:
                    dataTreino = input("Insira a data do treino (AAAA-MM-DD): ")
                    if validarData(dataTreino):
                        treino.data = dataTreino
                        break
                    else:
                        print("Data inválida. Tente novamente.")

                try:
                    duracao_min = float(input("Insira a duração do treino em minutos: "))
                except ValueError:
                    duracao_min = 0

                peso_user = self.utilizador_atual.peso
                calorias = treino.calcularCaloriasQueimadas(peso_user, duracao_min)
                treino.caloriasQueimadas = calorias

                treino.finalizarTreino()
                self.utilizador_atual.historico.registrarTreino(treino)
                self.salvar_utilizadores()
                print(f"Treino finalizado e registrado no histórico. Calorias Queimadas: {calorias:.2f} kcal")

            elif escolha == '5':
                break
            else:
                print("Opção inválida.")

    def menu_gerir_exercicios_treino(self, treino, exercicios_tipo):
        while True:
            print("\n=== Adicionar Exercício ===")
            print("Lista de Exercícios Pré-definidos para este tipo de treino:")
            for i, ex in enumerate(exercicios_tipo):
                print(f"{i + 1}. {ex['nome']} - {ex['series']}x{ex['repeticoes']} @ {ex['carga']}kg")
            print("0. Adicionar Exercício Personalizado")
            print("Enter sem valor para voltar")

            escolha = input("Escolha um exercício (número) ou Enter para voltar: ")
            if escolha == "":
                break
            try:
                escolha_num = int(escolha)
            except ValueError:
                print("Opção inválida.")
                continue

            if escolha_num == 0:
                nomeEx = input("Nome do exercício: ")
                try:
                    series = int(input("Número de séries: "))
                    repeticoes = int(input("Número de repetições: "))
                    carga = float(input("Carga utilizada (kg): "))
                except ValueError:
                    print("Valores inválidos para séries/rep/carga.")
                    continue
                ex_personalizado = Exercicio(nomeEx, series, repeticoes, carga)
                treino.adicionarExercicio(ex_personalizado)
                print(f"Exercício '{nomeEx}' adicionado com sucesso!")
            elif 1 <= escolha_num <= len(exercicios_tipo):
                ex_escolhido = exercicios_tipo[escolha_num - 1]
                exerc = Exercicio(
                    nomeExercicio=ex_escolhido["nome"],
                    series=ex_escolhido["series"],
                    repeticoes=ex_escolhido["repeticoes"],
                    carga=ex_escolhido["carga"]
                )
                treino.adicionarExercicio(exerc)
                print(f"Exercício '{exerc.nomeExercicio}' adicionado com sucesso!")
            else:
                print("Opção inválida.")
