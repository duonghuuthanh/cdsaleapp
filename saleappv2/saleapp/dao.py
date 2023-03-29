from saleapp.models import Category, Product, User, Receipt, ReceiptDetails
from saleapp import db, app
from flask_login import current_user
from sqlalchemy import func
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


def add_user(username, password, name, avatar):
    password = str(hashlib.md5(password.encode('utf-8')).hexdigest())
    u = User(name=name, username=username, password=password, avatar=avatar)
    db.session.add(u)
    db.session.commit()


def add_receipt(cart):
    if cart:
        r = Receipt(user_id=current_user.id)
        db.session.add(r)

        for p in cart.values():
            d = ReceiptDetails(receipt=r,
                               product_id=p['id'],
                               quantity=p['quantity'],
                               unit_price=p['price'])
            db.session.add(d)

        db.session.commit()


def revenue_by_product():
    return db.session.query(Product.id, Product.name,
                            func.sum(ReceiptDetails.unit_price * ReceiptDetails.quantity))\
                     .join(ReceiptDetails, ReceiptDetails.product_id.__eq__(Product.id), isouter=True)\
                     .group_by(Product.id).all()


def count_product_by_cate():
    return db.session.query(Category.id, Category.name, func.count(Product.id))\
             .join(Product, Product.category_id.__eq__(Category.id), isouter=True)\
             .group_by(Category.id).all()


if __name__ == '__main__':
    with app.app_context():
        print(revenue_by_product())


