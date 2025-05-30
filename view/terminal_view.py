# view/terminal_view.py

import os

class TerminalView:

    # Método para exibir o menu de opções para o usuário
    def mostrar_menu(self):
        print("\n========= MENU =========")
        print("1. Adicionar Produto")  # Opção para adicionar um novo produto
        print("2. Listar Produtos")   # Opção para listar todos os produtos
        print("3. Atualizar Produtos") # Opção para atualizar a quantidade de um produto existente
        print("4. Remover Produto")   # Opção para remover um produto 
        print("5. Sair")               # Opção para sair do programa
        print("========================")

    # Método para exibir o menu de opções para o usuário alterar as deevidas informações
    def menu_atualizar_info(self):
        print("\n=== MENU DE ALTERAÇÃO ===")
        print("1. Atualizar Quantidade em Stock")  
        print("2. Atualizar Preço do Produto")   
        print("3. Atualizar Nome do Produto") 
        print("4. Sair")            
        print("========================")

    # Método para exibir a lista de produtos
    def mostrar_produtos(self, produtos):
        for p in produtos:  # Itera sobre cada produto na lista
            print(p)        # Exibe o produto

    # Método para solicitar os dados de um novo produto ao usuário
    def pedir_dados_produto(self):
        nome = input("Nome do produto: ")          # Solicita o nome do produto
        categoria = input("Categoria: ")            # Solicita a categoria do produto
        preco = float(input("Preço: €"))           # Solicita o preço do produto e converte para float
        quantidade = int(input("Quantidade: "))     # Solicita a quantidade do produto e converte para int
        return nome, categoria, preco, quantidade    # Retorna os dados do produto como uma tupla
    
    # Método para solicitar o nome do produto que o usuário deseja atualizar
    def pedir_nome_produto(self):
        return input("Nome do produto que deseja atualizar: ")  # Retorna o nome do produto
    
    # Método para solicitar o nome do produto que o usuário deseja remover
    def pedir_nome_produto_remover(self):
        return input("Nome do produto que deseja remover: ") # Retorna o nome do produto

    # Método para solicitar a nova quantidade do produto ao usuário
    def pedir_nova_quantidade(self):
        return int(input("Nova quantidade: "))  # Solicita a nova quantidade e converte para int
    
    def pedir_novo_preco(self):
        return float(input("Novo preço: "))
    
    def pedirNovoNome(self):
        return input("Novo nome do produto: ")
    
    # Método para limpar o terminal
    def limparTerminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')