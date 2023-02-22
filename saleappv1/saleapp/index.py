from flask import render_template

from saleapp import app


@app.route("/")
def index():
    categories = [{
        "id": 1,
        "name": "Điện thoại di động"
    }, {
        "id": 2,
        "name": "Máy tính bảng"
    }, {
        "id": 3,
        "name": "Máy tính bàn"
    }]

    products = [{
        "id": 1,
        "name": "iPhone 7 Plus",
        "description": "Apple, 32GB, RAM: 3GB, iOS13",
        "price": 17000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
        "category_id": 1
    }, {
        "id": 2,
        "name": "iPad Pro 2020",
        "description": "Apple, 128GB, RAM: 6GB",
        "price": 37000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
        "category_id": 2
    }, {
        "id": 3,
        "name": "Galaxy Note 10 Plus",
        "description": "Samsung, 64GB, RAML: 6GB",
        "price": 24000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
        "category_id": 1
    }, {
        "id": 4,
        "name": "Galaxy S23",
        "description": "Samsung, 64GB, RAML: 6GB",
        "price": 24000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
        "category_id": 1
    }, {
        "id": 5,
        "name": "Galaxy S22",
        "description": "Samsung, 64GB, RAML: 6GB",
        "price": 24000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
        "category_id": 1
    }, {
        "id": 6,
        "name": "Galaxy S22",
        "description": "Samsung, 64GB, RAML: 6GB",
        "price": 24000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
        "category_id": 1
    }, {
        "id": 7,
        "name": "Galaxy S22",
        "description": "Samsung, 64GB, RAML: 6GB",
        "price": 24000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
        "category_id": 1
    }]

    return render_template("index.html", categories=categories, products=products)


@app.route("/products/<int:product_id>")
def details(product_id):
    product = {
        "id": 1,
        "name": "iPhone 7 Plus",
        "description": "Apple, 32GB, RAM: 3GB, iOS13",
        "price": 17000000,
        "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
        "category_id": 1
    }

    return render_template("details.html", product=product)


if __name__ == '__main__':
    app.run(debug=True)
