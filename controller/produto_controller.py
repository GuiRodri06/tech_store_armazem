# controller/produto_controller.py

# Importa as classes Estoque e Produto
from model.estoque import Estoque
from model.produto import Produto

class ProdutoController:
    
    # Método construtor da classe ProdutoController
    def __init__(self):
        # Cria uma instância da classe Estoque para gerenciar os produtos
        self.estoque = Estoque()

    # Método para adicionar um novo produto ao estoque
    def adicionar_produto(self, nome, categoria, preco, quantidade):
        # Cria uma nova instância da classe Produto com os dados fornecidos
        produto = Produto(nome, categoria, preco, quantidade)
        # Adiciona o produto ao estoque
        self.estoque.adicionar_produto(produto)

    # Método para listar todos os produtos no estoque
    def listar_produtos(self):
        # Retorna a lista de produtos do estoque
        return self.estoque.listar_produtos()

    # Método para atualizar a quantidade de um produto existente
    def atualizar_produto(self, nome, nova_quantidade):
        # Obtém a lista de produtos do estoque
        produtos = self.estoque.listar_produtos()
        # Itera sobre cada produto na lista
        for p in produtos:
            # Verifica se o nome do produto corresponde ao nome fornecido
            if p.nome == nome:
                # Atualiza a quantidade do produto no estoque
                self.estoque.atualizar_estoque(p, nova_quantidade)
                break  # Interrompe o loop após atualizar o produto