import flask as flsss
from flsss import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Produtos de exemplo
produtos = [
    {"id": 1, "nome": "Camisa", "preco": 49.90},
    {"id": 2, "nome": "Calça", "preco": 89.90},
    {"id": 3, "nome": "Tênis", "preco": 199.90}
]

# Carrinho de compras (memória temporária)
carrinho = []

@app.route('/')
def index():
    return render_template('index.html', produtos=produtos)

@app.route('/produto/<int:produto_id>')
def produto(produto_id):
    produto = next((p for p in produtos if p["id"] == produto_id), None)
    return render_template('produto.html', produto=produto)

@app.route('/adicionar/<int:produto_id>')
def adicionar(produto_id):
    produto = next((p for p in produtos if p["id"] == produto_id), None)
    if produto:
        carrinho.append(produto)
    return redirect(url_for('carrinho_view'))

@app.route('/carrinho')
def carrinho_view():
    total = sum(p["preco"] for p in carrinho)
    return render_template('carrinho.html', carrinho=carrinho, total=total)

if __name__ == '__main__':
    app.run(debug=True)
