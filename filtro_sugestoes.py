'''
Interesses provisorios do usuario logado.
'''
interesses_usuario = ['Rock', 'Pop']

'''
lista de dicionario teste, onde cada dicionario é um estabelecimento
'''
estabelecimentos = [
    {'nome': 'Labubu', 'interesses': ['Rock', 'Metal']},
    {'nome': 'Taka', 'interesses': ['Pagode', 'Samba']},
    {'nome': 'MusicBox', 'interesses': ['Pop', 'Eletrônica']},
    {'nome': 'Casa da Música', 'interesses': ['Rock', 'Pop', 'MPB']},
]


'''
Função onde o 1 argumento é os interesses do usuario, e o 2 argumento é a lista de dicionarios dos estabelecimentos
'''
def recomendar_estabelecimentos(usuario_interesses, estabelecimentos):
    #Lista onde vai ficar os matchs do usuario com os estabelecimentos
    recomendados = []

    #for para separar os estabelecimentos
    for estabelecimento in estabelecimentos:
        '''
        #transforma a lista de interesses em set(conjuntos), pra poder usar &. 
        # Se tiver interesses em comuns entre o usuario e os estabelecimentos, ele vai adicionar em recomendados o nome do estabelecimento e os interesses em comum.
        '''
        interesses_em_comum = set(usuario_interesses) & set(estabelecimento['interesses'])
        if interesses_em_comum:
            recomendados.append({
                'nome': estabelecimento['nome'],
                'interesses_em_comum': list(interesses_em_comum)
            })
    return recomendados

#Chamando a função e inserindo os dados
recomendacoes = recomendar_estabelecimentos(interesses_usuario, estabelecimentos)

print("Estabelecimentos recomendados com base em seus interesses: ")
#Printar o nome e o interesses para cada item da lista (recomendacoes)
for rec in recomendacoes:
    print(f"{rec['nome']} - Interesses em comum: {', '.join(rec['interesses_em_comum'])}")
    #metodo .join pra juntar todos os elementos em uma unica string e separar eles com virgula