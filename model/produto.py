# model/produto.py

class Produto:
    
    # Método construtor da classe Produto
    def __init__(self, nome, categoria, preco, quantidade):
        # Inicializa os atributos do produto com os valores fornecidos
        self.nome = nome          # Nome do produto
        self.categoria = categoria  # Categoria do produto
        self.preco = preco        # Preço do produto
        self.quantidade = quantidade  # Quantidade disponível do produto

    # Método especial para representar o objeto Produto como uma string
    def __str__(self):
        # Retorna uma representação formatada do produto
        return f'{self.nome} | {self.categoria} | R${self.preco:.2f} | Estoque: {self.quantidade}'