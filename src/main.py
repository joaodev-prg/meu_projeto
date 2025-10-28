from cadastro import adicionar_usuario, listar_usuarios

def exibir_menu():
    print("\n=== Sistema de Cadastro de Usuários ===")
    print("1 - Adicionar usuário")
    print("2 - Listar usuários")
    print("3 - Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            adicionar_usuario(nome, email)

        elif opcao == "2":
            listar_usuarios()

        elif opcao == "3":
            print("Encerrando o programa... 👋")
            break

        else:
            print("⚠️ Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
