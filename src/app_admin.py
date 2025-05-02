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
    produtos = controller.listar_produtos()
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
    # Busca o produto pelo nome
    produto = controller.buscar_produto_por_nome(nome)  # Método que você deve implementar
    if request.method == "POST":
        nova_quantidade = int(request.form['quantidade']) if request.form['quantidade'] else produto['quantidade']
        novo_preco = float(request.form['preco']) if request.form['preco'] else produto['preco']
        novo_nome = request.form['novo_nome'] if request.form['novo_nome'] else produto['nome']
        
        # Atualiza o produto
        controller.atualizarQuantidade(nome, nova_quantidade)
        controller.atualizarPreco(nome, novo_preco)
        controller.atualizarNome(nome, novo_nome)
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
    return render_template("buscar_resultados.html", produtos=resultados, termo=termo)

if __name__ == '__main__':
    app.run(debug=True)