# model/estoque.py

import sqlite3 # Importa o módulo sqlite

from model.produto import Produto # Importa a classe Produto

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
        
        conn.commit() # Salva as alterações no banco de dados
        
        conn.close() # Fecha a conexão com o banco de dados

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

        conn.commit() # Salva as alterações no banco de dados
        conn.close() # Fecha a conexão com o banco de dados

    # Método para listar todos os produtos no banco de dados
    def listar_produtos(self):
        # Conecta ao banco de dados
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Executa a instrução SQL para selecionar todos os produtos
        cursor.execute('SELECT * FROM produtos')
        produtos = cursor.fetchall()  # Obtém todos os resultados da consulta
        
        conn.close() # Fecha a conexão com o banco de dados

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
 
        conn.commit() # Salva as alterações no banco de dados
        conn.close() # Fecha a conexão com o banco de dados

    def atualizarPrecoEstoque(self, produto, preco):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
                       UPDATE produtos
                       SET preco = ?
                       WHERE nome = ?
                       ''', (preco, produto.nome))
        
        conn.commit()
        conn.close()

    def atualizarNomeEstoque(self, produto, nome):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
                       UPDATE produtos
                       SET nome = ?
                       WHERE nome = ?
                       ''', (nome, produto.nome))
        
        conn.commit()
        conn.close()

    # Método para remover um produto do banco de dados
    def remover_produto(self, produto):
        # Conecta ao banco de dados
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Executa a instrução SQL para remover o produto
        cursor.execute('''
            DELETE FROM produtos
            WHERE nome = ?
        ''', (produto,))
        
        conn.commit() # Salva as alterações no banco de dados
        conn.close() # Fecha a conexão com o banco de dados

    def buscar_produto_por_nome(self, nome):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM produtos WHERE nome = ?', (nome,))
        produto = cursor.fetchone()
        conn.close()
        if produto:
            return Produto(nome=produto[1], categoria=produto[2], preco=produto[3], quantidade=produto[4])
        return None