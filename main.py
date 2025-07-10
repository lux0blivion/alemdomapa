from utils import carregar_dados, tipo_de_perfil
from crud_perfis import criar_usuario, criar_estabelecimento, atualizar_perfil, excluir_perfil, ver_dados_por_id
from filtros_recomendacoes import recomendar_estabelecimentos, recomendacao_aleatoria


usuarios_json = 'usuarios.json'
estabelecimentos_json = 'estabelecimentos.json'

dados_usuarios = carregar_dados(usuarios_json)
dados_estabelecimentos = carregar_dados(estabelecimentos_json)



 
def login():
    """
    Realiza o login de um usuário ou estabelecimento.
    """
    print("=== LOGIN ===")
    tipo = tipo_de_perfil()
    email = input("Email: ").strip()
    senha = input("Senha: ").strip()

    if tipo == "usuario":
        usuario_encontrado = None
        for usuario in dados_usuarios:
            if usuario['email'] == email and usuario['senha'] == senha:
                usuario_encontrado = usuario
                break
        if usuario_encontrado:
            print(f"\nLogin bem-sucedido! Bem-vindo, {usuario_encontrado['nome']} (ID: {usuario_encontrado['id']})")
            global user_logado
            user_logado = usuario_encontrado
            menu_principal()
        else:
            print(" Email ou senha incorretos.")

    elif tipo == "estabelecimento":
        est_encontrado = None
        for est in dados_estabelecimentos:
            if est['email'] == email and est['senha'] == senha:
                est_encontrado = est
                break
        if est_encontrado:
            print(f"\nLogin bem-sucedido! Bem-vindo, {est_encontrado['nome']} (ID: {est_encontrado['id']})")
            menu_principal()
        else:
            print(" Email ou senha incorretos.")




def menu_principal():
    """
    Exibe o menu principal e direciona para as funções correspondentes.
    """
    print("\n=== MENU PRINCIPAL ===")
    print("\n1. 📜 Ir para Área de Sugestões")
    print("\n2. 🎲 Ir para Recomendações Aleatórias")
    print("\n3. 💾 Atualizar dados do perfil")
    print("\n4. ❗ Excluir Perfil")
    print("\n5. 📄 Ver meus dados")
    print("\n6. 🚪 Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        recomendar_estabelecimentos(user_logado)
    elif escolha == "2":
        recomendacao_aleatoria()
    elif escolha == "3":
        atualizar_perfil()
    elif escolha == "4":
        excluir_perfil()
    elif escolha == "5":
        ver_dados_por_id()
    elif escolha == "6":
        print("Saindo...")
        exit()
    else:
        print("Opção inválida!")

    menu_principal()


def menu_inicial():
    """
    Exibe o menu inicial para cadastro ou login.
    """
    while True:
        print("=== MENU INICIAL ===")
        print("\n1. 👤 Cadastrar Usuário")
        print("\n2. 🏪 Cadastrar Estabelecimento")
        print("\n3. 🔑 Login")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            criar_usuario()
            break
        elif escolha == "2":
            criar_estabelecimento()
            break
        elif escolha == "3":
            login()
            break
        else:
            print("Opção inválida.")


menu_inicial()
