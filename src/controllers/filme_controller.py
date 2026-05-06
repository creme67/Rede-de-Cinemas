from services.filme_service import FilmeService

class FilmeController:
    def __init__(self):
        self.service = FilmeService()

    def criar_filme(self, titulo, duracao, genero, elenco, diretor):
        try:
            filme = self.service.cadastrar_filme(titulo, duracao, genero, elenco, diretor)
            return f"Sucesso: Filme '{filme.titulo}' cadastrado com ID {filme.id}."
        except Exception as e:
            return f"Erro: {str(e)}"

    def obter_lista_filmes(self):
        return self.service.listar_filmes()
