from saleapp.models import Category, Product, User, Receipt, ReceiptDetails, Comment
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


def add_user(name, username, password, avatar=''):
    password = str(hashlib.md5(password.encode('utf-8')).hexdigest())
    u = User(name=name, username=username, password=password, avatar=avatar)
    db.session.add(u)
    db.session.commit()


def add_receipt(cart):
    if cart:
        receipt = Receipt(user_id=current_user.id)
        db.session.add(receipt)

        for d in cart.values():
            detail = ReceiptDetails(product_id=d['id'],
                                    receipt=receipt,
                                    unit_price=d['price'],
                                    quantity=d['quantity'])
            db.session.add(detail)

        db.session.commit()


def revenue_by_product():
    return db.session.query(Product.id, Product.name,
                            func.sum(ReceiptDetails.unit_price*ReceiptDetails.quantity))\
             .join(ReceiptDetails, ReceiptDetails.product_id.__eq__(Product.id), isouter=True)\
             .group_by(Product.id).all()


def count_products_by_cate():
    return db.session.query(Category.id, Category.name, func.count(Product.id))\
             .join(Product, Product.category_id.__eq__(Category.id), isouter=True)\
             .group_by(Category.id).all()


def get_comments_by_prod_id(prod_id):
    return Comment.query.filter(Comment.product_id.__eq__(prod_id)).order_by(-Comment.id).all()


def add_comment(content, product_id):
    from datetime import datetime
    c = Comment(content=content, product_id=product_id,
                user=current_user, created_date=datetime.now())
    db.session.add(c)
    db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        print(revenue_by_product())

