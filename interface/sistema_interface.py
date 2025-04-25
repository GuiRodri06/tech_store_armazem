from abc import ABC, abstractmethod

# Interface para gerenciamento de produto
class SistemaInterface(ABC):

    @abstractmethod
    def adicionar_produto(self, nome, categoria, preco, quantidade): pass

    @abstractmethod
    def listar_produtos(self): pass

    @abstractmethod
    def atualizar_produto(self, nome, nova_quantidade): pass

    @abstractmethod
    def remover_produto(self, nome): pass