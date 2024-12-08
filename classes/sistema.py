import json
from classes.utilizador import Utilizador
from classes.historico import Historico
from classes.planoTreino import PlanoTreino

class Sistema:
    def __init__(self):
        self.utilizadores = {}  # Dicionário {username: objeto Utilizador}
        self.utilizador_atual = None
        self.carregar_utilizadores()

    def criar_utilizador(self):
        """Cria um novo utilizador, garantindo unicidade do nome de utilizador."""
        username = input("Nome de utilizador: ")
        if username in self.utilizadores:
            print("Nome de utilizador já existe. Tente outro.")
            return

        password = input("Defina uma senha: ")
        nome = input("Nome completo: ")
        idade = int(input("Idade: "))
        peso = float(input("Peso (kg): ").replace(",", "."))
        altura = float(input("Altura (m): ").replace(",", "."))
        objetivo = input("Objetivo: ")

        novo_utilizador = Utilizador(nome, idade, peso, altura, objetivo, username, password)
        self.utilizadores[username] = novo_utilizador
        self.salvar_utilizadores()
        print(f"Utilizador '{username}' criado com sucesso!")

    def login_utilizador(self):
        """Permite que um utilizador faça login."""
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
        """Exibe todos os utilizadores registrados no sistema."""
        if not self.utilizadores:
            print("Nenhum utilizador registrado.")
        else:
            print("\n=== Lista de Utilizadores ===")
            for username, utilizador in self.utilizadores.items():
                print(f"Username: {username} | Nome: {utilizador.nome} | Objetivo: {utilizador.objetivo}")

    def salvar_utilizadores(self, arquivo='utilizadores.json'):
        """Salva os utilizadores no arquivo JSON."""
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
                        {"nomePlano": plano.nomePlano, "periodo": plano.periodo}
                        for plano in utilizador.planosTreino
                    ]
                }
                for username, utilizador in self.utilizadores.items()
            }
            with open(arquivo, 'w') as f:
                json.dump(dados, f, indent=4)
            print("Utilizadores salvos com sucesso.")
        except Exception as e:
            print(f"Erro ao salvar utilizadores: {e}")

    def carregar_utilizadores(self, arquivo='utilizadores.json'):
        """Carrega os utilizadores do arquivo JSON."""
        try:
            with open(arquivo, 'r') as f:
                dados = json.load(f)
                for username, info in dados.items():
                    historico = Historico.from_dict(info["historico"])
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
                    utilizador.planosTreino = [
                        PlanoTreino(plano["nomePlano"], plano["periodo"])
                        for plano in info.get("planosTreino", [])
                    ]
                    self.utilizadores[username] = utilizador
            print("Utilizadores carregados com sucesso.")
        except FileNotFoundError:
            print("Arquivo de utilizadores não encontrado. Será criado ao salvar.")
        except Exception as e:
            print(f"Erro ao carregar utilizadores: {e}")

    def menu_utilizador(self):
        """Apresenta o menu para o utilizador logado."""
        while self.utilizador_atual:
            print(f"\n=== Menu de {self.utilizador_atual.nome} ===")
            print("1. Calcular IMC")
            print("2. Gerir Planos")
            print("3. Visualizar Histórico")
            print("4. Logout")

            escolha = input("Escolha: ")
            if escolha == "1":
                imc = self.utilizador_atual.calcularIMC()
                print(f"IMC de {self.utilizador_atual.nome}: {imc:.2f}")
            elif escolha == "2":
                self.menu_planos()
            elif escolha == "3":
                self.utilizador_atual.historico.visualizarHistorico()
            elif escolha == "4":
                print(f"Logout do utilizador '{self.utilizador_atual.nome}'.")
                self.utilizador_atual = None
            else:
                print("Opção inválida. Tente novamente.")

    def menu_planos(self):
        """Gerencia os planos de treino do utilizador logado."""
        while True:
            print("\n=== Gestão de Planos ===")
            print("1. Criar Novo Plano")
            print("2. Visualizar Planos Existentes")
            print("3. Editar Plano")
            print("4. Remover Plano")
            print("5. Voltar ao Menu Anterior")

            escolha = input("Escolha: ")

            if escolha == "1":
                nomePlano = input("Nome do plano: ")
                periodo = input("Período do plano (ex.: 1 mês): ")
                novo_plano = PlanoTreino(nomePlano, periodo)
                self.utilizador_atual.planosTreino.append(novo_plano)
                print(f"Plano '{nomePlano}' criado com sucesso.")

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

                print("\n=== Editar Planos ===")
                for idx, plano in enumerate(self.utilizador_atual.planosTreino):
                    print(f"{idx + 1}. {plano.nomePlano} ({plano.periodo})")

                escolha_plano = int(input("Escolha o plano para editar: ")) - 1
                if 0 <= escolha_plano < len(self.utilizador_atual.planosTreino):
                    plano = self.utilizador_atual.planosTreino[escolha_plano]
                    novo_nome = input(
                        f"Novo nome para o plano '{plano.nomePlano}' (Enter para manter): ") or plano.nomePlano
                    novo_periodo = input(
                        f"Novo período para o plano '{plano.periodo}' (Enter para manter): ") or plano.periodo
                    plano.nomePlano = novo_nome
                    plano.periodo = novo_periodo
                    print("Plano atualizado com sucesso.")
                else:
                    print("Opção inválida.")

            elif escolha == "4":
                if not self.utilizador_atual.planosTreino:
                    print("Nenhum plano disponível para remover.")
                    continue

                print("\n=== Remover Planos ===")
                for idx, plano in enumerate(self.utilizador_atual.planosTreino):
                    print(f"{idx + 1}. {plano.nomePlano} ({plano.periodo})")

                escolha_plano = int(input("Escolha o plano para remover: ")) - 1
                if 0 <= escolha_plano < len(self.utilizador_atual.planosTreino):
                    plano_removido = self.utilizador_atual.planosTreino.pop(escolha_plano)
                    print(f"Plano '{plano_removido.nomePlano}' removido com sucesso.")
                else:
                    print("Opção inválida.")

            elif escolha == "5":
                break

            else:
                print("Opção inválida. Tente novamente.")
