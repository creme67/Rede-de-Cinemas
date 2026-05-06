from models.filme import Filme
from repositories.filme_repository import FilmeRepository

class FilmeService:
    def __init__(self):
        self.repository = FilmeRepository()

    def cadastrar_filme(self, titulo, duracao, genero, elenco, diretor):
        # Regra de Negócio: Título é obrigatório e duração deve ser positiva
        if not titulo:
            raise ValueError("O título do filme é obrigatório.")
        if duracao <= 0:
            raise ValueError("A duração deve ser maior que zero.")
        
        novo_filme = Filme(titulo=titulo, duracao=duracao, genero=genero, elenco=elenco, diretor=diretor)
        return self.repository.salvar(novo_filme)

    def listar_filmes(self):
        return self.repository.listar_todos()
