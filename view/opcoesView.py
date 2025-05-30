# view/opcoesView.py

# Importa os módulos necessários para manipulação de caminhos e sistema
import sys
import os
import time

# Adiciona o diretório pai ao sys.path para que os módulos possam ser importados corretamente
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controller.produto_controller import ProdutoController # Importa a classe ProdutoController
from view.terminal_view import TerminalView # Importa a classe TerminalView

class OpcoesView: 

    def opcoesMenu(self): 

        controller = ProdutoController() # Cria uma instância do controlador de produtos
        view = TerminalView() # Cria uma instância da visualização do terminal

        # Inicia um loop infinito para o menu principal
        while True:
            # Exibe o menu de opções para o usuário
            view.mostrar_menu()
            
            opcao = input("Escolha uma opção: ")

            print("========================\n")

            view.limparTerminal()

            # Se o usuário escolher a opção 1
            if opcao == "1":

                print("==== CADASTRO DE NOVO PRODUTO ====")
                # Solicita os dados do produto (nome, categoria, preço e quantidade)
                nome, categoria, preco, quantidade = view.pedir_dados_produto()
                # Adiciona o produto usando o controlador
                controller.adicionar_produto(nome, categoria, preco, quantidade)
                print("==================================")
                print("Produto Novo Cadastrado com Sucesso")
                print("==================================")
                time.sleep(2.5)
                view.limparTerminal()

            # Se o usuário escolher a opção 2
            elif opcao == "2":
                print("================ PRODUTOS NO STOCK ================")
                # Obtém a lista de produtos do controlador
                produtos = controller.listar_produtos()
                # Exibe a lista de produtos na visualização
                view.mostrar_produtos(produtos)
                print("===================================================")

            # Se o usuário escolher a opção 3
            elif opcao == "3":
                
                while True: 

                    print("================ PRODUTOS NO STOCK ================")
                    # Obtém a lista de produtos do controlador
                    produtos = controller.listar_produtos()
                    # Exibe a lista de produtos na visualização
                    view.mostrar_produtos(produtos)
                    print("===================================================")

                    view.menu_atualizar_info()
                    opcaoAtualizar = input("Escolha uma opção: ")
                    print("========================\n")

                    if opcaoAtualizar == "1":
                        # Solicita o nome do produto que o usuário deseja atualizar
                        nome = view.pedir_nome_produto()
                        # Solicita a nova quantidade para o produto
                        nova_quantidade = view.pedir_nova_quantidade()
                        # Atualiza a quantidade do produto usando o controlador
                        controller.atualizarQuantidade(nome, nova_quantidade)
                    
                    elif opcaoAtualizar == "2":
                        nome = view.pedir_nome_produto()
                        novoPreco = view.pedir_novo_preco()
                        controller.atualizarPreco(nome, novoPreco)
                        view.limparTerminal()

                    elif opcaoAtualizar == "3":
                        nome = view.pedir_nome_produto()
                        novoNome = view.pedirNovoNome()
                        controller.atualizarNome(nome, novoNome)
                        view.limparTerminal()

                    elif opcaoAtualizar == "4":
                        view.limparTerminal()
                        break   

            # Se o usuário escolher a opção 4
            elif opcao == "4":
                # Solicita o nome do produto que o usuário deseja remover
                nome = view.pedir_nome_produto_remover()
                # Remove o produto usando o controlador
                controller.remover_produto(nome)

            # Se o usuário escolher a opção 4
            elif opcao == "5":
                print("============================")
                print("     Saindo Do Programa")
                print("============================")
                time.sleep(1.5)
                view.limparTerminal()
                # Interrompe o loop e encerra o programa
                break