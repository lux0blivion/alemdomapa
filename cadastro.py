
from validacoes import email_valido, senha_valida, telefone_valido
from modelos_perfis import Usuario, Estabelecimento
from repositorios_perfis import RepositorioPerfis

def cadastrar_usuario(repositorio: RepositorioPerfis):
    print("=== Cadastro de Usuário ===")
    nome = input("Nome: ")

    while True:
        email = input("Email: ")
        if not email_valido(email) or any(u.email == email for u in repositorio.usuarios):
            print("Email inválido ou já cadastrado.")
        else:
            break

    while True:
        senha = input("Senha: ")
        if not senha_valida(senha):
            print("Senha inválida.")
        else:
            break

    print("Escolha três interesses")
    interesses = [input(f"Interesse {i+1}: ").strip() for i in range(3)]

    while True:
        regiao = input("Região (formato: Cidade - Estado): ")
        if ' - ' not in regiao:
            print("Formato inválido.")
        else:
            break

    novo_id = repositorio.gerar_novo_id(repositorio.usuarios)
    usuario = Usuario(novo_id, nome, email, senha, interesses, regiao)
    repositorio.usuarios.append(usuario)
    repositorio.salvar_tudo()

    print(f"Usuário cadastrado com sucesso! ID: {novo_id}")
    return usuario

def cadastrar_estabelecimento(repositorio: RepositorioPerfis):
    print("=== Cadastro de Estabelecimento ===")
    nome = input("Nome: ")

    while True:
        email = input("Email: ")
        if not email_valido(email) or any(e.email == email for e in repositorio.estabelecimentos):
            print("Email inválido ou já cadastrado.")
        else:
            break

    while True:
        senha = input("Senha: ")
        if not senha_valida(senha):
            print("Senha inválida.")
        else:
            break

    endereco = input("Endereço: ")

    print("Informe três interesses do estabelecimento:")
    interesses = [input(f"Interesse {i+1}: ").strip() for i in range(3)]

    bio = input("Bio: ")

    while True:
        telefone = input("Telefone (DDD + número): ")
        if not telefone_valido(telefone):
            print("Telefone inválido. Deve conter 11 dígitos.")
        else:
            break

    while True:
        regiao = input("Região (formato: Cidade - Estado): ")
        if ' - ' not in regiao:
            print("Formato inválido.")
        else:
            break

    novo_id = repositorio.gerar_novo_id(repositorio.estabelecimentos)
    est = Estabelecimento(novo_id, nome, email, senha, interesses, regiao, endereco, telefone, bio)
    repositorio.estabelecimentos.append(est)
    repositorio.salvar_tudo()

    print(f"Estabelecimento cadastrado com sucesso! ID: {novo_id}")
    return est

