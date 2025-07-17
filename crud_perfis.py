from utils import carregar_dados, salvar_dados, tipo_de_perfil
from validacoes import email_valido, senha_valida, telefone_valido

usuarios_json = 'usuarios.json'
estabelecimentos_json = 'estabelecimentos.json'
dados_usuarios = carregar_dados(usuarios_json)
dados_estabelecimentos = carregar_dados(estabelecimentos_json)


def criar_usuario():
    """
    Permite o cadastro de um novo usuário, com validações de email e senha.
    Gera um ID único para o novo usuário.
    """
    print("=== Cadastro de Usuário ===")
    nome = input("Nome: ")

    while True:
        email = input("Email (@gmail.com ou @hotmail.com, sem espaços): ")
        if not email_valido(email):
            print("Email inválido.")
        else:
            if any(u['email'] == email for u in dados_usuarios):
                print("Este email já está cadastrado.")
            else:
                break

    while True:
        senha = input("Senha (8+ caracteres, letras, números, sem espaços): ")
        if not senha_valida(senha):
            print("Senha inválida.")
        else:
            break
    print("""
    * Alternativo          * Forró              * Popular
    * Ao Vivo              * Futebol            * Regional
    * Ar Livre             * Geek               * Rock
    * Arte                 * Grupos             * Samba
    * Artesanal            * Happy Hour         * Saudável
    * Balada               * Íntimo             * Sertanejo
    * Boteco               * Jazz               * Sinuca
    * Café                 * Jogos              * Sucos
    * Comédia              * Karaokê            * Temático
    * Cultural             * LGBT               * Tranquilo
    * Dança                * MPB                * Vegano
    * DJ                   * Pet-Friendly       * Vinil
    * Drinks               * Petiscos           * Vinhos
    * Eletrônico           * Pop                * Vista
    """)
    print("Escolha três interesses")
    i1 = input("Digite seu primeiro interesse: ")
    i2 = input("Digite seu segundo interesse: ")
    i3 = input("Digite seu terceiro interesse: ")
    interesses = [i1.strip(), i2.strip(), i3.strip()] 

    while True:
        regiao = input("Região (formato: Cidade - Estado): ")
        if ' - ' not in regiao or len(regiao.split(' - ')) != 2:
            print("Formato inválido. Ex: Recife - Pernambuco")
        else:
            break

    novo_id = 1
    if dados_usuarios:
        novo_id = max(u['id'] for u in dados_usuarios) + 1

    global novo_usuario
    novo_usuario = {
        'id': novo_id,
        'nome': nome,
        'email': email,
        'senha': senha,
        'interesses': interesses,
        'regiao': regiao
    }
    dados_usuarios.append(novo_usuario)
    salvar_dados(usuarios_json, dados_usuarios)
    user_logado = novo_usuario
    print(f"Usuário cadastrado! Seu ID é: {novo_id}\nUse esse ID para atualizar ou excluir seu perfil.")
    return user_logado




def criar_estabelecimento():
    """
    Permite o cadastro de um novo estabelecimento, com validações.
    Gera um ID único para o novo estabelecimento.
    """
    print("=== Cadastro de Estabelecimento ===")
    nome = input("Nome: ")

    while True:
        email = input("Email (@gmail.com ou @hotmail.com, sem espaços): ")
        if not email_valido(email):
            print("Email inválido.")
        else:
            if any(e['email'] == email for e in dados_estabelecimentos):
                print("Este email já está cadastrado.")
            else:
                break

    while True:
        senha = input("Senha (8+ caracteres, letras, números, sem espaços): ")
        if not senha_valida(senha):
            print(" Senha inválida.")
        else:
            break

    endereco = input("Endereço: ")

    print("""
    * Alternativo          * Forró              * Popular
    * Ao Vivo              * Futebol            * Regional
    * Ar Livre             * Geek               * Rock
    * Arte                 * Grupos             * Samba
    * Artesanal            * Happy Hour         * Saudável
    * Balada               * Íntimo             * Sertanejo
    * Boteco               * Jazz               * Sinuca
    * Café                 * Jogos              * Sucos
    * Comédia              * Karaokê            * Temático
    * Cultural             * LGBT               * Tranquilo
    * Dança                * MPB                * Vegano
    * DJ                   * Pet-Friendly       * Vinil
    * Drinks               * Petiscos           * Vinhos
    * Eletrônico           * Pop                * Vista
    """)
    print("Informe os interesses do estabelecimento (três)")
    i1 = input("Digite seu primeiro interesse: ")
    i2 = input("Digite seu segundo interesse: ")
    i3 = input("Digite seu terceiro interesse: ")
    interesses = [i1.strip(), i2.strip(), i3.strip()]

    bio = input("Bio: ")

    while True:
        telefone = input("Telefone (DDD + número, ex: 81912345678): ")
        if not telefone_valido(telefone):
            print("Telefone inválido. Deve conter 11 dígitos numéricos.")
        else:
            break

    while True:
        regiao = input("Região (formato: Cidade - Estado): ")
        if ' - ' not in regiao or len(regiao.split(' - ')) != 2:
            print("Formato inválido. Ex: Recife - Pernambuco")
        else:
            break

    novo_id = 1
    if dados_estabelecimentos:
        novo_id = max(e['id'] for e in dados_estabelecimentos) + 1

    novo_est = {
        'id': novo_id,
        'nome': nome,
        'email': email,
        'senha': senha,
        'endereco': endereco,
        'interesses': interesses,
        'bio': bio,
        'telefone': telefone,
        'regiao': regiao
    }
    dados_estabelecimentos.append(novo_est)
    salvar_dados(estabelecimentos_json, dados_estabelecimentos)
    print(f"Estabelecimento cadastrado! Seu ID é: {novo_id}\nUse esse ID para atualizar ou excluir seu perfil.")




def atualizar_perfil():
    """
    Permite atualizar os dados de um perfil (usuário ou estabelecimento) existente.
    """
    tipo = tipo_de_perfil()
    id_input = input("Informe seu ID: ")
    try:
        id_ = int(id_input)
    except ValueError:
        print(" ID inválido. Deve ser um número inteiro.")
        return

    if tipo == "usuario":
        usuario_encontrado = None
        index = -1
        for i, usuario in enumerate(dados_usuarios):
            if usuario['id'] == id_:
                usuario_encontrado = usuario
                index = i
                break
        
        if not usuario_encontrado:
            print("Usuário não encontrado.")
            return

        nome = input(f"Novo nome (atual: {usuario_encontrado['nome']}) (pressione Enter para manter): ") or usuario_encontrado['nome']
        email = input(f"Novo email (atual: {usuario_encontrado['email']}) (pressione Enter para manter): ") or usuario_encontrado['email']
        senha = input(f"Nova senha (pressione Enter para manter): ") or usuario_encontrado['senha']
        
        print("""
    * Alternativo          * Forró              * Popular
    * Ao Vivo              * Futebol            * Regional
    * Ar Livre             * Geek               * Rock
    * Arte                 * Grupos             * Samba
    * Artesanal            * Happy Hour         * Saudável
    * Balada               * Íntimo             * Sertanejo
    * Boteco               * Jazz               * Sinuca
    * Café                 * Jogos              * Sucos
    * Comédia              * Karaokê            * Temático
    * Cultural             * LGBT               * Tranquilo
    * Dança                * MPB                * Vegano
    * DJ                   * Pet-Friendly       * Vinil
    * Drinks               * Petiscos           * Vinhos
    * Eletrônico           * Pop                * Vista
    """)
        print(f"Atualização dos interesses (atual: {', '.join(usuario_encontrado['interesses'])}")
        i1 = input("Digite seu primeiro interesse (pressione Enter para manter): ")
        i2 = input("Digite seu segundo interesse (pressione Enter para manter): ")
        i3 = input("Digite seu terceiro interesse (pressione Enter para manter): ")
        interesses = [i1.strip(), i2.strip(), i3.strip()]

        
        regiao = input(f"Nova região (atual: {usuario_encontrado['regiao']}) (pressione Enter para manter): ") or usuario_encontrado['regiao']


        dados_usuarios[index]['nome'] = nome
        dados_usuarios[index]['email'] = email
        dados_usuarios[index]['senha'] = senha
        dados_usuarios[index]['interesses'] = interesses
        dados_usuarios[index]['regiao'] = regiao

        salvar_dados(usuarios_json, dados_usuarios)
        print("Perfil atualizado com sucesso.\n")

    elif tipo == "estabelecimento":
        est_encontrado = None
        index = -1
        
        for i, est in enumerate(dados_estabelecimentos):
            if est['id'] == id_:
                est_encontrado = est
                index = i
                break
        
        if not est_encontrado:
            print("Estabelecimento não encontrado.")
            return


        nome = input(f"Novo nome (atual: {est_encontrado['nome']}) (pressione Enter para manter): ") or est_encontrado['nome']
        email = input(f"Novo email (atual: {est_encontrado['email']}) (pressione Enter para manter): ") or est_encontrado['email']
        senha = input(f"Nova senha (pressione Enter para manter): ") or est_encontrado['senha']
        endereco = input(f"Novo endereço (atual: {est_encontrado['endereco']}) (pressione Enter para manter): ") or est_encontrado['endereco']
        
        interesses_str = input(f"Novos interesses (atual: {', '.join(est_encontrado['interesses'])}) (pressione Enter para manter): ")

        interesses = [i.strip() for i in interesses_str.split(',')] if interesses_str else est_encontrado['interesses']
        
        bio = input(f"Nova bio (atual: {est_encontrado['bio']}) (pressione Enter para manter): ") or est_encontrado['bio']
        telefone = input(f"Novo telefone (atual: {est_encontrado['telefone']}) (pressione Enter para manter): ") or est_encontrado['telefone']
        regiao = input(f"Nova região (atual: {est_encontrado['regiao']}) (pressione Enter para manter): ") or est_encontrado['regiao']


        dados_estabelecimentos[index]['nome'] = nome
        dados_estabelecimentos[index]['email'] = email
        dados_estabelecimentos[index]['senha'] = senha
        dados_estabelecimentos[index]['endereco'] = endereco
        dados_estabelecimentos[index]['interesses'] = interesses
        dados_estabelecimentos[index]['bio'] = bio
        dados_estabelecimentos[index]['telefone'] = telefone
        dados_estabelecimentos[index]['regiao'] = regiao

        salvar_dados(estabelecimentos_json, dados_estabelecimentos)
        print("Estabelecimento atualizado com sucesso.\n")


def excluir_perfil():
    """
    Permite excluir um perfil (usuário ou estabelecimento) existente.
    """
    tipo = tipo_de_perfil()
    id_input = input("Informe seu ID: ")
    try:
        id_ = int(id_input) 
    except ValueError:
        print("ID inválido. Deve ser um número inteiro.")
        return

    if tipo == "usuario":
        usuario_encontrado_index = -1

        for i, usuario in enumerate(dados_usuarios):
            if usuario['id'] == id_:
                usuario_encontrado_index = i
                break

        if usuario_encontrado_index == -1:
            print("Usuário não encontrado.")
            return

        confirm = input(f"⚠️ Tem certeza que deseja excluir o perfil de '{dados_usuarios[usuario_encontrado_index]['nome']}'? Isso é irreversível (s/n): ")
        if confirm.lower() == "s":
            del dados_usuarios[usuario_encontrado_index]
            salvar_dados(usuarios_json, dados_usuarios)
            print("Perfil excluído.")
        else:
            print("Operação cancelada.")

    elif tipo == "estabelecimento":
        est_encontrado_index = -1

        for i, est in enumerate(dados_estabelecimentos):
            if est['id'] == id_:
                est_encontrado_index = i
                break

        if est_encontrado_index == -1:
            print("Estabelecimento não encontrado!")
            return

        confirm = input(f"⚠️ Tem certeza que deseja excluir '{dados_estabelecimentos[est_encontrado_index]['nome']}'? Isso é irreversível (s/n): ")
        if confirm.lower() == "s":
            del dados_estabelecimentos[est_encontrado_index]
            salvar_dados(estabelecimentos_json, dados_estabelecimentos)
            print("Estabelecimento excluído.")
        else:
            print("Operação cancelada.")


def ver_dados_por_id():
    """
    Exibe os dados de um perfil (usuário ou estabelecimento) específico pelo ID.
    """
    tipo = tipo_de_perfil()
    id_input = input("Informe seu ID: ")
    try:
        id_ = int(id_input)
    except ValueError:
        print("ID inválido. Deve ser um número inteiro.")
        return

    if tipo == "usuario":
        u = next((usuario for usuario in dados_usuarios if usuario['id'] == id_), None)
        if u:
            print(f"ID: {u['id']} | Nome: {u['nome']} | Email: {u['email']} | Interesses: {', '.join(u['interesses'])} | Região: {u['regiao']}")
        else:
            print("ID não encontrado.")

    elif tipo == "estabelecimento":
        e = next((est for est in dados_estabelecimentos if est['id'] == id_), None)
        if e:
            print(f"ID: {e['id']} | Nome: {e['nome']} | Email: {e['email']} | Endereço: {e['endereco']} | Região: {e['regiao']}")
        else:
            print("ID não encontrado.")