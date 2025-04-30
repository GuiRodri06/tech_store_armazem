# src/app_admin.py
from flask import Flask, render_template, request, redirect, url_for

# Importa os módulos necessários para manipulação de caminhos e sistema
import sys
import os

# Adiciona o diretório pai ao sys.path para que os módulos possam ser importados corretamente
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controller.produto_controller import ProdutoController

app = Flask(__name__, template_folder="../templates/admin", static_folder="../static/admin")
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
    if request.method == "POST":
        nova_quantidade = int(request.form['quantidade'])
        novo_preco = float(request.form['preco'])
        novo_nome = request.form['novo_nome']
        controller.atualizarQuantidade(nome, nova_quantidade)
        controller.atualizarPreco(nome, novo_preco)
        controller.atualizarNome(nome, novo_nome)
        return redirect(url_for("admin_index"))
    return render_template("atualizar.html", nome=nome)

@app.route("/admin/remover/<string:nome>", methods=["POST"])
def remover_produto(nome):
    controller.remover_produto(nome)
    return redirect(url_for("admin_index"))

if __name__ == '__main__':
    app.run(debug=True)