from flask import Flask,render_template,request,blueprints
from corporation import details_produits,rechreche
from PageInitiale.recuperation_base import index

app = Flask(__name__)

app.register_blueprint(index)

@app.route('/recherhce', methods=['POST'])
def post_route():
    key_word = request.form['keyword']
    page = request.args.get('page', default=1, type=int)
    if page == 0:
        page = 1

    sort_order = request.args.get('sortOrder', default='False', type=str)
    return render_template('post_list.html', records=rechreche.cherche_employe(key_word, page), keyword=key_word, page=page)

@app.route('/detail_produit')
def detail_produit():
    productCode = request.args.get('productCode', default=-1, type=str)
    return render_template("detail_produit.html", productCode=productCode, state=details_produits.description_produit(productCode))

@app.route('/detail_line')
def detail_line():
    productLine = request.args.get('productLine', default=-1, type=str)
    return render_template("detail_line_produit.html", productLine=productLine, state=details_produits.description_produit_line(productLine))

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/ajoutProduit')
def ajout():
    return render_template('ajoutProduit.html')

@app.route('/achat')
def achat():
    return render_template('achat.html')

@app.route('/login')
def login():
    return render_template('login.html')
if __name__ == "__main__":
    app.run(debug=True)
