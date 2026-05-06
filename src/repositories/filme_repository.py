import sqlite3
from models.filme import Filme

class FilmeRepository:
    def __init__(self, db_path="cinema.db"):
        self.db_path = db_path
        self._criar_tabela()

    def _criar_tabela(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS filmes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    duracao INTEGER,
                    genero TEXT,
                    elenco TEXT,
                    diretor TEXT
                )
            """)

    def salvar(self, filme: Filme):
        query = "INSERT INTO filmes (titulo, duracao, genero, elenco, diretor) VALUES (?, ?, ?, ?, ?)"
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query, (filme.titulo, filme.duracao, filme.genero, filme.elenco, filme.diretor))
            filme.id = cursor.lastrowid
        return filme

    def listar_todos(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM filmes")
            rows = cursor.fetchall()
            return [Filme(*row) for row in rows]
