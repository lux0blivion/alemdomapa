import re
import json
import random


usuarios_json = 'usuarios.json'
estabelecimentos_json = 'estabelecimentos.json'

# Funções de Carregamento e Salvamento de Dados
def carregar_dados(caminho):
    """
    Carrega dados de um arquivo JSON.
    Se o arquivo não for encontrado ou estiver vazio/inválido, retorna uma lista vazia.
    """
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Retorna uma lista vazia se o arquivo não existir ou for um JSON inválido
        return []
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao carregar '{caminho}': {e}")
        return []

def salvar_dados(caminho, dados):
    """
    Salva dados em um arquivo JSON.
    """
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

# Carregar os dados iniciais ao iniciar o programa
# Assegura que as listas de dados estejam sempre atualizadas com o conteúdo dos arquivos
dados_usuarios = carregar_dados(usuarios_json)
dados_estabelecimentos = carregar_dados(estabelecimentos_json)

# Funções de Validação
def email_valido(email):
    """
    Verifica se o email é válido (formato e domínios permitidos).
    """
    email = email.strip()
    if ' ' in email:
        return False
    padrao = r'^[\w\.-]+@(gmail\.com|hotmail\.com)$'
    return re.match(padrao, email)

def senha_valida(senha):
    """
    Verifica se a senha é válida (mínimo 8 caracteres, letras, números, sem espaços).
    """
    if senha != senha.strip():
        return False
    if ' ' in senha:
        return False
    if len(senha) < 8:
        return False
    if not re.search(r'[A-Za-z]', senha):
        return False
    if not re.search(r'[0-9]', senha):
        return False
    return True

def telefone_valido(telefone):
    """
    Verifica se o telefone é válido (11 dígitos numéricos).
    """
    return telefone.isdigit() and len(telefone) == 11

# Funções Auxiliares
def tipo_de_perfil():
    """
    Solicita ao usuário que escolha o tipo de perfil (usuário ou estabelecimento).
    """
    print("Qual o tipo do seu perfil?")
    print("1. Usuário")
    print("2. Estabelecimento")
    escolha = input("Digite 1 ou 2: ")
    if escolha == "1":
        return "usuario"
    elif escolha == "2":
        return "estabelecimento"
    else:
        print("❌ Tipo inválido. Tente novamente.\n")
        return tipo_de_perfil()
    
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
        # Procura o usuário na lista de dados de usuários
        for usuario in dados_usuarios:
            if usuario['email'] == email and usuario['senha'] == senha:
                usuario_encontrado = usuario
                break
        if usuario_encontrado:
            print(f"\n✅ Login bem-sucedido! Bem-vindo, {usuario_encontrado['nome']} (ID: {usuario_encontrado['id']})")
            menu_principal()
        else:
            print("❌ Email ou senha incorretos.")

    elif tipo == "estabelecimento":
        est_encontrado = None
        # Procura o estabelecimento na lista de dados de estabelecimentos
        for est in dados_estabelecimentos:
            if est['email'] == email and est['senha'] == senha:
                est_encontrado = est
                break
        if est_encontrado:
            print(f"\n✅ Login bem-sucedido! Bem-vindo, {est_encontrado['nome']} (ID: {est_encontrado['id']})")
            menu_principal()
        else:
            print("❌ Email ou senha incorretos.")

# Cadastro
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
            print("❌ Email inválido.")
        else:
            # Verifica se o email já existe na lista de usuários
            if any(u['email'] == email for u in dados_usuarios):
                print("❌ Este email já está cadastrado.")
            else:
                break

    while True:
        senha = input("Senha (8+ caracteres, letras, números, sem espaços): ")
        if not senha_valida(senha):
            print("❌ Senha inválida.")
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
    # Armazena interesses como uma lista de strings
    interesses = [i1.strip(), i2.strip(), i3.strip()] 

    while True:
        regiao = input("Região (formato: Cidade - Estado): ")
        if ' - ' not in regiao or len(regiao.split(' - ')) != 2:
            print("❌ Formato inválido. Ex: Recife - Pernambuco")
        else:
            break

    # Gerar novo ID: encontra o maior ID existente e adiciona 1, ou começa com 1 se a lista estiver vazia
    novo_id = 1
    if dados_usuarios:
        novo_id = max(u['id'] for u in dados_usuarios) + 1

    novo_usuario = {
        'id': novo_id,
        'nome': nome,
        'email': email,
        'senha': senha,
        'interesses': interesses,
        'regiao': regiao
    }
    dados_usuarios.append(novo_usuario)
    salvar_dados(usuarios_json, dados_usuarios) # Salva as alterações no arquivo JSON
    print(f"✅ Usuário cadastrado! Seu ID é: {novo_id}\nUse esse ID para atualizar ou excluir seu perfil.")

    menu_principal()

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
            print("❌ Email inválido.")
        else:
            # Verifica se o email já existe na lista de estabelecimentos
            if any(e['email'] == email for e in dados_estabelecimentos):
                print("❌ Este email já está cadastrado.")
            else:
                break

    while True:
        senha = input("Senha (8+ caracteres, letras, números, sem espaços): ")
        if not senha_valida(senha):
            print("❌ Senha inválida.")
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
    # Armazena interesses como uma lista de strings
    interesses = [i1.strip(), i2.strip(), i3.strip()]

    bio = input("Bio: ")

    while True:
        telefone = input("Telefone (DDD + número, ex: 81912345678): ")
        if not telefone_valido(telefone):
            print("❌ Telefone inválido. Deve conter 11 dígitos numéricos.")
        else:
            break

    while True:
        regiao = input("Região (formato: Cidade - Estado): ")
        if ' - ' not in regiao or len(regiao.split(' - ')) != 2:
            print("❌ Formato inválido. Ex: Recife - Pernambuco")
        else:
            break

    # Gerar novo ID: encontra o maior ID existente e adiciona 1, ou começa com 1 se a lista estiver vazia
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
    salvar_dados(estabelecimentos_json, dados_estabelecimentos) # Salva as alterações no arquivo JSON
    print(f"✅ Estabelecimento cadastrado! Seu ID é: {novo_id}\nUse esse ID para atualizar ou excluir seu perfil.")

    menu_principal()

# Atualizar Perfil
def atualizar_perfil():
    """
    Permite atualizar os dados de um perfil (usuário ou estabelecimento) existente.
    """
    tipo = tipo_de_perfil()
    id_input = input("Informe seu ID: ")
    try:
        id_ = int(id_input) # Converte o ID para inteiro
    except ValueError:
        print("❌ ID inválido. Deve ser um número inteiro.")
        return

    if tipo == "usuario":
        usuario_encontrado = None
        index = -1
        # Encontra o usuário pelo ID e seu índice na lista
        for i, usuario in enumerate(dados_usuarios):
            if usuario['id'] == id_:
                usuario_encontrado = usuario
                index = i
                break
        
        if not usuario_encontrado:
            print("❌ Usuário não encontrado.")
            return

        # Solicita novos dados, mantendo os antigos se o campo for deixado em branco
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
        # Armazena interesses como uma lista de strings
        interesses = [i1.strip(), i2.strip(), i3.strip()]

        
        regiao = input(f"Nova região (atual: {usuario_encontrado['regiao']}) (pressione Enter para manter): ") or usuario_encontrado['regiao']

        # Atualiza o dicionário diretamente na lista
        dados_usuarios[index]['nome'] = nome
        dados_usuarios[index]['email'] = email
        dados_usuarios[index]['senha'] = senha
        dados_usuarios[index]['interesses'] = interesses
        dados_usuarios[index]['regiao'] = regiao

        salvar_dados(usuarios_json, dados_usuarios) # Salva as alterações no arquivo JSON
        print("✅ Perfil atualizado com sucesso.\n")

    elif tipo == "estabelecimento":
        est_encontrado = None
        index = -1
        # Encontra o estabelecimento pelo ID e seu índice na lista
        for i, est in enumerate(dados_estabelecimentos):
            if est['id'] == id_:
                est_encontrado = est
                index = i
                break
        
        if not est_encontrado:
            print("❌ Estabelecimento não encontrado.")
            return

        # Solicita novos dados, mantendo os antigos se o campo for deixado em branco
        nome = input(f"Novo nome (atual: {est_encontrado['nome']}) (pressione Enter para manter): ") or est_encontrado['nome']
        email = input(f"Novo email (atual: {est_encontrado['email']}) (pressione Enter para manter): ") or est_encontrado['email']
        senha = input(f"Nova senha (pressione Enter para manter): ") or est_encontrado['senha']
        endereco = input(f"Novo endereço (atual: {est_encontrado['endereco']}) (pressione Enter para manter): ") or est_encontrado['endereco']
        
        interesses_str = input(f"Novos interesses (atual: {', '.join(est_encontrado['interesses'])}) (pressione Enter para manter): ")
        # Se o usuário digitou novos interesses, converte a string para uma lista
        interesses = [i.strip() for i in interesses_str.split(',')] if interesses_str else est_encontrado['interesses']
        
        bio = input(f"Nova bio (atual: {est_encontrado['bio']}) (pressione Enter para manter): ") or est_encontrado['bio']
        telefone = input(f"Novo telefone (atual: {est_encontrado['telefone']}) (pressione Enter para manter): ") or est_encontrado['telefone']
        regiao = input(f"Nova região (atual: {est_encontrado['regiao']}) (pressione Enter para manter): ") or est_encontrado['regiao']

        # Atualiza o dicionário diretamente na lista
        dados_estabelecimentos[index]['nome'] = nome
        dados_estabelecimentos[index]['email'] = email
        dados_estabelecimentos[index]['senha'] = senha
        dados_estabelecimentos[index]['endereco'] = endereco
        dados_estabelecimentos[index]['interesses'] = interesses
        dados_estabelecimentos[index]['bio'] = bio
        dados_estabelecimentos[index]['telefone'] = telefone
        dados_estabelecimentos[index]['regiao'] = regiao

        salvar_dados(estabelecimentos_json, dados_estabelecimentos) # Salva as alterações no arquivo JSON
        print("✅ Estabelecimento atualizado com sucesso.\n")

# Excluir Perfil
def excluir_perfil():
    """
    Permite excluir um perfil (usuário ou estabelecimento) existente.
    """
    tipo = tipo_de_perfil()
    id_input = input("Informe seu ID: ")
    try:
        id_ = int(id_input) # Converte o ID para inteiro
    except ValueError:
        print("❌ ID inválido. Deve ser um número inteiro.")
        return

    if tipo == "usuario":
        usuario_encontrado_index = -1
        # Encontra o índice do usuário pelo ID
        for i, usuario in enumerate(dados_usuarios):
            if usuario['id'] == id_:
                usuario_encontrado_index = i
                break

        if usuario_encontrado_index == -1:
            print("❌ Usuário não encontrado.")
            return

        confirm = input(f"⚠️ Tem certeza que deseja excluir o perfil de '{dados_usuarios[usuario_encontrado_index]['nome']}'? Isso é irreversível (s/n): ")
        if confirm.lower() == "s":
            del dados_usuarios[usuario_encontrado_index] # Remove o item da lista
            salvar_dados(usuarios_json, dados_usuarios) # Salva as alterações no arquivo JSON
            print("✅ Perfil excluído.")
        else:
            print("❌ Operação cancelada.")

    elif tipo == "estabelecimento":
        est_encontrado_index = -1
        # Encontra o índice do estabelecimento pelo ID
        for i, est in enumerate(dados_estabelecimentos):
            if est['id'] == id_:
                est_encontrado_index = i
                break

        if est_encontrado_index == -1:
            print("❌ Estabelecimento não encontrado.")
            return

        confirm = input(f"⚠️ Tem certeza que deseja excluir '{dados_estabelecimentos[est_encontrado_index]['nome']}'? Isso é irreversível (s/n): ")
        if confirm.lower() == "s":
            del dados_estabelecimentos[est_encontrado_index] # Remove o item da lista
            salvar_dados(estabelecimentos_json, dados_estabelecimentos) # Salva as alterações no arquivo JSON
            print("✅ Estabelecimento excluído.")
        else:
            print("❌ Operação cancelada.")

# Ver Dados
def ver_dados_por_id():
    """
    Exibe os dados de um perfil (usuário ou estabelecimento) específico pelo ID.
    """
    tipo = tipo_de_perfil()
    id_input = input("Informe seu ID: ")
    try:
        id_ = int(id_input) # Converte o ID para inteiro
    except ValueError:
        print("❌ ID inválido. Deve ser um número inteiro.")
        return

    if tipo == "usuario":
        # Usa next() com um gerador para encontrar o primeiro usuário com o ID, ou None se não encontrar
        u = next((usuario for usuario in dados_usuarios if usuario['id'] == id_), None)
        if u:
            # Acessa os dados usando chaves de dicionário
            print(f"ID: {u['id']} | Nome: {u['nome']} | Email: {u['email']} | Interesses: {', '.join(u['interesses'])} | Região: {u['regiao']}")
        else:
            print("❌ ID não encontrado.")

    elif tipo == "estabelecimento":
        # Usa next() com um gerador para encontrar o primeiro estabelecimento com o ID, ou None se não encontrar
        e = next((est for est in dados_estabelecimentos if est['id'] == id_), None)
        if e:
            # Acessa os dados usando chaves de dicionário
            print(f"ID: {e['id']} | Nome: {e['nome']} | Email: {e['email']} | Endereço: {e['endereco']} | Região: {e['regiao']}")
        else:
            print("❌ ID não encontrado.")

# Menus
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
        recomendar_estabelecimentos()
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
        print("❌ Opção inválida.")

    menu_principal() # Loop para voltar ao menu principal

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
            print("❌ Opção inválida.")


def recomendar_estabelecimentos():
    """
    Recomenda estabelecimentos com base nos interesses e região do usuário.
    """
    id_input = input("Informe seu ID: ")
    try:
        id_ = int(id_input) # Converte o ID para inteiro
    except ValueError:
        print("❌ ID inválido. Deve ser um número inteiro.")
        return

    # Encontra o usuário pelo ID
    u = next((usuario for usuario in dados_usuarios if usuario['id'] == id_), None)

    if not u:
        print('Usuario não encontrado')
        return
    
    # Interesses do usuário são agora uma lista de strings
    interesses_usuario = [i.strip().lower() for i in u['interesses']]
    regiao_usuario = u['regiao'].lower()
    estabelecimentos = dados_estabelecimentos # Já carregado globalmente

    # Lista onde vai ficar os matches do usuário com os estabelecimentos
    recomendados = []

    # Itera sobre os estabelecimentos para encontrar correspondências
    for estabelecimento in estabelecimentos:
        regiao_estabelecimento = estabelecimento['regiao'].lower()
        # Interesses do estabelecimento também são uma lista de strings
        interesses_estabelecimento = [i.lower() for i in estabelecimento['interesses']]

        if regiao_estabelecimento == regiao_usuario:
            # Encontra interesses em comum usando conjuntos (sets)
            interesses_em_comum = set(interesses_usuario) & set(interesses_estabelecimento)
            if interesses_em_comum:
                recomendados.append({
                    'nome': estabelecimento['nome'],
                    'interesses_em_comum': list(interesses_em_comum),
                    'regiao': regiao_estabelecimento
                })

    if not recomendados:
        print('\n⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘')
        print('\n(╥﹏╥) (╥﹏╥) (╥﹏╥) (╥﹏╥)')
        print("🥺 Não encontramos estabelecimentos compatíveis com seus interesses nessa região :( \nTente alterar seus interesses.")
        print('\n⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘')
        menu_principal() # Retorna ao menu principal
        return
    
    print('\n✦·┈๑⋅⋯ ⋯⋅๑┈·✦ ✦·┈๑⋅⋯ ⋯⋅๑┈·✦ ✦·┈๑⋅⋯ ⋯⋅๑┈·✦ ✦·┈๑⋅⋯ ⋯⋅๑┈·✦ ✦·┈๑⋅⋯ ⋯⋅๑┈·✦ ✦·┈๑⋅⋯ ⋯⋅๑┈·✦ ✦·┈๑⋅⋯ ⋯⋅๑┈·✦ ✦·┈๑⋅⋯ ⋯⋅๑┈·✦ ✦·┈๑⋅⋯ ⋯⋅๑┈·✦')
    print("\nEstabelecimentos recomendados com base em seus interesses: ")
    # Imprime o nome e os interesses em comum para cada estabelecimento recomendado
    for rec in recomendados:
        print(f"\n🔖 {rec['nome']}")
        print(f"💟 Interesses em comum: {', '.join(rec['interesses_em_comum'])}")
        print(f"🗺️  Região: {rec['regiao']}")

    print('✦·┈๑⋅⋯ ⋯⋅๑┈·✦ ✦·┈๑⋅⋯ ⋯⋅๑┈·✦ ✦·┈๑⋅⋯ ⋯⋅๑┈·✦ ✦·┈๑⋅⋯ ⋯⋅๑┈·✦ ✦·┈๑⋅⋯ ⋯⋅๑┈·✦ ✦·┈๑⋅⋯ ⋯⋅๑┈·✦ ✦·┈๑⋅⋯ ⋯⋅๑┈·✦ ✦·┈๑⋅⋯ ⋯⋅๑┈·✦ ✦·┈๑⋅⋯ ⋯⋅๑┈·✦')
    

def recomendacao_aleatoria():
    """
    Exibe uma lista de 3 estabelecimentos aleatórios.
    """
    print('\n──── ୨୧ ──────── ୨୧ ──────── ୨୧ ──────── ୨୧ ──────── ୨୧ ──────── ୨୧ ──────── ୨୧ ──────── ୨୧ ──────── ୨୧ ────')
    print('\nA vida é feita de novas experiências. Permita-se sair do óbvio e descubra lugares incríveis')
    
    if len(dados_estabelecimentos) < 3:
        print("🥺 Não há estabelecimentos suficientes para fazer uma recomendação aleatória (mínimo de 3).")
        print('\n──── ୨୧ ──────── ୨୧ ──────── ୨୧ ──────── ୨୧ ──────── ୨୧ ──────── ୨୧ ──────── ୨୧ ──────── ୨୧ ──────── ୨୧ ────')
        return

    # Seleciona 3 estabelecimentos aleatoriamente
    estabelecimentos_sorteados = random.sample(dados_estabelecimentos, k=3)
    for i in estabelecimentos_sorteados:
        print(f"\n 🔖 Nome: {i['nome']}")
        print(f"💟 Interesses: {', '.join(i['interesses'])}")
        print(f"🗺️  Região: {i['regiao']}")
        print(f"📍 Endereço: {i['endereco']}")
        print(f"📞 Telefone: {i['telefone']}")
        print(f"📖 Bio: {i['bio']}")
        print('﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌'*7)
    print('──── ୨୧ ──────── ୨୧ ──────── ୨୧ ──────── ୨୧ ──────── ୨୧ ──────── ୨୧ ──────── ୨୧ ──────── ୨୧ ──────── ୨୧ ────')


# Inicia o sistema chamando o menu inicial
menu_inicial()
