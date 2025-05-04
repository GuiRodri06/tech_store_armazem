# src/app_admin.py
from flask import Flask, render_template, request, redirect, url_for

# Importa os módulos necessários para manipulação de caminhos e sistema
import sys
import os

# Adiciona o diretório pai ao sys.path para que os módulos possam ser importados corretamente
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controller.produto_controller import ProdutoController

# Configura pasta de templates e static para o projeto
app = Flask(__name__, template_folder="../templates/admin", static_folder="../static")

controller = ProdutoController()

@app.route("/admin")
def admin_index():
    categoria = request.args.get('categoria', '')
    faixa_preco = request.args.get('faixa_preco', '')

    produtos = controller.listar_produtos()

    # Filtro por categoria
    if categoria:
        produtos = [p for p in produtos if p.categoria == categoria]

    # Filtro por faixa de preço
    if faixa_preco:
        if faixa_preco == "0-100":
            produtos = [p for p in produtos if p.preco <= 100]
        elif faixa_preco == "101-200":
            produtos = [p for p in produtos if 101 <= p.preco <= 200]
        elif faixa_preco == "201-300":
            produtos = [p for p in produtos if 201 <= p.preco <= 300]
        elif faixa_preco == "301-400":
            produtos = [p for p in produtos if 301 <= p.preco <= 400]
        elif faixa_preco == "401-500":
            produtos = [p for p in produtos if 401 <= p.preco <= 500]
        elif faixa_preco == "501-":
            produtos = [p for p in produtos if p.preco > 500]

    return render_template("index.html", produtos=produtos)

@app.route("/admin/adicionar", methods=["GET", "POST"])
def adicionar_produto():
    if request.method == "POST":
        nome = request.form['nome']
        categoria = request.form['categoria']
        preco = float(request.form['preco'])
        quantidade = int(request.form['quantidade'])
        controller.adicionar_produto(nome, categoria, preco, quantidade)
        return redirect(url_for("admin_index"))
    return render_template("adicionar.html")

@app.route("/admin/atualizar/<string:nome>", methods=["GET", "POST"])
def atualizar_produto(nome):
    produto = controller.buscar_produto_por_nome(nome)  # Busca o produto pelo nome
    if request.method == "POST":
        nova_quantidade = int(request.form['quantidade']) if request.form['quantidade'] else produto.quantidade
        novo_preco = float(request.form['preco']) if request.form['preco'] else produto.preco
        novo_nome = request.form['novo_nome'] if request.form['novo_nome'] else produto.nome
        nova_categoria = request.form['categoria'] if request.form['categoria'] else produto.categoria  # Captura a nova categoria
        
        controller.atualizarQuantidade(nome, nova_quantidade)  # Atualiza a quantidade
        controller.atualizarPreco(nome, novo_preco)            # Atualiza o preço
        controller.atualizarNome(nome, novo_nome)              # Atualiza o nome
        controller.atualizarCategoria(nome, nova_categoria)     # Atualiza a categoria
        
        return redirect(url_for("admin_index"))
    
    return render_template("atualizar.html", produto=produto)  # Passa o produto para o template

@app.route("/admin/remover/<string:nome>", methods=["POST"])
def remover_produto(nome):
    controller.remover_produto(nome)
    return redirect(url_for("admin_index"))

# Nova rota para busca de produtos com resultado múltiplo
@app.route("/admin/buscar", methods=["GET", "POST"])
def buscar_produto():
    termo = ''
    resultados = []
    if request.method == "POST":
        termo = request.form.get('nome', '').strip()
        if termo:
            resultados = controller.buscar_produtos_fuzzy(termo)
    elif request.method == "GET":
        termo = request.args.get('nome', '').strip()
        if termo:
            resultados = controller.buscar_produtos_fuzzy(termo)
    return render_template("buscar.html", produtos=resultados, termo=termo)

if __name__ == '__main__':
    app.run(debug=True)