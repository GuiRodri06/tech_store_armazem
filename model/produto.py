# model/produto.py

class Produto:
    
    # Método construtor da classe Produto
    def __init__(self, nome, categoria, preco, quantidade):
        # Inicializa os atributos do produto como privados
        self.__nome = nome          # Nome do produto
        self.__categoria = categoria  # Categoria do produto
        self.__preco = preco        # Preço do produto
        self.__quantidade = quantidade  # Quantidade disponível do produto

    # Getters
    @property
    def nome(self):
        return self.__nome

    @property
    def categoria(self):
        return self.__categoria

    @property
    def preco(self):
        return self.__preco

    @property
    def quantidade(self):
        return self.__quantidade

    # Setters
    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome, str) and novo_nome.strip():
            self.__nome = novo_nome
        else:
            raise ValueError("O nome deve ser uma string não vazia.")

    @categoria.setter
    def categoria(self, nova_categoria):
        if isinstance(nova_categoria, str) and nova_categoria.strip():
            self.__categoria = nova_categoria
        else:
            raise ValueError("A categoria deve ser uma string não vazia.")

    @preco.setter
    def preco(self, novo_preco):
        if isinstance(novo_preco, (int, float)) and novo_preco >= 0:
            self.__preco = novo_preco
        else:
            raise ValueError("O preço deve ser um número positivo.")

    @quantidade.setter
    def quantidade(self, nova_quantidade):
        if isinstance(nova_quantidade, int) and nova_quantidade >= 0:
            self.__quantidade = nova_quantidade
        else:
            raise ValueError("A quantidade deve ser um número inteiro não negativo.")

    # Método especial para representar o objeto Produto como uma string
    def __str__(self):
        # Retorna uma representação formatada do produto
        return f'{self.nome} | {self.categoria} | €{self.preco:.2f} | Estoque: {self.quantidade}'