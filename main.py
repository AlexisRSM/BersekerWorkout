# main.py - Ponto de entrada da aplicação
from classes.sistema import Sistema

ASCII_ART = r"""
    ____                                _                __          __           _                  _   
   |  _ \                              | |               \ \        / /          | |                | |  
   | |_) |  ___  _ __  ___   ___  _ __ | | __ ___  _ __   \ \  /\  / /___   _ __ | | __ ___   _   _ | |_ 
   |  _ <  / _ \| '__|/ __| / _ \| '__|| |/ // _ \| '__|   \ \/  \/ // _ \ | '__|| |/ // _ \ | | | || __|
   | |_) ||  __/| |   \__ \|  __/| |   |   <|  __/| |       \  /\  /| (_) || |   |   <| (_) || |_| || |_ 
   |____/  \___||_|   |___/ \___||_|   |_|\_\\___||_|        \/  \/  \___/ |_|   |_|\_\\___/  \__,_| \__|
"""

if __name__ == "__main__":
    print(ASCII_ART)
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
