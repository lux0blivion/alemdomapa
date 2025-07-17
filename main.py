from repositorios_perfis import RepositorioPerfis
from cadastro import cadastrar_usuario, cadastrar_estabelecimento
from filtros_recomendacoes import recomendar_estabelecimentos, recomendacao_aleatoria
from servicos_perfil import ServicoPerfil
from utils import tipo_de_perfil


# Inicializa o repositório e variável de login
repositorio = RepositorioPerfis('usuarios.json', 'estabelecimentos.json')
user_logado = None


def login():
    """
    Realiza o login e redireciona para o menu correspondente.
    """
    global user_logado
    print("=== LOGIN ===")
    tipo = tipo_de_perfil()
    email = input("Email: ").strip()
    senha = input("Senha: ").strip()

    if tipo == "usuario":
        for usuario in repositorio.usuarios:
            if usuario.email == email and usuario.senha == senha:
                user_logado = usuario
                print(f"\n✅ Login bem-sucedido! Bem-vindo, {usuario.nome} (ID: {usuario.id})")
                menu_usuario()
                return
        print("❌ Email ou senha incorretos.")

    elif tipo == "estabelecimento":
        for est in repositorio.estabelecimentos:
            if est.email == email and est.senha == senha:
                user_logado = est
                print(f"\n✅ Login bem-sucedido! Bem-vindo, {est.nome} (ID: {est.id})")
                menu_estabelecimento()
                return
        print("❌ Email ou senha incorretos.")


def menu_usuario():
    """
    Menu principal exclusivo para usuários.
    """
    print("\n=== MENU DO USUÁRIO ===")
    print("1. 📜 Ir para Área de Sugestões")
    print("2. 🎲 Recomendações Aleatórias")
    print("3. 💾 Atualizar dados do perfil")
    print("4. ❗ Excluir Perfil")
    print("5. 📄 Ver meus dados")
    print("6. 🚪 Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        recomendar_estabelecimentos(user_logado)
    elif escolha == "2":
        recomendacao_aleatoria()
    elif escolha == "3":
        ServicoPerfil.atualizar_usuario(user_logado, repositorio)
    elif escolha == "4":
        ServicoPerfil.excluir_perfil(user_logado, repositorio.usuarios, repositorio)
    elif escolha == "5":
        ServicoPerfil.ver_dados(user_logado)
    elif escolha == "6":
        print("Saindo...")
        exit()
    else:
        print("Opção inválida!")

    menu_usuario()  # volta para o menu


def menu_estabelecimento():
    """
    Menu principal exclusivo para estabelecimentos.
    """
    print("\n=== MENU DO ESTABELECIMENTO ===")
    print("1. 💾 Atualizar dados do perfil")
    print("2. ❗ Excluir Perfil")
    print("3. 📄 Ver meus dados")
    print("4. 🚪 Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        ServicoPerfil.atualizar_estabelecimento(user_logado, repositorio)
    elif escolha == "2":
        ServicoPerfil.excluir_perfil(user_logado, repositorio.estabelecimentos, repositorio)
    elif escolha == "3":
        ServicoPerfil.ver_dados(user_logado)
    elif escolha == "4":
        print("Saindo...")
        exit()
    else:
        print("Opção inválida!")

    menu_estabelecimento()  def avaliar_estabelecimento(usuario, repositorio):
    print("\n=== Avaliar Estabelecimento ===")

    for i, est in enumerate(repositorio.estabelecimentos):
        media = est.media_avaliacoes() if hasattr(est, 'media_avaliacoes') else 0
        print(f"{i+1}. {est.nome} - Média: {media}")

    try:
        escolha = int(input("\nDigite o número do estabelecimento que deseja avaliar: ")) - 1
        if 0 <= escolha < len(repositorio.estabelecimentos):
            nota = int(input("Dê uma nota de 1 a 5: "))
            if nota < 1 or nota > 5:
                print("Nota inválida.")
                return
            repositorio.estabelecimentos[escolha].adicionar_avaliacao(nota)
            repositorio.salvar_tudo()
            print("✅ Avaliação registrada com sucesso!")
        else:
            print("Estabelecimento não encontrado.")
    except ValueError:
        print("Entrada inválida.")



def menu_inicial():
    """
    Exibe o menu inicial para cadastro ou login.
    """
    while True:
        print("=== MENU INICIAL ===")
        print("1. 👤 Cadastrar Usuário")
        print("2. 🏪 Cadastrar Estabelecimento")
        print("3. 🔑 Login")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cadastrar_usuario(repositorio)
        elif escolha == "2":
            cadastrar_estabelecimento(repositorio)
        elif escolha == "3":
            login()
            break
        else:
            print("Opção inválida.")

menu_inicial()
