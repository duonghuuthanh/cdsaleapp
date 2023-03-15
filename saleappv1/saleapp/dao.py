from saleapp.models import Category, Product, User
from saleapp import db
import hashlib


def get_categories():
    return Category.query.all()


def get_products(kw=None, category_id=None):
    query = Product.query

    if kw:
        query = query.filter(Product.name.contains(kw))

    if category_id:
        query = query.filter(Product.category_id.__eq__(category_id))

    return query.all()


def get_product_by_id(product_id):
    return Product.query.get(product_id)


def get_user_by_id(user_id):
    return User.query.get(user_id)


def auth_user(username, password):
    password = str(hashlib.md5(password.encode('utf-8')).hexdigest())

    return User.query.filter(User.username.__eq__(username),
                             User.password.__eq__(password)).first()


def add_user(name, username, password, avatar=''):
    password = str(hashlib.md5(password.encode('utf-8')).hexdigest())
    u = User(name=name, username=username, password=password, avatar=avatar)
    db.session.add(u)
    db.session.commit()

