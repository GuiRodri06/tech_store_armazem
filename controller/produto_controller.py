# controller/produto_controller.py

# Importa as classes Estoque e Produto
from model.estoque import Estoque
from model.produto import Produto
from interface.sistema_interface import SistemaInterface
from rapidfuzz import process

class ProdutoController(SistemaInterface):

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
    def atualizarQuantidade(self, nome, nova_quantidade):
        # Obtém a lista de produtos do estoque
        produtos = self.estoque.listar_produtos()
        # Itera sobre cada produto na lista
        for p in produtos:
            # Verifica se o nome do produto corresponde ao nome fornecido
            if p.nome == nome:
                # Atualiza a quantidade do produto no estoque
                self.estoque.atualizar_estoque(p, nova_quantidade)
                break  # Interrompe o loop após atualizar o produto

    def atualizarPreco(self, nome, novoPreco):
        produtos = self.estoque.listar_produtos()
        for p in produtos: 
            if p.nome == nome:
                self.estoque.atualizarPrecoEstoque(p, novoPreco)
                break

    def atualizarNome(self, nome, novoNome): 
        produtos = self.estoque.listar_produtos()
        for p in produtos: 
            if p.nome == nome:
                self.estoque.atualizarNomeEstoque(p, novoNome)
                break

    # Método para remover um produto ao estoque
    def remover_produto(self, nome):
        # Remove o produto
        return self.estoque.remover_produto(nome)
    
    # Busca aproximada via fuzzy matching
    def buscar_produtos_fuzzy(self, termo, limite=5):
        termo = termo.strip().lower()
        produtos = self.estoque.listar_produtos()
        nomes = [produto.nome.strip().lower() for produto in produtos]
        matches = process.extract(termo, nomes, limit=limite, score_cutoff=60)
        resultados = []
        for nome, score, index in matches:
            resultados.append(produtos[index])
        return resultados
    
    def buscar_produto_por_nome(self, nome):
        return self.estoque.buscar_produto_por_nome(nome)
    
    def atualizarCategoria(self, nome_antigo, nova_categoria):
        produto = self.estoque.buscar_produto_por_nome(nome_antigo)
        if produto:
            self.estoque.atualizarCategoriaEstoque(produto, nova_categoria)