
class Perfil:
    def __init__(self, id, nome, email, senha, interesses, regiao):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.interesses = interesses
        self.regiao = regiao

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
            "interesses": self.interesses,
            "regiao": self.regiao
        }

class Usuario(Perfil):
    pass  

class Estabelecimento(Perfil):
    def __init__(self, id, nome, email, senha, interesses, regiao, endereco, telefone, bio, avaliacoes=None):
        super().__init__(id, nome, email, senha, interesses, regiao)
        self.endereco = endereco
        self.telefone = telefone
        self.bio = bio
        self.avaliacoes = avaliacoes if avaliacoes is not None else []

    def adicionar_avaliacao(self, nota):
        if 1 <= nota <= 5:
            self.avaliacoes.append(nota)

    def media_avaliacoes(self):
        if not self.avaliacoes:
            return 0
        return round(sum(self.avaliacoes) / len(self.avaliacoes), 2)

    def to_dict(self):
        dados = super().to_dict()
        dados.update({
            "endereco": self.endereco,
            "telefone": self.telefone,
            "bio": self.bio,
            "avaliacoes": self.avaliacoes
        })
        return dados

