from sqlalchemy import Column, String, Integer, Float, ForeignKey, Text
from sqlalchemy.orm import relationship
from saleapp import db, app
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    avatar = Column(String(100))
    username = Column(String(50), nullable=False)
    password = Column(String(100), nullable=False)
    user_role = Column(String(20), default='USER')

    def __str__(self):
        return self.name


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    price = Column(Float, default=0)
    image = Column(String(100))
    category_id = Column(Integer, ForeignKey(Category.id))

    def __str__(self):
        return self.name


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        import hashlib

        u = User(username='demo', password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),
                 name='ABC DEF',
                 avatar='https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg')
        db.session.add(u)
        db.session.commit()

        # c1 = Category(name='Điện thoại di động')
        # c2 = Category(name='Máy tính bảng')
        # db.session.add_all([c1, c2])
        # db.session.commit()
        #
        # products = [{
        #     "id": 1,
        #     "name": "iPhone 7 Plus",
        #     "description": "Apple, 32GB, RAM: 3GB, iOS13",
        #     "price": 17000000,
        #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
        #     "category_id": 1
        # }, {
        #     "id": 2,
        #     "name": "iPad Pro 2020",
        #     "description": "Apple, 128GB, RAM: 6GB",
        #     "price": 37000000,
        #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
        #     "category_id": 2
        # }, {
        #     "id": 3,
        #     "name": "Galaxy Note 10 Plus",
        #     "description": "Samsung, 64GB, RAML: 6GB",
        #     "price": 24000000,
        #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
        #     "category_id": 1
        # }, {
        #     "id": 4,
        #     "name": "Galaxy S23",
        #     "description": "Samsung, 64GB, RAML: 6GB",
        #     "price": 24000000,
        #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
        #     "category_id": 1
        # }, {
        #     "id": 5,
        #     "name": "Galaxy S22",
        #     "description": "Samsung, 64GB, RAML: 6GB",
        #     "price": 24000000,
        #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
        #     "category_id": 1
        # }, {
        #     "id": 6,
        #     "name": "Galaxy S22",
        #     "description": "Samsung, 64GB, RAML: 6GB",
        #     "price": 24000000,
        #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
        #     "category_id": 1
        # }, {
        #     "id": 7,
        #     "name": "Galaxy S22",
        #     "description": "Samsung, 64GB, RAML: 6GB",
        #     "price": 24000000,
        #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
        #     "category_id": 1
        # }]
        #
        # for p in products:
        #     del p['id']
        #     pro = Product(**p)
        #     db.session.add(pro)
        #
        # db.session.commit()

        # import hashlib
        # u1 = User(username='admin', password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()), name='Le Duong',
        #           avatar='https://res.cloudinary.com/dxxwcby8l/image/upload/v1670424381/eukjxogflweriqo6jg8k.png')
        # u2 = User(username='thanh', password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()), name='Minh Nguyen',
        #           avatar='https://res.cloudinary.com/dxxwcby8l/image/upload/v1670424381/eukjxogflweriqo6jg8k.png')
        # db.session.add_all([u1, u2])
        # db.session.commit()
