
from validacoes import telefone_valido
from modelos_perfis import Usuario, Estabelecimento
from repositorios_perfis import RepositorioPerfis

class ServicoPerfil:

    @staticmethod
    def atualizar_usuario(usuario: Usuario, repositorio: RepositorioPerfis):
        print("=== Atualizar Perfil de Usuário ===")

        nome = input(f"Novo nome (atual: {usuario.nome}): ") or usuario.nome
        email = input(f"Novo email (atual: {usuario.email}): ") or usuario.email
        senha = input("Nova senha (pressione Enter para manter): ") or usuario.senha

        print("Atualize seus interesses (pressione Enter para manter os atuais)")
        interesses = []
        for i, atual in enumerate(usuario.interesses):
            novo = input(f"Interesse {i+1} (atual: {atual}): ") or atual
            interesses.append(novo.strip())

        regiao = input(f"Nova região (atual: {usuario.regiao}): ") or usuario.regiao

        # Atualiza os atributos
        usuario.nome = nome
        usuario.email = email
        usuario.senha = senha
        usuario.interesses = interesses
        usuario.regiao = regiao

        repositorio.salvar_tudo()
        print("✅ Perfil de usuário atualizado com sucesso!")

    @staticmethod
    def atualizar_estabelecimento(estabelecimento: Estabelecimento, repositorio: RepositorioPerfis):
        print("=== Atualizar Perfil de Estabelecimento ===")

        nome = input(f"Novo nome (atual: {estabelecimento.nome}): ") or estabelecimento.nome
        email = input(f"Novo email (atual: {estabelecimento.email}): ") or estabelecimento.email
        senha = input("Nova senha (pressione Enter para manter): ") or estabelecimento.senha
        endereco = input(f"Novo endereço (atual: {estabelecimento.endereco}): ") or estabelecimento.endereco
        bio = input(f"Nova bio (atual: {estabelecimento.bio}): ") or estabelecimento.bio
        regiao = input(f"Nova região (atual: {estabelecimento.regiao}): ") or estabelecimento.regiao

        print("Atualize seus interesses (pressione Enter para manter os atuais)")
        interesses = []
        for i, atual in enumerate(estabelecimento.interesses):
            novo = input(f"Interesse {i+1} (atual: {atual}): ") or atual
            interesses.append(novo.strip())

        while True:
            telefone = input(f"Novo telefone (atual: {estabelecimento.telefone}): ") or estabelecimento.telefone
            if telefone_valido(telefone):
                break
            print("Telefone inválido. Deve ter 11 dígitos.")

        # Atualiza os atributos
        estabelecimento.nome = nome
        estabelecimento.email = email
        estabelecimento.senha = senha
        estabelecimento.endereco = endereco
        estabelecimento.bio = bio
        estabelecimento.regiao = regiao
        estabelecimento.interesses = interesses
        estabelecimento.telefone = telefone

        repositorio.salvar_tudo()
        print("✅ Perfil de estabelecimento atualizado com sucesso!")

    @staticmethod
    def excluir_perfil(perfil, lista, repositorio: RepositorioPerfis):
        confirm = input(f"⚠ Tem certeza que deseja excluir '{perfil.nome}'? (s/n): ")
        if confirm.lower() == 's':
            lista.remove(perfil)
            repositorio.salvar_tudo()
            print("❌ Perfil excluído com sucesso.")
            exit()
        else:
            print("Operação cancelada.")

    @staticmethod
    def ver_dados(perfil):
        print("\n📄 Dados do perfil:")
        print(f"ID: {perfil.id}")
        print(f"Nome: {perfil.nome}")
        print(f"Email: {perfil.email}")
        print(f"Interesses: {', '.join(perfil.interesses)}")
        print(f"Região: {perfil.regiao}")
        if isinstance(perfil, Estabelecimento):
            print(f"Endereço: {perfil.endereco}")
            print(f"Telefone: {perfil.telefone}")
            print(f"Bio: {perfil.bio}")
