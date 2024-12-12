# classe sistema
import json
import re
from datetime import datetime

from classes.utilizador import Utilizador
from classes.planoTreino import PlanoTreino
from classes.historico import Historico
from classes.treino import Treino, TreinoForca, TreinoCardio, TreinoSuperior, TreinoInferior
from classes.exercicio import Exercicio

def validarData(data):
    """valida se a data é válida e no formato aaaa-mm-dd."""
    try:
        datetime.strptime(data, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validar_username(username):
    """valida o nome de utilizador."""
    pattern = r'^[A-Za-z0-9_]+$'
    return re.match(pattern, username) is not None

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
    def __init__(self):
        self.utilizadores = {}
        self.utilizador_atual = None
        self.carregar_utilizadores()

    def criar_utilizador(self):
        """cria um novo utilizador."""
        print("dica: o nome de utilizador deve conter apenas letras, números ou underscore, sem espaços ou acentos.")
        while True:
            username = input("nome de utilizador: ")
            if validar_username(username):
                if username in self.utilizadores:
                    print("nome de utilizador já existe. tente outro.")
                else:
                    break
            else:
                print("username inválido. utilize apenas letras, números ou underscore.")

        password = input("defina uma senha: ")
        nome = input("nome completo: ")
        try:
            idade = int(input("idade: "))
            peso = float(input("peso (kg): ").replace(",", "." ))
            altura = float(input("altura (m): ").replace(",", "."))
        except ValueError:
            print("valores inválidos inseridos. tente novamente.")
            return

        print("escolha o seu objetivo:")
        print("1. perder peso")
        print("2. manter peso e tonificar")
        print("3. ganhar massa muscular")
        while True:
            obj_choice = input("insira o número do objetivo: ")
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
                print("opção inválida. escolha entre 1, 2 ou 3.")

        novo_utilizador = Utilizador(nome, idade, peso, altura, objetivo, username, password)
        self.utilizadores[username] = novo_utilizador
        self.salvar_utilizadores()
        print(f"utilizador '{username}' criado com sucesso!")

    def login_utilizador(self):
        """permite o login do utilizador."""
        username = input("nome de utilizador: ")
        password = input("senha: ")

        if username in self.utilizadores:
            utilizador = self.utilizadores[username]
            if utilizador.password == password:
                self.utilizador_atual = utilizador
                print(f"bem-vindo(a), {utilizador.nome}!")
            else:
                print("senha incorreta.")
        else:
            print("utilizador não encontrado.")

    def visualizar_utilizadores(self):
        """exibe a lista de utilizadores."""
        if not self.utilizadores:
            print("nenhum utilizador registrado.")
        else:
            print("\n=== lista de utilizadores ===")
            for username, utilizador in self.utilizadores.items():
                print(f"username: {username} | nome: {utilizador.nome} | objetivo: {utilizador.objetivo}")

    def salvar_utilizadores(self, arquivo='utilizadores.json'):
        """salva os utilizadores no ficheiro json."""
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
            print(f"erro ao salvar utilizadores: {e}")

    def carregar_utilizadores(self, arquivo='utilizadores.json'):
        """carrega os utilizadores do ficheiro json."""
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

                            t.data = treino_data["data"]
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
            print(f"erro ao carregar utilizadores: {e}")

    def menu_utilizador(self):
        """menu do utilizador logado."""
        if not self.utilizador_atual:
            print("nenhum utilizador logado.")
            return

        while self.utilizador_atual:
            print(f"\n=== menu de {self.utilizador_atual.nome} ===")
            print("1. calcular imc e calorias recom.")
            print("2. gerir planos")
            print("3. visualizar histórico")
            print("4. editar perfil")
            print("5. calcular calorias diárias (objetivo atual)")
            print("6. logout")

            escolha = input("escolha: ")
            if escolha == "1":
                imc = self.utilizador_atual.calcularIMC()
                print(f"imc de {self.utilizador_atual.nome}: {imc:.2f}")
                print("deseja ajustar ingestão calórica?")
                print("1. perda rápida (-300 kcal)")
                print("2. perda lenta (-150 kcal)")
                print("3. manter (0 kcal)")
                print("4. ganhar massa (+200 kcal)")
                print("enter para não calcular agora")
                sub = input("opção: ")
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
                    print("opção inválida. mantendo valor base.")

                if sub in ['1','2','3','4']:
                    print(f"ingestão calórica recomendada: {calorias_base:.0f} kcal/dia")

            elif escolha == "2":
                self.menu_planos()
            elif escolha == "3":
                self.utilizador_atual.historico.visualizarHistorico()
            elif escolha == "4":
                self.editar_perfil()
            elif escolha == "5":
                calorias = self.utilizador_atual.calcularCaloriasDiarias()
                print(f"baseado no seu objetivo, recomendamos aproximadamente {calorias:.0f} calorias/dia.")
            elif escolha == "6":
                print(f"logout do utilizador '{self.utilizador_atual.nome}'.")
                self.utilizador_atual = None
            else:
                print("opção inválida. tente novamente.")

    def editar_perfil(self):
        """edita o perfil do utilizador atual."""
        if not self.utilizador_atual:
            return
        print("\n=== editar perfil ===")
        idade = input(f"nova idade (enter para manter {self.utilizador_atual.idade}): ")
        peso = input(f"novo peso (enter para manter {self.utilizador_atual.peso}): ")
        altura = input(f"nova altura (enter para manter {self.utilizador_atual.altura}): ")

        print("selecione um novo objetivo (ou enter para manter o atual):")
        print("objetivo atual:", self.utilizador_atual.objetivo)
        print("1. perder peso")
        print("2. manter peso e tonificar")
        print("3. ganhar massa muscular")
        print("enter para manter o objetivo atual.")
        obj_choice = input("insira o número do objetivo: ")

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
            print("opção inválida. mantendo objetivo atual.")

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
        print("perfil atualizado com sucesso!")

    def menu_planos(self):
        """menu de gestão de planos."""
        while True:
            print("\n=== gestão de planos ===")
            print("1. criar novo plano")
            print("2. visualizar planos existentes")
            print("3. gerir/editar um plano")
            print("4. remover plano")
            print("5. voltar ao menu anterior")

            escolha = input("escolha: ")

            if escolha == "1":
                nomePlano = input("nome do plano: ")
                periodo = input("período do plano (ex.: 1 mês): ")
                novo_plano = PlanoTreino(nomePlano, periodo)
                self.utilizador_atual.planosTreino.append(novo_plano)
                self.salvar_utilizadores()
                print(f"plano '{nomePlano}' criado com sucesso.")
                add_now = input("deseja adicionar um treino agora? (s/n): ").lower()
                if add_now == 's':
                    self.menu_editar_plano(novo_plano)

            elif escolha == "2":
                if not self.utilizador_atual.planosTreino:
                    print("nenhum plano disponível.")
                else:
                    print("\n=== planos de treino ===")
                    for idx, plano in enumerate(self.utilizador_atual.planosTreino):
                        print(f"{idx + 1}. {plano.nomePlano} ({plano.periodo})")

            elif escolha == "3":
                if not self.utilizador_atual.planosTreino:
                    print("nenhum plano disponível para editar.")
                    continue

                print("\n=== editar/ gerir planos ===")
                for idx, plano in enumerate(self.utilizador_atual.planosTreino):
                    print(f"{idx + 1}. {plano.nomePlano} ({plano.periodo})")

                try:
                    escolha_plano = int(input("escolha o plano para gerir: ")) - 1
                except ValueError:
                    print("opção inválida.")
                    continue

                if 0 <= escolha_plano < len(self.utilizador_atual.planosTreino):
                    plano = self.utilizador_atual.planosTreino[escolha_plano]
                    self.menu_editar_plano(plano)
                else:
                    print("opção inválida.")

            elif escolha == "4":
                if not self.utilizador_atual.planosTreino:
                    print("nenhum plano disponível para remover.")
                    continue

                print("\n=== remover planos ===")
                for idx, plano in enumerate(self.utilizador_atual.planosTreino):
                    print(f"{idx + 1}. {plano.nomePlano} ({plano.periodo})")

                try:
                    escolha_plano = int(input("escolha o plano para remover: ")) - 1
                except ValueError:
                    print("opção inválida.")
                    continue

                if 0 <= escolha_plano < len(self.utilizador_atual.planosTreino):
                    plano_removido = self.utilizador_atual.planosTreino.pop(escolha_plano)
                    self.salvar_utilizadores()
                    print(f"plano '{plano_removido.nomePlano}' removido com sucesso.")
                else:
                    print("opção inválida.")

            elif escolha == "5":
                break
            else:
                print("opção inválida. tente novamente.")

    def menu_editar_plano(self, plano):
        """menu para editar um plano."""
        while True:
            print(f"\n=== gerir plano: {plano.nomePlano} ({plano.periodo}) ===")
            print("1. editar nome e período do plano")
            print("2. adicionar treino")
            print("3. gerir treinos (visualizar/editar/remover)")
            print("4. voltar")

            escolha = input("escolha: ")

            if escolha == '1':
                novo_nome = input(f"novo nome (enter para manter {plano.nomePlano}): ") or plano.nomePlano
                novo_periodo = input(f"novo período (enter para manter {plano.periodo}): ") or plano.periodo
                plano.nomePlano = novo_nome
                plano.periodo = novo_periodo
                self.salvar_utilizadores()
                print("plano atualizado com sucesso.")

            elif escolha == '2':
                nomeTreino = input("nome do treino: ")
                print("\nescolha a dificuldade:")
                print("1. fácil")
                print("2. intermédio")
                print("3. difícil")

                nivel = input("insira a dificuldade (1, 2 ou 3): ")
                dificuldades = {"1": "Fácil", "2": "Intermédio", "3": "Difícil"}
                while nivel not in dificuldades:
                    print("opção inválida. escolha 1, 2 ou 3.")
                    nivel = input("insira a dificuldade (1, 2 ou 3): ")

                print("\nescolha o tipo de treino:")
                print("1. força")
                print("2. cardio")
                print("3. superior")
                print("4. inferior")

                tipo = input("insira o tipo (1, 2, 3 ou 4): ")
                while tipo not in ["1", "2", "3", "4"]:
                    print("opção inválida. escolha 1, 2, 3 ou 4.")
                    tipo = input("insira o tipo (1, 2, 3 ou 4): ")

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
                print(f"treino '{nomeTreino}' adicionado ao plano '{plano.nomePlano}'.")

                # perguntar se quer adicionar exercícios agora
                add_ex = input("deseja adicionar exercícios a este treino agora? (s/n): ").lower()
                if add_ex == 's':
                    self.menu_gerir_exercicios_treino(treino, exercicios_tipo)
                    self.salvar_utilizadores()

            elif escolha == '3':
                if not plano.treinosProgramados:
                    print("não há treinos neste plano.")
                    continue
                for i, tr in enumerate(plano.treinosProgramados):
                    print(f"{i + 1}. {tr.nome} - {tr.nivelDificuldade}")

                try:
                    es_treino = int(input("escolha um treino para gerir: ")) - 1
                except ValueError:
                    print("opção inválida.")
                    continue

                if 0 <= es_treino < len(plano.treinosProgramados):
                    self.menu_editar_treino(plano, es_treino)
                else:
                    print("opção inválida.")

            elif escolha == '4':
                break
            else:
                print("opção inválida.")

    def menu_editar_treino(self, plano, indice_treino):
        """menu para editar um treino."""
        treino = plano.treinosProgramados[indice_treino]
        while True:
            print(f"\n=== gerir treino: {treino.nome} ({treino.nivelDificuldade}) ===")
            print("1. adicionar exercício")
            print("2. remover exercício")
            print("3. editar nome do treino")
            print("4. finalizar treino (definir data, duração e registar histórico)")
            print("5. voltar")

            escolha = input("escolha: ")

            if escolha == '1':
                if isinstance(treino, TreinoForca):
                    exercicios_tipo = EXERCICIOS_FORCA
                elif isinstance(treino, TreinoCardio):
                    exercicios_tipo = EXERCICIOS_CARDIO
                elif isinstance(treino, TreinoSuperior):
                    exercicios_tipo = EXERCICIOS_SUPERIOR
                elif isinstance(treino, TreinoInferior):
                    exercicios_tipo = EXERCICIOS_INFERIOR
                else:
                    exercicios_tipo = []
                self.menu_gerir_exercicios_treino(treino, exercicios_tipo)
                self.salvar_utilizadores()

            elif escolha == '2':
                if not treino.listaExercicios:
                    print("não há exercícios para remover.")
                else:
                    for i, ex in enumerate(treino.listaExercicios):
                        print(f"{i + 1}. {ex.nomeExercicio} - {ex.series}x{ex.repeticoes}@{ex.carga}kg")
                    try:
                        ex_rmv = int(input("escolha o exercício para remover: ")) - 1
                    except ValueError:
                        print("opção inválida.")
                        continue
                    if 0 <= ex_rmv < len(treino.listaExercicios):
                        removido = treino.removerExercicio(ex_rmv)
                        print(f"exercício '{removido.nomeExercicio}' removido.")
                        self.salvar_utilizadores()
                    else:
                        print("índice inválido.")

            elif escolha == '3':
                novo_nome = input("novo nome do treino: ")
                treino.editarNome(novo_nome)
                self.salvar_utilizadores()
                print("nome do treino atualizado.")

            elif escolha == '4':
                if not treino.iniciado:
                    treino.iniciarTreino()

                while True:
                    dataTreino = input("insira a data do treino (aaaa-mm-dd): ")
                    if validarData(dataTreino):
                        treino.data = dataTreino
                        break
                    else:
                        print("data inválida. tente novamente.")

                try:
                    duracao_min = float(input("insira a duração do treino em minutos: "))
                except ValueError:
                    duracao_min = 0

                peso_user = self.utilizador_atual.peso
                calorias = treino.calcularCaloriasQueimadas(peso_user, duracao_min)
                treino.caloriasQueimadas = calorias

                treino.finalizarTreino()
                self.utilizador_atual.historico.registrarTreino(treino)
                self.salvar_utilizadores()
                print(f"treino finalizado e registrado no histórico. calorias queimadas: {calorias:.2f} kcal")

            elif escolha == '5':
                break
            else:
                print("opção inválida.")

    def menu_gerir_exercicios_treino(self, treino, exercicios_tipo):
        """menu para adicionar exercícios (pré-definidos ou personalizados)."""
        while True:
            print("\n=== adicionar exercício ===")
            print("lista de exercícios pré-definidos para este tipo de treino:")
            for i, ex in enumerate(exercicios_tipo):
                print(f"{i + 1}. {ex['nome']} - {ex['series']}x{ex['repeticoes']} @ {ex['carga']}kg")
            print("0. adicionar exercício personalizado")
            print("enter sem valor para voltar")

            escolha = input("escolha um exercício (número) ou enter para voltar: ")
            if escolha == "":
                break
            try:
                escolha_num = int(escolha)
            except ValueError:
                print("opção inválida.")
                continue

            if escolha_num == 0:
                nomeEx = input("nome do exercício: ")
                try:
                    series = int(input("número de séries: "))
                    repeticoes = int(input("número de repetições: "))
                    carga = float(input("carga utilizada (kg): "))
                except ValueError:
                    print("valores inválidos para séries/rep/carga.")
                    continue
                ex_personalizado = Exercicio(nomeEx, series, repeticoes, carga)
                treino.adicionarExercicio(ex_personalizado)
                print(f"exercício '{nomeEx}' adicionado com sucesso!")
            elif 1 <= escolha_num <= len(exercicios_tipo):
                ex_escolhido = exercicios_tipo[escolha_num - 1]
                exerc = Exercicio(
                    nomeExercicio=ex_escolhido["nome"],
                    series=ex_escolhido["series"],
                    repeticoes=ex_escolhido["repeticoes"],
                    carga=ex_escolhido["carga"]
                )
                treino.adicionarExercicio(exerc)
                print(f"exercício '{exerc.nomeExercicio}' adicionado com sucesso!")
            else:
                print("opção inválida.")
