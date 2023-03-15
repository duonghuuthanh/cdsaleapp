from flask import render_template, request, redirect, session
from saleapp import app, admin, dao, login
from flask_login import login_user, logout_user
import cloudinary.uploader


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


@app.route("/login")
def my_login():
    return render_template("login.html")


@app.route("/login", methods=['post'])
def login_process():
    username = request.form['username']
    password = request.form['password']
    u = dao.auth_user(username, password)
    if u:
        login_user(u)
        return redirect("/")

    return render_template("login.html")


@app.route('/logout')
def my_logout():
    logout_user()
    return redirect("/login")


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/register', methods=['post'])
def register_process():
    data = request.form
    password = data['password']
    confirm = data['confirm']
    if password.__eq__(confirm):
        username = data['username']
        name = data['name']
        try:
            res = cloudinary.uploader.upload(request.files['avatar'])
            dao.add_user(username=username, password=password, name=name, avatar=res['secure_url'])
            return redirect('/login')
        except Exception as ex:
            err = str(ex)
    else:
        err = 'Password does not match!!!'

    return render_template('register.html', err=err)


@app.route('/cart')
def cart():
    return render_template('cart.html')


@app.route('/order/<int:product_id>')
def order_item(product_id):
    p = dao.get_product_by_id(product_id)

    cart = {}
    if 'cart' in session:
        cart = session['cart']

    product_id = str(product_id)

    if product_id in cart:
        cart[product_id]['quantity'] = cart[product_id]['quantity'] + 1
    else:
        cart[product_id] = {
            "id": p.id,
            "name": p.name,
            "price": p.price,
            "quantity": 1
        }

    session['cart'] = cart

    return redirect('/cart')


@app.context_processor
def common_attr():
    return {
        'categories': dao.get_categories()
    }


@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


if __name__ == '__main__':
    app.run(debug=True)
