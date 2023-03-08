from flask import render_template, request, redirect
from saleapp import app, admin, dao, login
from flask_login import login_user, logout_user


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
