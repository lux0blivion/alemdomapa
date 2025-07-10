import json
def carregar_dados(caminho):
    """
    Carrega dados de um arquivo JSON.
    Se o arquivo não for encontrado ou estiver vazio/inválido, retorna uma lista vazia.
    """
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao carregar '{caminho}': {e}")
        return []

def salvar_dados(caminho, dados):
    """
    Reescreve o conteudo de um arquivo JSON caso ja tenha dados, se não, cria o conteudo.
    """
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)


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
        print(" Tipo inválido. Tente novamente.\n")
        return tipo_de_perfil()