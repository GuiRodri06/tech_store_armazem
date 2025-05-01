from abc import ABC, abstractmethod

# Interface para gerenciamento de produto
class SistemaInterface(ABC):

    @abstractmethod
    def adicionar_produto(self, nome, categoria, preco, quantidade): pass

    @abstractmethod
    def listar_produtos(self): pass

    @abstractmethod
    def atualizarQuantidade(self, nome, nova_quantidade): pass

    @abstractmethod
    def atualizarPreco(self, nome, novoPreco): pass

    @abstractmethod
    def atualizarNome(self, nome, novoNome): pass
    
    @abstractmethod
    def remover_produto(self, nome): pass

    @abstractmethod
    def buscar_produto(self, nome): pass