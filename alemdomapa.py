import sqlite3
import re
import json

estabelecimentos_json = 'lista_estabelecimentos.json'
dados_estabelecimentos = []
try:
    with open(estabelecimentos_json, 'r', encoding='utf-8') as arquivo:
        #Ler o dados do json e coloca na variavel estabelecimentos_json
        dados_estabelecimentos = json.load(arquivo)

except FileNotFoundError:
    print(f"Erro: O arquivo '{estabelecimentos_json}' não foi encontrado. Verifique o nome e o caminho do arquivo.")
except json.JSONDecodeError:
    print(f"Erro: O arquivo '{estabelecimentos_json}' não contém um JSON válido.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")

# banco de dados
conn = sqlite3.connect("alem_do_mapa.db")
cursor = conn.cursor()

# tabelas com as estruturas atualizadas
cursor.execute("DROP TABLE IF EXISTS usuarios")
cursor.execute("DROP TABLE IF EXISTS estabelecimentos")

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL,
    interesses TEXT NOT NULL,
    regiao TEXT NOT NULL)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS estabelecimentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL,
    endereco TEXT NOT NULL,
    interesses TEXT NOT NULL,
    bio TEXT NOT NULL,
    telefone TEXT NOT NULL,
    regiao TEXT NOT NULL
)
""")
conn.commit()

#  Funções de Validação 
def email_valido(email):
    email = email.strip()
    if ' ' in email:
        return False
    padrao = r'^[\w\.-]+@(gmail\.com|hotmail\.com)$'
    return re.match(padrao, email)

def senha_valida(senha):
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
    return telefone.isdigit() and len(telefone) == 11

#  Funções Auxiliares 
def tipo_de_perfil():
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

#  Cadastro 
def criar_usuario():
    print("=== Cadastro de Usuário ===")
    nome = input("Nome: ")

    while True:
        email = input("Email (@gmail.com ou @hotmail.com, sem espaços): ")
        if not email_valido(email):
            print("❌ Email inválido.")
        else:
            break

    while True:
        senha = input("Senha (8+ caracteres, letras, números, sem espaços): ")
        if not senha_valida(senha):
            print("❌ Senha inválida.")
        else:
            break
    print("""
    * Alternativo        * Forró              * Popular           
    * Ao Vivo            * Futebol            * Regional          
    * Ar Livre           * Geek               * Rock              
    * Arte               * Grupos             * Samba             
    * Artesanal          * Happy Hour         * Saudável          
    * Balada             * Íntimo             * Sertanejo         
    * Boteco             * Jazz               * Sinuca            
    * Café               * Jogos              * Sucos             
    * Comédia            * Karaokê            * Temático          
    * Cultural           * LGBT               * Tranquilo         
    * Dança              * MPB                * Vegano            
    * DJ                 * Pet-Friendly       * Vinil             
    * Drinks             * Petiscos           * Vinhos            
    * Eletrônico         * Pop                * Vista   
    """)
    print("Escolha seus interesses (três):")
    i1 = input("Digite seu primeiro interesse: ")
    i2 = input("Digite seu segundo interesse: ")
    i3 = input("Digite seu terceiro interesse: ")
    interesses = f"{i1}, {i2}, {i3}"

    while True:
        regiao = input("Região (formato: Cidade - Estado): ")
        if ' - ' not in regiao or len(regiao.split(' - ')) != 2:
            print("❌ Formato inválido. Ex: Recife - Pernambuco")
        else:
            break

    try:
        cursor.execute("INSERT INTO usuarios (nome, email, senha, interesses, regiao) VALUES (?, ?, ?, ?, ?)",
                       (nome, email, senha, interesses, regiao))
        conn.commit()
        cursor.execute("SELECT last_insert_rowid()")
        novo_id = cursor.fetchone()[0]
        print(f"✅ Usuário cadastrado! Seu ID é: {novo_id}\nUse esse ID para atualizar ou excluir seu perfil.")
    except sqlite3.IntegrityError:
        print("❌ Este email já está cadastrado.\n")

def criar_estabelecimento():
    print("=== Cadastro de Estabelecimento ===")
    nome = input("Nome: ")

    while True:
        email = input("Email (@gmail.com ou @hotmail.com, sem espaços): ")
        if not email_valido(email):
            print("❌ Email inválido.")
        else:
            break

    while True:
        senha = input("Senha (8+ caracteres, letras, números, sem espaços): ")
        if not senha_valida(senha):
            print("❌ Senha inválida.")
        else:
            break

    endereco = input("Endereço: ")

    print("Informe os interesses do estabelecimento (três)")
    i1 = input("Digite seu primeiro interesse: ")
    i2 = input("Digite seu segundo interesse: ")
    i3 = input("Digite seu terceiro interesse: ")
    interesses = f"{i1}, {i2}, {i3}"

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

    try:
        cursor.execute("""
            INSERT INTO estabelecimentos (nome, email, senha, endereco, interesses, bio, telefone, regiao)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (nome, email, senha, endereco, interesses, bio, telefone, regiao))
        conn.commit()
        cursor.execute("SELECT last_insert_rowid()")
        novo_id = cursor.fetchone()[0]
        print(f"✅ Estabelecimento cadastrado! Seu ID é: {novo_id}\nUse esse ID para atualizar ou excluir seu perfil.")
    except sqlite3.IntegrityError:
        print("❌ Este email já está cadastrado.\n")

#  Atualizar Perfil 
def atualizar_perfil():
    tipo = tipo_de_perfil()
    id_ = input("Informe seu ID: ")

    if tipo == "usuario":
        cursor.execute("SELECT * FROM usuarios WHERE id=?", (id_,))
        pessoa = cursor.fetchone()
        if not pessoa:
            print("❌ Usuário não encontrado.")
            return

        nome = input("Novo nome (pressione Enter para manter e passar para o próximo): ") or pessoa[1]
        email = input("Novo email (pressione Enter para manter e passar para o próximo): ") or pessoa[2]
        senha = input("Nova senha (pressione Enter para manter e passar para o próximo): ") or pessoa[3]
        interesses = input("Novos interesses (pressione Enter para manter e passar para o próximo): ") or pessoa[4]
        regiao = input("Nova região (pressione Enter para manter): ") or pessoa[5]

        cursor.execute("""
        UPDATE usuarios SET nome=?, email=?, senha=?, interesses=?, regiao=? WHERE id=?
        """, (nome, email, senha, interesses, regiao, id_))
        conn.commit()
        print("✅ Perfil atualizado com sucesso.\n")

    elif tipo == "estabelecimento":
        cursor.execute("SELECT * FROM estabelecimentos WHERE id=?", (id_,))
        est = cursor.fetchone()
        if not est:
            print("❌ Estabelecimento não encontrado.")
            return

        nome = input("Novo nome (pressione Enter para manter): ") or est[1]
        email = input("Novo email (pressione Enter para manter): ") or est[2]
        senha = input("Nova senha (pressione Enter para manter): ") or est[3]
        endereco = input("Novo endereço (pressione Enter para manter): ") or est[4]
        interesses = input("Novos interesses (pressione Enter para manter): ") or est[5]
        bio = input("Nova bio (pressione Enter para manter): ") or est[6]
        telefone = input("Novo telefone (pressione Enter para manter): ") or est[7]
        regiao = input("Nova região (pressione Enter para manter): ") or est[8]

        cursor.execute("""
        UPDATE estabelecimentos
        SET nome=?, email=?, senha=?, endereco=?, interesses=?, bio=?, telefone=?, regiao=? WHERE id=?
        """, (nome, email, senha, endereco, interesses, bio, telefone, regiao, id_))
        conn.commit()
        print("✅ Estabelecimento atualizado com sucesso.\n")

#  Excluir Perfil 
def excluir_perfil():
    tipo = tipo_de_perfil()
    id_ = input("Informe seu ID: ")

    if tipo == "usuario":
        cursor.execute("SELECT * FROM usuarios WHERE id=?", (id_,))
        pessoa = cursor.fetchone()
        if not pessoa:
            print("❌ Usuário não encontrado.")
            return

        confirm = input(f"⚠️ Tem certeza que deseja excluir o perfil de '{pessoa[1]}'? Isso é irreversível (s/n): ")
        if confirm.lower() == "s":
            cursor.execute("DELETE FROM usuarios WHERE id=?", (id_,))
            conn.commit()
            print("✅ Perfil excluído.")
        else:
            print("❌ Operação cancelada.")

    elif tipo == "estabelecimento":
        cursor.execute("SELECT * FROM estabelecimentos WHERE id=?", (id_,))
        est = cursor.fetchone()
        if not est:
            print("❌ Estabelecimento não encontrado.")
            return

        confirm = input(f"⚠️ Tem certeza que deseja excluir '{est[1]}'? Isso é irreversível (s/n): ")
        if confirm.lower() == "s":
            cursor.execute("DELETE FROM estabelecimentos WHERE id=?", (id_,))
            conn.commit()
            print("✅ Estabelecimento excluído.")
        else:
            print("❌ Operação cancelada.")

#  Ver Dados 
def ver_dados_por_id():
    tipo = tipo_de_perfil()
    id_ = input("Informe seu ID: ")

    if tipo == "usuario":
        cursor.execute("SELECT * FROM usuarios WHERE id=?", (id_,))
        u = cursor.fetchone()
        if u:
            print(f"ID: {u[0]} | Nome: {u[1]} | Email: {u[2]} | Interesses: {u[4]} | Região: {u[5]}")
        else:
            print("❌ ID não encontrado.")

    elif tipo == "estabelecimento":
        cursor.execute("SELECT * FROM estabelecimentos WHERE id=?", (id_,))
        e = cursor.fetchone()
        if e:
            print(f"ID: {e[0]} | Nome: {e[1]} | Email: {e[2]} | Endereço: {e[4]} | Região: {e[8]}")
        else:
            print("❌ ID não encontrado.")

# Menus 
def menu_principal():
    print("\n=== MENU PRINCIPAL ===")
    print("1. Ir para área de sugestões")
    print("2. Atualizar dados do perfil")
    print("3. Excluir Perfil")
    print("4. Ver meus dados")
    print("5. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        recomendar_estabelecimentos()
    elif escolha == "2":
        atualizar_perfil()
    elif escolha == "3":
        excluir_perfil()
    elif escolha == "4":
        ver_dados_por_id()
    elif escolha == "5":
        print("Saindo...")
        exit()
    else:
        print("❌ Opção inválida.")

    menu_principal()

def menu_inicial():
    print("=== MENU INICIAL ===")
    print("1. Cadastrar Usuário")
    print("2. Cadastrar Estabelecimento")
    print("3. Login (em breve)")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        criar_usuario()
        menu_principal()
    elif escolha == "2":
        criar_estabelecimento()
        menu_principal()
    elif escolha == "3":
        print("Funcionalidade de login em desenvolvimento.")
    else:
        print("❌ Opção inválida.")
        menu_inicial()




def recomendar_estabelecimentos():
    id_ = input("Informe seu ID: ")
    cursor.execute("SELECT * FROM usuarios WHERE id=?", (id_,))
    u = cursor.fetchone()

    if not u:
        print('Usuario não encontrado')
        return
    #formatação da string, para uma lista separando os itens com a virgula
    interesses_usuario = [i.strip().lower() for i in u[4].split(',')]
    regiao_usuario = u[5].lower()
    estabelecimentos = dados_estabelecimentos

    #Lista onde vai ficar os matchs do usuario com os estabelecimentos
    recomendados = []

    usuario_interesses = [interesse.lower() for interesse in interesses_usuario]
    usuario_regiao = regiao_usuario.lower()

    #for para separar os estabelecimentos
    for estabelecimento in estabelecimentos:

        regiao_estabelecimento = estabelecimento['regiao'].lower()
        interesses_estabelecimento = [i.lower() for i in estabelecimento['interesses']]


        if regiao_estabelecimento == usuario_regiao:
            interesses_em_comum = set(usuario_interesses) & set(interesses_estabelecimento)
            if interesses_em_comum:
                recomendados.append({
                    'nome': estabelecimento['nome'],
                    'interesses_em_comum': list(interesses_em_comum),
                    'regiao': regiao_estabelecimento
                })


    if not recomendados:
        print("Não encontramos estabelecimentos compatives com seus interesses nessa região :( \nTente alterar seus interesses.")
        return
    
    print("\nEstabelecimentos recomendados com base em seus interesses: ")
    #Printar o nome e o interesses para cada item da lista (recomendacoes)
    for rec in recomendados:
        print(f"\n{rec['nome']}")
        print(f"Interesses em comum: {', '.join(rec['interesses_em_comum'])}")
        print(f"Região: {rec['regiao']}")

 


# Inicia o sistema
menu_inicial()
conn.close()