from flask import render_template, request
from saleapp import app, dao, admin


@app.route("/")
def index():
    kw = request.args.get('kw')
    category_id = request.args.get('category_id')
    products = dao.get_products(kw=kw, category_id=category_id)

    return render_template("index.html", products=products)


@app.route("/products/<int:product_id>")
def details(product_id):
    # product = {
    #     "id": 1,
    #     "name": "iPhone 7 Plus",
    #     "description": "Apple, 32GB, RAM: 3GB, iOS13",
    #     "price": 17000000,
    #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
    #     "category_id": 1
    # }
    product = dao.get_product_by_id(product_id)

    return render_template("details.html", product=product)


@app.context_processor
def common_attr():
    return {
        'categories': dao.get_categories()
    }


if __name__ == '__main__':
    app.run(debug=True)
