# model/produto.py

class Produto:
    
    # Método construtor da classe Produto
    def __init__(self, nome, categoria, preco, quantidade):
        # Inicializa os atributos do produto como privados
        self._nome = nome          # Nome do produto
        self._categoria = categoria  # Categoria do produto
        self._preco = preco        # Preço do produto
        self._quantidade = quantidade  # Quantidade disponível do produto

    # Getter e Setter para nome
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome, str) and novo_nome.strip():
            self._nome = novo_nome
        else:
            raise ValueError("O nome deve ser uma string não vazia.")

    # Getter e Setter para categoria
    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, nova_categoria):
        if isinstance(nova_categoria, str) and nova_categoria.strip():
            self._categoria = nova_categoria
        else:
            raise ValueError("A categoria deve ser uma string não vazia.")

    # Getter e Setter para preco
    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, novo_preco):
        if isinstance(novo_preco, (int, float)) and novo_preco >= 0:
            self._preco = novo_preco
        else:
            raise ValueError("O preço deve ser um número positivo.")

    # Getter e Setter para quantidade
    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, nova_quantidade):
        if isinstance(nova_quantidade, int) and nova_quantidade >= 0:
            self._quantidade = nova_quantidade
        else:
            raise ValueError("A quantidade deve ser um número inteiro não negativo.")

    # Método especial para representar o objeto Produto como uma string
    def __str__(self):
        # Retorna uma representação formatada do produto
        return f'{self.nome} | {self.categoria} | €{self.preco:.2f} | Estoque: {self.quantidade}'