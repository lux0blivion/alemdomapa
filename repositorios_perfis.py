
import json
from modelos_perfis import Usuario, Estabelecimento

class RepositorioPerfis:
    def __init__(self, caminho_usuarios, caminho_estabelecimentos):
        self.caminho_usuarios = caminho_usuarios
        self.caminho_estabelecimentos = caminho_estabelecimentos
        self.usuarios = self._carregar(caminho_usuarios, Usuario)
        self.estabelecimentos = self._carregar(caminho_estabelecimentos, Estabelecimento)

    def _carregar(self, caminho, classe):
        try:
            with open(caminho, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                return [classe(**d) for d in dados]
        except:
            return []

    def salvar_tudo(self):
        with open(self.caminho_usuarios, 'w', encoding='utf-8') as f:
            json.dump([u.to_dict() for u in self.usuarios], f, ensure_ascii=False, indent=4)
        with open(self.caminho_estabelecimentos, 'w', encoding='utf-8') as f:
            json.dump([e.to_dict() for e in self.estabelecimentos], f, ensure_ascii=False, indent=4)

    def gerar_novo_id(self, lista):
        return max((p.id for p in lista), default=0) + 1
