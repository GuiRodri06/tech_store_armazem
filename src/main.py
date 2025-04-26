# main.py

# Importa os módulos necessários para manipulação de caminhos e sistema
import sys
import os

# Adiciona o diretório pai ao sys.path para que os módulos possam ser importados corretamente
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controller.produto_controller import ProdutoController # Importa a classe ProdutoController
from view.opcoesView import OpcoesView # Importa a classe TerminalView

def main():
    
    view = OpcoesView() # Cria uma instância da visualização do terminal
    view.opcoesMenu()

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    # Chama a função principal para iniciar o programa
    main()