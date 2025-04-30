# Importa as bibliotecas do Flask necessárias para criar rotas, renderizar templates e redirecionar páginas
from flask import Flask, render_template, request, redirect, url_for

# Importa os módulos necessários para manipulação de caminhos e sistema
import sys
import os

# Adiciona o diretório pai ao sys.path para que os módulos possam ser importados corretamente
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importa o controlador responsável pelas operações nos produtos
from controller.produto_controller import ProdutoController

# Cria a aplicação Flask, informando onde estão os templates e os arquivos estáticos
app = Flask(
    __name__,
    template_folder='../view/templates',  # Onde ficam os arquivos HTML
    static_folder='../static'             # Onde ficam os arquivos CSS, JS, imagens etc.
)

# Cria uma instância do controlador, que conecta a aplicação com o modelo de dados
controller = ProdutoController()


# Rota principal ("/") que exibe a lista de produtos no estoque
@app.route('/')
def index():
    produtos = controller.listar_produtos()           # Busca todos os produtos usando o controller
    return render_template('index.html', produtos=produtos)  # Renderiza o HTML com a lista de produtos


# Rota para adicionar um novo produto (GET exibe o formulário, POST salva no banco)
@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar_produto():
    if request.method == 'POST':                           # Se o formulário foi enviado (POST)
        nome = request.form['nome']                        # Pega o nome do produto do formulário
        categoria = request.form['categoria']              # Pega a categoria
        preco = float(request.form['preco'])               # Pega o preço e converte para float
        quantidade = int(request.form['quantidade'])       # Pega a quantidade e converte para int
        controller.adicionar_produto(nome, categoria, preco, quantidade)  # Chama o controller para salvar
        return redirect(url_for('index'))                  # Redireciona de volta para a página inicial
    return render_template('adicionar.html')               # Se for GET, exibe o formulário de cadastro


# Rota para remover um produto pelo nome
@app.route('/remover/<string:nome>', methods=['POST'])
def remover_produto(nome):
    controller.remover_produto(nome)                       # Chama o controller para remover o produto pelo nome
    return redirect(url_for('index'))                      # Redireciona de volta para a lista


# Rota para atualizar informações de um produto
@app.route('/atualizar/<string:nome>', methods=['GET', 'POST'])
def atualizar_produto(nome):
    if request.method == 'POST':                           # Se o formulário foi enviado (POST)
        nova_quantidade = int(request.form['quantidade'])  # Nova quantidade informada
        novo_preco = float(request.form['preco'])          # Novo preço informado
        novo_nome = request.form['novo_nome']              # Novo nome informado
        controller.atualizarQuantidade(nome, nova_quantidade)  # Atualiza quantidade no banco
        controller.atualizarPreco(nome, novo_preco)             # Atualiza preço no banco
        controller.atualizarNome(nome, novo_nome)               # Atualiza nome no banco
        return redirect(url_for('index'))                  # Redireciona para a página inicial
    return render_template('atualizar.html', nome=nome)    # Se for GET, mostra formulário com o nome atual


# Rota para realizar uma venda (escolher produto e quantidade)
@app.route('/vender', methods=['GET', 'POST'])
def vender():
    if request.method == 'POST':                           # Se o formulário foi enviado (POST)
        produto_id = int(request.form['produto_id'])       # ID do produto selecionado
        quantidade = int(request.form['quantidade'])       # Quantidade a vender
        controller.registrar_venda(produto_id, quantidade) # Registra a venda e atualiza estoque via controller
        return redirect(url_for('index'))                  # Redireciona para a página inicial
    produtos = controller.listar_produtos()                # Se for GET, busca produtos disponíveis para o select
    return render_template('venda.html', produtos=produtos)# Exibe o formulário de venda


# Executa o app se esse arquivo for rodado diretamente (modo desenvolvimento)
if __name__ == '__main__':
    app.run(debug=True)    # Inicia o servidor Flask com modo debug ativado (útil para testes)