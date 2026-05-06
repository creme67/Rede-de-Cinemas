from dataclasses import dataclass

@dataclass
class Filme:
    id: int = None
    titulo: str = ""
    duracao: int = 0
    genero: str = ""
    elenco: str = ""
    diretor: str = ""
