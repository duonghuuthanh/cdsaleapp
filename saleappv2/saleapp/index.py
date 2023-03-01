from flask import render_template, request
from saleapp.models import Category
from saleapp import app, admin, dao


@app.route("/")
def index():
    kw = request.args.get('kw')
    cate_id = request.args.get('category_id')
    products = dao.get_products(kw=kw, category_id=cate_id)

    return render_template("index.html", products=products)


@app.route("/products/<int:product_id>")
def details(product_id):
    product = dao.get_product_by_id(product_id)
    return render_template('details.html', product=product)


@app.context_processor
def common_attr():
    return {
        'categories': dao.get_categories()
    }


if __name__ == '__main__':
    app.run(debug=True)
