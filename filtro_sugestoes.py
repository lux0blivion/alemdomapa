'''
Interesses provisorios do usuario logado.
'''
interesses_usuario = ['rock', 'pop', 'vinil']
regiao_usuario = ['recife']

'''
lista de dicionario teste, onde cada dicionario é um estabelecimento
'''
estabelecimentos = [
    {'nome': 'Labubu', 'interesses': ['Rock', 'Metal'], 'regiao': 'recife'},
    {'nome': 'Taka', 'interesses': ['Pagode', 'Samba'], 'regiao': 'paulista'},
    {'nome': 'MusicBox', 'interesses': ['Pop', 'Eletrônica'], 'regiao': 'olinda'},
    {'nome': 'Casa da Música', 'interesses': ['Rock', 'Pop', 'MPB'], 'regiao': 'recife'},
]


def recomendar_estabelecimentos(usuario_interesses, usuario_regiao, estabelecimentos):
    #Lista onde vai ficar os matchs do usuario com os estabelecimentos
    recomendados = []

    usuario_interesses = [interesse.lower() for interesse in usuario_interesses]
    usuario_regiao = usuario_regiao[0].lower()

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
    return recomendados

#Chamando a função e inserindo os dados
recomendacoes = recomendar_estabelecimentos(interesses_usuario, regiao_usuario, estabelecimentos)

print("Estabelecimentos recomendados com base em seus interesses: ")
#Printar o nome e o interesses para cada item da lista (recomendacoes)
for rec in recomendacoes:
    print(f"{rec['nome']} - Interesses em comum: {', '.join(rec['interesses_em_comum'])} - Região: {rec['regiao']}")
 