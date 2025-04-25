# model/estoque.py

# Importa o módulo sqlite3 para manipulação de banco de dados SQLite
import sqlite3
# Importa a classe Produto, que representa um produto no estoque
from model.produto import Produto

class Estoque:
    # Método construtor da classe Estoque
    def __init__(self, db_path="db/armazem.db"):
        # Define o caminho do banco de dados
        self.db_path = db_path
        # Chama o método para criar a tabela de produtos no banco de dados
        self.criar_tabela()

    # Método para criar a tabela de produtos no banco de dados
    def criar_tabela(self):
        # Conecta ao banco de dados
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        # Executa a instrução SQL para criar a tabela, se ela não existir
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                categoria TEXT,
                preco REAL,
                quantidade INTEGER
            )
        ''')
        # Salva as alterações no banco de dados
        conn.commit()
        # Fecha a conexão com o banco de dados
        conn.close()

    # Método para adicionar um novo produto ao banco de dados
    def adicionar_produto(self, produto):
        # Conecta ao banco de dados
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        # Executa a instrução SQL para inserir um novo produto na tabela
        cursor.execute('''
            INSERT INTO produtos (nome, categoria, preco, quantidade) 
            VALUES (?, ?, ?, ?)
        ''', (produto.nome, produto.categoria, produto.preco, produto.quantidade))
        # Salva as alterações no banco de dados
        conn.commit()
        # Fecha a conexão com o banco de dados
        conn.close()

    # Método para listar todos os produtos no banco de dados
    def listar_produtos(self):
        # Conecta ao banco de dados
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        # Executa a instrução SQL para selecionar todos os produtos
        cursor.execute('SELECT * FROM produtos')
        produtos = cursor.fetchall()  # Obtém todos os resultados da consulta
        # Fecha a conexão com o banco de dados
        conn.close()

        # Retorna uma lista de instâncias de Produto, criando um para cada linha retornada
        return [Produto(nome=p[1], categoria=p[2], preco=p[3], quantidade=p[4]) for p in produtos]
    
    # Método para atualizar a quantidade de um produto no banco de dados
    def atualizar_estoque(self, produto, quantidade):
        # Conecta ao banco de dados
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        # Executa a instrução SQL para atualizar a quantidade do produto
        cursor.execute('''
            UPDATE produtos
            SET quantidade = ?
            WHERE nome = ?
        ''', (quantidade, produto.nome))
        # Salva as alterações no banco de dados
        conn.commit()
        # Fecha a conexão com o banco de dados
        conn.close()