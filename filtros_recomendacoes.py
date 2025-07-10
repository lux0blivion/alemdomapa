import random
from utils import carregar_dados

usuarios_json = 'usuarios.json'
estabelecimentos_json = 'estabelecimentos.json'
dados_usuarios = carregar_dados(usuarios_json)
dados_estabelecimentos = carregar_dados(estabelecimentos_json)


def recomendar_estabelecimentos(user_logado):
    """
    Recomenda estabelecimentos com base nos interesses e região do usuário.
    """

    usuario = user_logado

    if not usuario:
        print('Usuario não encontrado')
        return
    
    interesses_usuario = [i.strip().lower() for i in usuario['interesses']]
    regiao_usuario = usuario['regiao'].lower()
    estabelecimentos = dados_estabelecimentos 

    recomendados = []

    for estabelecimento in estabelecimentos:
        regiao_estabelecimento = estabelecimento['regiao'].lower()
        interesses_estabelecimento = [i.lower() for i in estabelecimento['interesses']]

        if regiao_estabelecimento == regiao_usuario:
            interesses_em_comum = set(interesses_usuario) & set(interesses_estabelecimento)
            if interesses_em_comum:
                recomendados.append({
                    'nome': estabelecimento['nome'],
                    'interesses_em_comum': list(interesses_em_comum),
                    'regiao': regiao_estabelecimento,
                    'bio': estabelecimento['bio'],
                    'endereco': estabelecimento['endereco'],
                    'telefone': estabelecimento['telefone'],
                    'interesses': estabelecimento['interesses']
                })

    if not recomendados:
        print('\n⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘')
        print('\n(╥﹏╥) (╥﹏╥) (╥﹏╥) (╥﹏╥)')
        print("🥺 Não encontramos estabelecimentos compatíveis com seus interesses nessa região :( \nTente alterar seus interesses.")
        print('\n⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘')
        return
    
    print('\n✦·┈๑⋅⋯ ⋯⋅๑┈·✦ ✦·┈๑⋅⋯ ⋯⋅๑┈·✦ ✦·┈๑⋅⋯ ⋯⋅๑┈·✦ ✦·┈๑⋅⋯ ⋯⋅๑┈·✦ ✦·┈๑⋅⋯ ⋯⋅๑┈·✦ ✦·┈๑⋅⋯ ⋯⋅๑┈·✦ ✦·┈๑⋅⋯ ⋯⋅๑┈·✦ ✦·┈๑⋅⋯ ⋯⋅๑┈·✦ ✦·┈๑⋅⋯ ⋯⋅๑┈·✦')
    print("\nEstabelecimentos recomendados com base em seus interesses: ")
    for i, rec in enumerate(recomendados, start=1):
        print(f"\n🔖 {i}. {rec['nome']}")
        print(f"💟 Interesses em comum: {', '.join(rec['interesses_em_comum']).capitalize()}")
        print(f"🗺️  Região: {rec['regiao']}")

    indice_recomendado = int(input('\nPressione o indice de um estabelecimento para acessar a pagina dele: '))
    if  1 <= indice_recomendado <= len(recomendados):
        estabeleci_selecion = recomendados[indice_recomendado - 1]
        print(f"\n{estabeleci_selecion['nome']}")
        print(f"{estabeleci_selecion['bio']}")
        print(f"{', '.join(estabeleci_selecion['interesses']).title()}")
        print(f"{estabeleci_selecion['telefone']}")
        print(f"{estabeleci_selecion['endereco']}")
        
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