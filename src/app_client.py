# src/app_client.py
from flask import Flask, render_template, url_for

# Importa os módulos necessários para manipulação de caminhos e sistema
import sys
import os

# Adiciona o diretório pai ao sys.path para que os módulos possam ser importados corretamente
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controller.produto_controller import ProdutoController

app = Flask(__name__, template_folder="../templates/client", static_folder="../static/client")
controller = ProdutoController()

@app.route("/")
def loja():
    produtos = controller.listar_produtos()
    return render_template("index.html", produtos=produtos)

@app.route("/produto/<string:nome>")
def detalhe(nome):
    produtos = controller.listar_produtos()
    for p in produtos:
        if p.nome == nome:
            return render_template("produto.html", produto=p)
    return "Produto não encontrado", 404

if __name__ == '__main__':
    app.run(debug=True)